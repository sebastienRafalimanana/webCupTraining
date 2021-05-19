from django.shortcuts import render
from .forms import SignInForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from App.models import user


@receiver(post_save, sender=user )
def my_handler(sender, **kwargs):
    print(user.userEmail)

# Create your views here.

def login( request ):
    form = SignInForm()
    context ={
            'form': form
        }
    return render(request, 'login.html',context)

   
def signIn( request ):
    #return render(request, 'signIn.html')
    pass


def home( request):

    if request == 'POST':
        print('test kely')
        form = SignInForm(request.POST)
        if form.is_valide():

            #request.POST.get('name')

            name = form.cleaned_data['UserName']
            email =  form.cleaned_data['UserEmail']
            password = form.cleaned_data['Password']
            print( name , email , password )
            data = user(
              UserName = name,
              UserEmail = email,
              Password = password
            )
            return render(request, 'home.html',context)
        else:
            context['errors'] = form.errors.items()
            return render(request, 'login.html',context)

    return render(request, 'home.html')
    
