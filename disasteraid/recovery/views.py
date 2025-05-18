from django.shortcuts import render

# Create your views here.

def recovery_home(request):
    return render(request, 'recovery.html')  # Replace with actual template
