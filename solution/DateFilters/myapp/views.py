from django.shortcuts import render
from datetime import date, datetime

# Create your views here.

def home_function(request):
    date_str = '12-30-2019'
    date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
    context = {
        'date': date_object,
        'string': "Tech Academy is coding bootcamp",
        'length': 10
     }
    return render(request, 'home.html', context)