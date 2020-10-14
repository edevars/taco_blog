"""Users URLs"""

from django.urls import path

from users import views

urlpatterns = [

    # Management
    path(route='login', view=views.ClassLoginView.as_view(), name="login"),
]
