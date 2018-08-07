from django.conf.urls import url
from snippets import views

urlpatterns = [
    url('snippets', views.SnippetList.as_view()),
    url('snippets/<int:pk>', views.SnippetDetail.as_view()),
    url('users', views.UserList.as_view()),
    url('users/<int:pk>', views.UserDetail.as_view()),
]
