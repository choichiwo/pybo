from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# ---------------------------------- [edit] ---------------------------------- #
from django.shortcuts import render
# ---------------------------------------------------------------------------- #
# ---------------------------------- [edit] ---------------------------------- #
from .models import Question
# ---------------------------------------------------------------------------- #
def index(request):
    # ---------------------------------- [edit] ---------------------------------- #
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    # ---------------------------------------------------------------------------- #
    # ---------------------------------- [edit] ---------------------------------- #
    return render(request, 'pybo/question_list.html', context)
    # ---------------------------------------------------------------------------- #
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")