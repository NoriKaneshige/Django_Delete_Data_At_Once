from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path('', views.PostIndex.as_view(), name='post_list'), # as_view() is necessary because PostIndex view uses ListView
    path('', views.postindex, name='post_list'), # as_view() is NOT necessary because postindex view is a nomal view
   
]