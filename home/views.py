from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    university = 'karabuk university'
    department = 'enginering'
    context={'university':university,'department':department}
    return render(request,'index.html',context)
