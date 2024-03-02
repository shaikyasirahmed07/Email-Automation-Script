from django.urls import path
from . import views
urlpatterns = [
    path('', views.send_invitation, name='send_invitation'),
    path('send_invitation.html/', views.send_invitation, name='send_invitation'),
    path('send_invitation.html/send_invitation.html',views.send_invitation, name='send_invitation'),
]