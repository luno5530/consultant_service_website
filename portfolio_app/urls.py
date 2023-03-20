
from django.contrib import admin
from django.urls import path
from .views import ProfileDetailsView

app_name = "portfolio_app"

urlpatterns = [
    path("profile/", ProfileDetailsView.as_view(), name="profile_details" )
]
