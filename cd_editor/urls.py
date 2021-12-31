from django.urls import path
from .views import cd_editor, save_diagram

urlpatterns = [
    path('cd-editor', cd_editor, name='cd_editor'),
]