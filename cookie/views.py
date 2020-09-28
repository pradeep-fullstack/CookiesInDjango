from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request,'cookie/index.html')

def setcookie(request):
    name="gagan"
    pas=" 123"
    my_data=name+pas
    response = render(request,'cookie/index.html',{'rs':"cookies setted"})
    response.set_cookie('cname',my_data)
    return response

def getcookie(request):
    a  = request.COOKIES['pk']
    return HttpResponse("value is "+ a);