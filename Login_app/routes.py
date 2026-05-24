# views.py
from flask import render_template, session, redirect, url_for
from flask.views import View, MethodView
from auth import GoogleAuth

# Base class untuk proteksi login
class LoginRequiredView(View):
    def dispatch_request(self):
        if not auth.is_authenticated():
            return redirect(url_for('index'))
        return super().dispatch_request()

# View untuk halaman login (method GET saja)
class LoginPage(View):
    def dispatch_request(self):
        return render_template('login.html')

# View untuk dashboard (hanya bisa diakses jika login)
class DashboardView(LoginRequiredView):
    def dispatch_request(self):
        return render_template('dashboard.html', user_name=session.get('user_name'))

# Atau gunakan MethodView untuk menangani GET/POST dalam satu class
class AuthAction(MethodView):
    def get(self, action):
        if action == 'login':
            return auth.login()
        elif action == 'logout':
            return auth.logout()
        else:
            return redirect(url_for('index'))

# Kita tetap butuh endpoint untuk callback Google (tidak bisa dijadikan class-based dengan mudah, tapi bisa juga pakai MethodView)