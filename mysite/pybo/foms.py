from django import forms

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
# ---------------------------------------------------------------------------- #
