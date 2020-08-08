from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'home':'active'}
    return render(request, 'core/home.html', context)

def contact(request):
    context = {'cnt':'active'}
    return render(request, 'core/contact.html', context)