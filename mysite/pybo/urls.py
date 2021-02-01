from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
# ---------------------------------- [edit] ---------------------------------- #
    path('<int:question_id>/', views.detail),
# ---------------------------------------------------------------------------- #
]