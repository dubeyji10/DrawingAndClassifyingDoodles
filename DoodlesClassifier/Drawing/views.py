from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1> Home Page </h1>')

    
def draw(request):
    # return HttpResponse('<h2><font color="#ff0011">render the drawing page</font></h2>')

    return render(request,'drawing_board/draw.html',{'title': 'Drawing Board'})
