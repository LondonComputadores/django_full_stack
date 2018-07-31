from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage, AccessRecord

# Create your views here.
#return HttpResponse('Heya Pythonista') usar abaixo de def index so pra testar

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' :webpages_list}
    #my_dict = {'insert_me': "Heya! I was coming from views.py. Now I'm coming from first_app/index.html"}
    return render(request,'first_app/index.html',context=date_dict)
