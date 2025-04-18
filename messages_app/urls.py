from django.urls import path
from . import views

app_name = 'messages_app'

urlpatterns = [
    path('',          views.inbox,         name='inbox'),
    path('new/',      views.new_message,   name='new'),
    path('<int:pk>/', views.thread_detail, name='thread_detail'),
]
