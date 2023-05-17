from django.shortcuts import render
from django.http import HttpResponse
import joblib
from joblib import load
# Create your views here.


def index(request):
    return render(request,'index.html')
def form(request):
    return render(request,'form.html')
def result(request):
    cls = joblib.load('model.joblib')
    Places = request.POST['DZ']
    Year = request.POST['Y']
    Month = request.POST['M']
    Tmax = request.POST['TM']
    Tmin = request.POST['TI']
    Rh = request.POST['RH']
    WindSpeed = request.POST['WS']
    y_pred = cls.predict([[Places,Year,Month,Tmax,Tmin,Rh,WindSpeed]])
    final = str(y_pred).replace('[','').replace(']','')

    #  print(y_pred)

    return render(request,"result.html",{'result':final,'max':Tmax,'min':Tmin,'rh':Rh,'speed':WindSpeed,'location':Places,'year':Year})
    