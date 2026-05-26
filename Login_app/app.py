# app.py
from flask import Flask
from auth import GoogleAuth
from routes import LoginPage, DashboardView, AuthAction
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = 'rahasia_kuat_untuk_session_2026'
    
    # Gunakan environment variable atau isi langsung (untuk sementara)
    app.config['GOOGLE_CLIENT_ID'] = os.environ.get('GOOGLE_CLIENT_ID', '972630016919-ltr018mk4jccb3ol07pml2i23kcfcm4s.apps.googleusercontent.com')
    app.config['GOOGLE_CLIENT_SECRET'] = os.environ.get('GOOGLE_CLIENT_SECRET', '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')

    # Inisialisasi GoogleAuth
    auth = GoogleAuth(app)
    app.auth = auth  # simpan sebagai atribut app

    # Daftarkan class-based views
    app.add_url_rule('/', view_func=LoginPage.as_view('index'))
    app.add_url_rule('/dashboard', view_func=DashboardView.as_view('dashboard'))
    app.add_url_rule('/auth/<action>', view_func=AuthAction.as_view('auth'))

    # Route callback Google
    @app.route('/login/callback')
    def auth_callback():
        return app.auth.callback()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)