from django.shortcuts import render, redirect

# Create your views here.
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST


def index(request):
    # QuerySet API -> 전체 데이터 조회 : Article.objects.all()
    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

@require_http_methods(["GET"])
def detail(request, pk):
    # QuerySet API -> 단일 데이터 조회 : get
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # article에서 comment를 가져오려는데 참조?? 역참조??
    # 역참조
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }

    # articles폴더에있는 detail.html파일을 랜더링하겠다. context를 넘겨주고,
    return render(request, 'articles/detail.html', context)



# 페이지 렌더링 + 리다이렉트 (if-else구조)
@login_required
@require_http_methods(["POST", "GET"])
def create(request):
    # submit버튼 눌렀을 때
    # print(request)
    if request.method == "POST":
        # request.POST ---> title, content
        # request.FILES ---> image, file 등..
        form = ArticleForm(request.POST, request.FILES)
        # 1. 모든 필수 필드가 채워져 있는지
        # 2. 입력된 데이터가 필드 조건을 만족하는지(데이터 타입, 길이 제한)
        if form.is_valid():
            # commit=False : DB에 바로 저장하지말고 일단 객체로 만들어라
            article = form.save(commit=False)
            # request.user : 로그인한 user
            article.user = request.user
            # DB에 저장
            article.save()
            return redirect('articles:detail', article.pk)
    
    else: # submit버튼 누르기 전, 다른 버튼(다른 요청 일때)
        form = ArticleForm() # 빈폼
    # GET요청
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

@login_required
@require_http_methods(["POST", "GET"])
def update(request, pk):
    # 조회 먼저 하고
    article = Article.objects.get(pk = pk)
    # submit버튼 눌렀을때
    if request.method == "POST":
        # 기존 게시글의 데이터를 미리 채운다(instance = article)
        form = ArticleForm(request.POST, request.FILES, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)

    else: # POST요청이 아닐 때
        form = ArticleForm(instance = article)
    context = {
        'article': article,
        'form': form
    }
    return render(request, 'articles/update.html', context)




# 단일 게시글 조회 후 삭제
@login_required
@require_http_methods(["POST"])
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    # 렌더링? 리다이렉트? : POST요청
    return redirect('articles:index')


@login_required
@require_http_methods(["POST"
                       
                       ])
def comments_create(request, pk):
    # 게시글 조회(QuerysetAPI)
    article = Article.objects.get(pk=pk)
    # request.POST : user가 입력한 content
    comment_form = CommentForm(request.POST)
    # 유효성 검사 
    if comment_form.is_valid():
        # commit=False : DB에 바로 저장 X
        comment = comment_form.save(commit=False)
        comment.article = article # 1. 게시글 객체
        comment.user = request.user # 2. 로그인한 user
        comment.save() # DB에 저장
        return redirect('articles:detail', article.pk)
    # 유효성 검사 실패
    context = {
        'article': article,
        'comment_form': comment_form
    }
    return render(request, 'articles:detail.html', context)

def comments_delete(request, article_pk, comment_pk):
    # 댓글 조회
    comment = Comment.objects.get(pk=comment_pk)
    # request.user : 로그인한 user
    # comment.user : 댓글 작성한 user
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
