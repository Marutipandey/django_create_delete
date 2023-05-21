from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import simpleform
from .forms import loginform


# Create your views here.
def index(request):
    if request.method=='POST':
       form = loginform(request.POST)
       if form.is_valid():
           form.save()
    else:
        form =loginform()
    user =simpleform.objects.all()
    return render(request, 'enroll/index.html',{'form':form,'user':user})


def deletedataa(request, id):
    user=simpleform.objects.get(pk=id)
    user.delete() 
    return redirect('/',{'user':user})

