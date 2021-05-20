from django.shortcuts import render
from .forms import SignInForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from App.models import Client


@receiver(post_save, sender=Client )
def my_handler(sender, **kwargs):
    print('')

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

    if request.method == 'POST':
        print('test kely')
        form = SignInForm(request.POST)
        if form.is_valid():
            #request.POST.get('name')
            # collect data for login template save data 


            name = form.cleaned_data['UserName']
            email =  form.cleaned_data['UserEmail']
            password = form.cleaned_data['Password']
            print( name , email , password )
            data = Client(userName = name, userEmail = email, userPassword = password )
            data.save()
            context ={
                'name':name,
                'email':email,
            }
            return render(request, 'home.html', context)
        else:
        
            context ={
                'form':form,
                'errors': form.errors.items()
            }
            return render(request, 'login.html',context)

    
    
