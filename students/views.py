
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=='POST':
        name=request.POST.get('sname')
        usn=request.POST.get('usn')
        email=request.POST.get('email')
        phone=request.POST.get('mob')
        college=request.POST.get('college')
        degree=request.POST.get('degree')
        branch=request.POST.get('branch')
        sem=request.POST.get('sem')
        
        
        print("Student Name:",name)
        print("USN",usn)
        print("Email",email)
        print("Phone",phone)
        print("degree",degree)
        print("college",college)
        print("Branch",branch)
        print("sem",sem)
        
        
    return render(request,'register.html')