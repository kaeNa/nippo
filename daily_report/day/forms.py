# from django.forms import ModelForm
from django import forms
from .models import Report, Impression, Question, CommentQuestion


class ImpressionForm(forms.ModelForm):
    """感想のフォーム"""
    class Meta:
        model = Impression
        fields = ('comment_user', 'comment',)


class ReportForm(forms.ModelForm):
    """書籍のフォーム"""
    class Meta:
        model = Report
        # fields = ('name', 'publisher', )
        # fields = ( 'user','title', 'content')
        fields = ('user', 'title', 'content_Y', 'content_W', 'content_T')
        # fields = ( 'user','title', 'content', 'user_login_time', 'user_post_time')
        # fields = ('date', 'title', 'user',)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_content',)
        # fields = "__all__"


class AnswerForm(forms.ModelForm):
    class Meta:
        model = CommentQuestion
        fields = ('answer',)


class SearchForm(forms.Form):

    Search = forms.CharField(max_length=255)
    print('search')
