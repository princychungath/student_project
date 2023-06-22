from django.shortcuts import render, redirect
from .forms import StudentForm
from django.views.generic import ListView
from .models import Student
from django.http import HttpResponse

def add_student(request):
    if request.method == "POST":
        form=StudentForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponse('Student is added!')
    else:
        form=StudentForm()
        return render(request,'student_app/add_student.html',{'form':form})
        
class Homepage(ListView):
    template_name="student_app/display.html"
    queryset=Student.objects.all()
    context_object_name="students"