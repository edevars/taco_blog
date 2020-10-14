"""Users URLs"""

from django.urls import path

from users import views

urlpatterns = [

    # Management
    path(route='login', view=views.ClassLoginView.as_view(), name="login"),
    path(route='logout', view=views.ClassLogoutView.as_view(), name="logout"),
    path(route='signup', view=views.SignUpView.as_view(), name="signup"),
]
