from django.urls import path
from .views import *

urlpatterns = [
    path('', ListTodoViews.as_view(), name='list_todos'),
    path('<int:pk>/delete', DeleteTodoViews.as_view(), name='delete_todo'),
    path('create/', CreateTodoViews.as_view(), name='create_todo'),
    path('<int:pk>/update/', EditTodoView.as_view(), name='update_todo'),
    path('<int:pk>/detail/', DetailTodoView.as_view(), name='detail_todo'),

    # path('api_todo/', todo_list_serializer, name='api_todo'),
    # path('api_todo/<int:pk>/', todo_detail_serializer, name='api_todo'),

    # Using class based views
    path('api_todo/', TodoListApi.as_view(), name='api_todo'),
    path('api_todo/<int:pk>/', DetailApi.as_view(), name='api_todo'),
    path('likes/<int:pk>/', like_todo, name='like_todo'),

    #Create like button
]
