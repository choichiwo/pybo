from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# ---------------------------------- [edit] ---------------------------------- #
from django.shortcuts import render, get_object_or_404, redirect
# ---------------------------------------------------------------------------- #
# ---------------------------------- [edit] ---------------------------------- #
from .models import Question
from django.utils import timezone
# ---------------------------------------------------------------------------- #
# ---------------------------------- [edit] ---------------------------------- #
from .forms import QuestionForm
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
# ---------------------------------- [edit] ---------------------------------- #
def detail(request, question_id):
    """
    pybo 내용 출력
    """
# ---------------------------------- [edit] ---------------------------------- #
    question = get_object_or_404(Question, pk=question_id)
# ---------------------------------------------------------------------------- #
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)
# ---------------------------------------------------------------------------- #
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
# ---------------------------------------------------------------------------- #
# ---------------------------------- [edit] ---------------------------------- #
    return redirect('pybo:detail', question_id=question.id)
# ---------------------------------------------------------------------------- #
def question_create(request):
    """
    pybo 질문등록
    """
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})
# ---------------------------------------------------------------------------- #
    if request.method == 'POST':
        form = QuestionForm(request.POST)