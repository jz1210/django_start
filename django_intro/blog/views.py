from django.shortcuts import render

from django.http import HttpResponse
from blog.models import Article

# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World')

def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    date = article.date
    return_str = 'title: %s, brief_content: %s, content: %s,' \
                  ' article_id: %s, date: %s' %(title,
                                                brief_content,
                                                content,
                                                article_id,
                                                date)

    return HttpResponse(return_str)
