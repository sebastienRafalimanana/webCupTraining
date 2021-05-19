from django import  forms 


class SignInForm(forms.Form) :
    UserName = forms.CharField(
                label='Username',
                 max_length= 50 ,
                 widget =forms.TextInput(attrs = {'class': 'form', 'placeholder':'UserName...'}),
                  required=True 
                  )
    
    UserEmail = forms.EmailField(
                label='E-mail',
                 widget =forms.EmailInput(attrs = {'class': 'form' , 'placeholder':'E-mail...'}),
                  required=True 
                  )
    
    Password = forms.CharField(
                label='Password',
                 max_length= 12 ,
                 widget =forms.PasswordInput(attrs = {'class': 'form ', 'placeholder':'Password...'}),
                  required=True 
                  )