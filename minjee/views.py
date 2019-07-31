from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def hello(request):
    blogs = Blog.objects
    return render(request, 'hello.html', {'blogs':blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html',{'blogdetail': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/' + str(blog.id))


def delete(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect('/')

def update(request, blog_id):
    blog_update = get_object_or_404(Blog, pk=blog_id)
    return render(request,'update.html',{"blogupdate":blog_update})

def updatesend(request, blog_id):
    updateSendpost = get_object_or_404(Blog, pk=blog_id)
    updateSendpost.title = request.GET['updateTitle']
    updateSendpost.body = request.GET['updateBody']
    updateSendpost.pubdate = timezone.datetime.now()
    updateSendpost.save()
    return redirect('hello')
#pk - 어떤 기능?? 우리가 찾고자 하는 아이디 정해주는 것
#id 와 pk의 차이가 무엇일까 
#왜 여기다가는 pk를 해주지 않는 것일까??? 전역변수  지역변수는 함수내에서 정의 내려진 함수,
#redirect  지정해준 사이트로  간다~

def postcreate(request):
    posting = Post()
    posting.title = request.GET['postTitle']
    posting.body = request.GET['postBody']
    posting.dateTime = timezone.datetime.now()
    posting.save()
    return redirect('postView')

# def commentCreate(request,post_pk):
#     post = get_object_or_404(Post, pk=post_pk)
#     content = request.POST.get('content')
#     commentNLike.objects.create(post=post,comment=content)
#     return redirect('/mutsaposting/posting/postDetail/+str(post.id))

