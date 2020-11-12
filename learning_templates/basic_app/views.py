from django.shortcuts import render
def index(request):
    my_dict = {'text' : "welcome to my page" , 'date' :'22'}
    return render(request , 'basic_app/index.html' , my_dict)
def other(request) :
    return render(request , 'basic_app/other.html')
# Create your views here.
def relative(request) :
    return render(request , 'basic_app/relative_url_templates.html')
