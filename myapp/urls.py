from django.urls import path
app_name='myapp'
from myapp import views
urlpatterns=[
    path('get_demo/', views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
]