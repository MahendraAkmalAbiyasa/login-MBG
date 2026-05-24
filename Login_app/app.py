# app.py
from flask import Flask
from auth import GoogleAuth
from routes import LoginPage, DashboardView, AuthAction

def create_app():
    app = Flask(__name__)
    app.secret_key = 'rahasia_kuat_untuk_session_2026'
    app.config['GOOGLE_CLIENT_ID'] = '...'
    app.config['GOOGLE_CLIENT_SECRET'] = '...'

    # Inisialisasi GoogleAuth sebagai objek (OOP)
    global auth
    auth = GoogleAuth(app)

    # Daftarkan class-based views
    app.add_url_rule('/', view_func=LoginPage.as_view('index'))
    app.add_url_rule('/dashboard', view_func=DashboardView.as_view('dashboard'))
    app.add_url_rule('/auth/<action>', view_func=AuthAction.as_view('auth'))

    # Route callback (tetap fungsi biasa, tapi tetap OOP karena memanggil method objek)
    @app.route('/login/callback')
    def auth_callback():
        return auth.callback()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)