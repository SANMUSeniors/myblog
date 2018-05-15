from django.shortcuts import render
from django.http import HttpResponse
from django_web.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("Hello World,django")


def detail(request):
        post = Article.objects.all()
        str = ("title = %s, category = %s, date_time = %s, content = %s"
            % (post.title, post.category, post.date_time, post.content))
        return HttpResponse(str)
def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})

def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})