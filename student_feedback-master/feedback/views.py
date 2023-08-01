from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
#from .models import User



# Create your views here.
def index(request):
    return render(request, "index.html")


def signin(request):
    return render(request, "signin.html")

# myapp/views.py

'''def signin(request):
    if request.method == 'POST':
        username = request.POST.get('email_address')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email_address=email_address, password=password)
            # Redirect to a success page or perform other actions
        except User.DoesNotExist:
            # Handle unsuccessful sign-in, such as displaying an error message
            pass

    return render(request, 'signin.html')

'''