# realtime_help/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import DisasterReport
from django.db import models
from datetime import datetime
import joblib
import os
import numpy as np

# Handle disaster report form
def report_disaster(request):
    if request.method == 'POST':
        disaster_type = request.POST.get('disaster_type')
        description = request.POST.get('description')
        location = request.POST.get('location')
        image = request.FILES.get('image')

        k = DisasterReport(
            disaster_type=disaster_type,
            description=description,
            location=location,
            image=image
        )
        k.save()

        return HttpResponse("Disaster reported!")
        
    return render(request, 'realtime_help/report.html')


# View all reports
def view_reports(request):
    reports = DisasterReport.objects.all()
    return render(request, 'realtime/view_reports.html', {'reports': reports})


# Predict disaster
def predict_disaster(request):
    prediction = None

    if request.method == 'POST':
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        wind_speed = float(request.POST.get('wind_speed'))
        rainfall = float(request.POST.get('rainfall'))

        input_data = np.array([[temperature, humidity, wind_speed, rainfall]])

        # Load the model
        model_path = os.path.join(os.path.dirname(__file__), 'disaster_predictor.pkl')
        model = joblib.load(model_path)

        prediction = model.predict(input_data)[0]

    return render(request, 'realtime_help/predict_disaster.html', {'prediction': prediction})
