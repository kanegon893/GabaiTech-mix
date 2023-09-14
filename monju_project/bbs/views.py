from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Article
from .forms import SearchForm
from .forms import ArticleForm # forms.pyからArticleFormクラスをインポート

def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        articles = Article.objects.filter(content__contains=keyword)
    else:
        searchForm = SearchForm()
        articles = Article.objects.all()

    context = {
    'articles': articles,
    'searchForm': searchForm,
    }
    return render(request, 'bbs/index.html', context)

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    context = {
        'article': article,
    }
    return render(request, 'bbs/detail.html', context)

# 新規投稿画面のWebページを返すnew関数
def new(request):
    articleForm = ArticleForm() # ArticleFormオブジェクトを生成
    # テンプレート側でarticleFormのデータを取り出せるようにcontextに渡す
    context = {
        'articleForm': articleForm,
    }
    return render(request, 'bbs/new.html', context) # new.htmlというテンプレートを返す

#新規投稿データを保存するcreate関数
def create(request):
    # リクエストのメソッドがPOSTなら
    if request.method == 'POST':
        articleForm = ArticleForm(request.POST) # リクエストから取り出したデータを代入
        # 受け取ったデータが正常なら
        if articleForm.is_valid():
            article = articleForm.save() # データを保存
    context = {
        'article': article,
    }
    return render(request, 'bbs/posted.html', context) # detail.htmlを返す

    # 投稿編集ページを返すedit関数
def edit(request, id):
    article = get_object_or_404(Article, pk=id) # 指定した投稿をarticle変数に代入
    articleForm = ArticleForm(instance=article) # ArticleFormクラスからarticleFormオブジェクトを生成
    context = {
        'article': article,
        'articleForm': articleForm,
    }
    return render(request, 'bbs/edit.html', context) # edit.htmlというテンプレートを返す

# 編集データを保存して個別投稿ページを返すupdate関数
def update(request, id):
    # リクエストのメソッドがPOSTなら
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=id)
        articleForm = ArticleForm(request.POST, instance=article) # ArticleFormクラスからarticleFormオブジェクトを生成
        # 受け取ったデータが正常なら
        if articleForm.is_valid():
            articleForm.save() # データを保存
    context = {
        'article': article,
    }
    return render(request, 'bbs/detail.html', context) # detail.htmlを返す

# 投稿データを削除するdelete関数
def delete(request, id):
    article = get_object_or_404(Article, pk=id) # 指定した投稿をarticle変数に代入
    article.delete()

    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'bbs/index.html', context) # index.htmlを返す
