from django.shortcuts import render
from .forms import MyForm, rData
import joblib
import numpy as np
import pandas as pd
# Create your views here.
def index(request):
    return render(request,"index.html")

# app/views.py
def loadInfo():
    encoding_info1=joblib.load('./static/EncodingInfo.pkl')
    return encoding_info1
def preprocessSVM(state, district, crop, date, season, area, yieldd):
    # Convert string inputs to numerical values using encoding mappings
    encoding_info=loadInfo()
    state = encoding_info['State'][state]
    district = encoding_info['District'][district]
    crop = encoding_info['Crop'][crop]
    season = encoding_info['Season'][season]
    
    # As date and area are numeric, no conversion needed
    
    test_data = np.array([[state, district, crop, date, season, area,yieldd]])
    trained_model = joblib.load("./static/SVMmodel.pkl")
    prediction = trained_model.predict(test_data)
    return prediction



from .forms import MyForm

def my_form_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process the form data
            a = form.cleaned_data
            pr = preprocessSVM(a['field1'], a['field2'], a['field3'], a['field4'], a['field5'], int(a['field6']), 0.25)
            form.cleaned_data['result']=pr
            return render(request, 'success.html', {'data': form.cleaned_data})
        
    else: 
        form = MyForm()
    return render(request, 'my_form.html', {'form': form})

