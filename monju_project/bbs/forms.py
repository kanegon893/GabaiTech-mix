from django import forms
from .models import Article # models.pyからArticleクラスをインポート

# SearchFormクラスを定義
class SearchForm(forms.Form):
        keyword = forms.CharField(label='', max_length=50)

# 新規投稿フォームを定義
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content', 'user_name')
