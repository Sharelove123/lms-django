from django.shortcuts import render



def home(request):
    def home(request):
        context = {
            'data':'okay'
        }
    return render(request, 'core/home.html')
