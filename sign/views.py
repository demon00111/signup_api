from django.http import HttpResponseRedirect
from django.shortcuts import render

from sign.forms import AllData, UserData
from sign.models import SignupForm

# Create your views here.
def signup(request):
 
    if request.method == 'POST':
        name=request.POST.get('name')
        username= request.POST.get('username')
        password= request.POST.get('password')
        email= request.POST.get('email')

        reg = SignupForm(name=name,username=username,password=password,email=email)
        reg.save()

  

    else:
        reg= UserData()

    return render(request,'index.html',{"forms": reg})
 
 
# def signin(request):
#     if request.method == 'POST':
#         rs= UserData(request.POST)
        
#         if rs.is_valid():
#             rs.save()


#     else:
#         rs= UserData()

#     fs= AllData()
#     return render(request,'signin.html',{"signin": fs})

    
