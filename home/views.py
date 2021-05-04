from django.shortcuts import render,HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success':False}
    if request.method == 'POST':
        task = request.POST['task']    
        desc = request.POST['desc']  
        ins = Task(task=task,desc=desc)  
        ins.save()
        context = {'success':True}

    # HttpResponse('Data has been saved')
    return render(request,'index.html',context)
def task(request):
    allTask = Task.objects.all()
    context = {'task': allTask}
    return render(request,'task.html',context)


