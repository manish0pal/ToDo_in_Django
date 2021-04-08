from django.shortcuts import render,redirect
from .models import TodoWork
from django.contrib import messages
from datetime import datetime

def index(req):
    if req.method == "POST":
        task = req.POST.get('task')
        status= req.POST.get('status')
        print('task: ',task,'status: ',status)
        todos = TodoWork(title=task,status=status,today=datetime.today())
        #todos = TodoWork(id=11)
        todos.save()
        #todos.delete()
        messages.success(req , "Task Added")
        
    todow = TodoWork.objects.all()
    return render (req ,"base.html",{'todow':todow})
def del_task(req):
    id = req.POST.get('id')
    todos = TodoWork(id=id)
    todos.delete()
    return redirect('/')