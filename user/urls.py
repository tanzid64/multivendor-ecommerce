from django.urls import path, include, re_path
from .views import UserLoginView, GoogleLogin
from allauth.account.views import ConfirmEmailView
from .views import GoogleLogin, RedirectView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    re_path('confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(),name='account_confirm_email'),
    path('login/google/', GoogleLogin.as_view(), name='google_login'),
    path('~redirect/', RedirectView.as_view(), name='redirect'),
]
