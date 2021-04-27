from django import forms
from pybo.models import Question
# ---------------------------------- [edit] ---------------------------------- #
from pybo.models import Question, Answer
# ---------------------------------------------------------------------------- #

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
# ---------------------------------------------------------------------------- #
        # widget 항목 삭제
# ---------------------------------------------------------------------------- #