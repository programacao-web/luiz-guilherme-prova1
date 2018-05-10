from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pastebin-index'),
    path('<language>/', views.language_list, name='pastebin-language'),
    path('pastes/<int:id>/', views.paste, name='pastebin-detail'),
]
