from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



import re
from io import BytesIO
import sys
import base64
from django.core.files.base import ContentFile
from django.core.files import File
from base64 import b64encode, b64decode
import os
from base64 import decodestring


def home(request):
    return HttpResponse('<h1> Home Page </h1>')

    
def draw(request):
    # return HttpResponse('<h2><font color="#ff0011">render the drawing page</font></h2>')

    return render(request,'drawing_board/draw.html',{'title': 'Drawing Board'})



def get_img3(request):
    if request.method == 'POST':
        # result = request.GET.get('id3')
        # result = request.GET['id2']
        # result = request.POST.get('id3')
        
        result = request.POST.get('imageDataField')
        
        print("\n\n1.asdasdasdasd wokring\n\n\n\n.............\n\n\n\n .........")
        # create a form instance and populate it with data from the request:
        # check whether it's valid:
        print('2. ','-'*50)
        print('3. ',result)
        # result_decoded = b64decode(result)
        # print('4. resulted decoded','-'*50)
        # print('5.',type(result_decoded))
        print('-'*50)
        # print(result_decoded)

        # img = readb64(result)
        # print(type(result))
        # print(img)
        print('-'*50)
        # print('decoding string')
        # data_url_pattern = re.compile('data:image/(png|jpeg);base64,(.*)$')
        # signature_data = data_url_pattern.match(result).group(2)
        # signature_data = bytes(signature_data, 'UTF-8')
        # signature_data = decodestring(signature_data)
        # print(signature_data)
        print('last\n\n','-'*50)
        
        # return HttpResponse('<h1>/thanks/<br> it is a post method form</h1> IMAGE i got : <img src="{}"/>'.format(result))
        # return HttpResponse('<h1>/thanks/<br> it is a post method form</h1> IMAGE i got : <img src="{}"/> <br>image : <br><br><br>{}'.format(result,signature_data))
        
        
        return render(request,'drawing_board/image.html',{'title': 'Drawing Board',
        'message':'/thanks/ it is a post method form\n\n\n\n IMAGE got : {}'.format(result),
        'image':result
        })

    # result = request.GET.get('q')
    else:
        result = request.GET.get('q')

    # return HttpResponse('<h2><font color="#ff0011">render the drawing page</font></h2>')
    # result = request.POST.get('q')
    # result = request.POST('id3')
    
    # format, imgstr = result.split(';base64,')
    # print("format", format)
    # ext = format.split('/')[-1]

    # data = ContentFile(base64.b64decode(imgstr))  
    # file_name = "'myphoto." + ext

    
    # with open("ppcd.png", 'rb') as fi:
    #     self.my_file = File(fi, name=os.path.basename(fi.name))
    #     self.save()
    print(result,'\n',type(result))
    return HttpResponse(str(result))
