from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from baseapp.models import question,students
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        questions=question.objects.all()
        return render(request,"baseapp/index.html",{
            'questions':questions
        })

    else:
        return HttpResponse("Please login first to view questions")

def show_question(request,question_id):
    curr_question=question.objects.get(pk=question_id)
    curr_question_solvers=curr_question.solved_by.all()
    return render(request,"baseapp/question_shower.html",{
        'curr_question':curr_question,
        'curr_question_solvers':curr_question_solvers,
        'non_solvers': students.objects.exclude(student_solved_questions=curr_question)
    })

def add_name(request,question_id):
    if request.user.is_authenticated:
        if request.method=="POST":
            curr_question=question.objects.get(pk=question_id)
            curr_student=students.objects.get(pk=int(request.POST["stu_id"]))
            curr_student.student_solved_questions.add(curr_question)
            return HttpResponseRedirect(reverse("show_problem",args=(question_id,)))

    else:
        return HttpResponse("Please login first to view questions")