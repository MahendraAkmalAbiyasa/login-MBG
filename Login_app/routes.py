# routes.py
from flask import render_template, session, redirect, url_for
from flask.views import View, MethodView
from flask import current_app

class LoginPage(View):
    def dispatch_request(self):
        return render_template('login.html')

class DashboardView(View):
    def dispatch_request(self):
        if not current_app.auth.is_authenticated():
            return redirect(url_for('index'))
        return render_template('dashboard.html', user_name=session.get('user_name'))

class AuthAction(MethodView):
    def get(self, action):
        if action == 'login':
            return current_app.auth.login()
        elif action == 'logout':
            return current_app.auth.logout()
        else:
            return redirect(url_for('index'))