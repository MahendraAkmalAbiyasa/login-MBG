# auth.py
from flask import session, redirect, url_for
from authlib.integrations.flask_client import OAuth

class GoogleAuth:
    def __init__(self, app=None):
        self.app = app
        self.google = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        oauth = OAuth(app)
        self.google = oauth.register(
            name='google',
            client_id=app.config['GOOGLE_CLIENT_ID'],
            client_secret=app.config['GOOGLE_CLIENT_SECRET'],
            server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
            client_kwargs={'scope': 'openid email profile'}
        )

    def login(self):
        return self.google.authorize_redirect(url_for('auth_callback', _external=True))

    def callback(self):
        token = self.google.authorize_access_token()
        resp = self.google.get('https://www.googleapis.com/oauth2/v1/userinfo')
        user_info = resp.json()
        session['user'] = user_info
        session['user_id'] = user_info['id']
        session['user_name'] = user_info['name']
        return redirect(url_for('dashboard'))

    def logout(self):
        session.clear()
        return redirect(url_for('index'))

    def is_authenticated(self):
        return session.get('user') is not None