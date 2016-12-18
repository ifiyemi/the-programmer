from django.shortcuts import render
from .forms import PostForm
from django.shortcuts import redirect
from .models import RegDetails

# Create your views here.

def welcome(request):
    return render(request,'UserRegistration/welcome.html',{})


def lists(request):
    all_names = RegDetails.objects.order_by('name')
    all_emails = RegDetails.objects.order_by('mail_address')
    return render(request,'UserRegistration/list.html',{'all_names':all_names,'all_emails':all_emails})





def create(request):
    result= "Registration Successful"
    failed = "Registration failed"
    if request.method == "POST":
       newform = PostForm(request.POST)
       if newform.is_valid():
         # post = form.save(commit=False)
          #post.name = form.cleaned_data['name']
          #post.mail_address = form.cleaned_data['mail_address']
          #post.name = request.user
          #post.mail_address = request.user
          newform.save()

          return render(request, 'UserRegistration/add.html', {'form': newform,'result':result})
       else:
           myform = PostForm()
           return render(request, 'UserRegistration/add.html', {'form': myform,'failed':failed})


    else:
         forms = PostForm()
         return render(request, 'UserRegistration/add.html', {'form': forms})





