from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'preparedness.html')  # Replace with actual template
