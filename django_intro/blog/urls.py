from django.urls import path, include
import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.article_content)
]
