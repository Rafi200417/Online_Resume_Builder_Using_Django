from django.contrib import admin
from django.urls import path
from home.views import home, resume_preview, save_resume, login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', login_view, name='login_view'),
    path('register/', register_view, name='register_view'),
    path('logout/', logout_view, name='logout_view'),
    path('save/', save_resume, name='save_resume'),
    path('preview/<int:resume_id>/', resume_preview, name='resume_preview'),
]
