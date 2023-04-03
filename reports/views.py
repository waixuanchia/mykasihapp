from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import JSONParser
from .models import Report,Status
from .serializer import ReportSerializer
from ministries.models import Ministries
from accounts.models import User
import json
import base64
from django.core.files.base import ContentFile
from PIL import Image
from drf_extra_fields.fields import Base64ImageField
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import os
from django.conf import settings


# Create your views here.

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [AllowAny]
    
    def create(self,request):
        
        print(request.user.id)
        id = request.user.id
        user = User.objects.get(id = id)
        contact = request.data['contact']
        description = request.data['description']
        ministry_id = request.data['option']
        ministry = Ministries.objects.get(id = ministry_id)
        image = request.data['image']
        decoded_image = base64.b64decode(image)
        
        image_field = Base64ImageField()
        image = image_field.to_internal_value(image)

        status = Status.objects.get(status="pending acceptance")
        report = Report.objects.create(user=user,ministry=ministry,description=description,status=status,image_url=image)
        
        report.save()





        #print(user)
        #print(request.data['contact'])
        
        #json_data = json.loads(request.body)['_parts']
        #name = json_data[0][1]
        #contact = json_data[1][1]
        #description = json_data[2][1]
        #ministry = json_data[3][1]
        #image = json_data[4][1]
        #ministry = Ministries.objects.get(id=ministry)
        #print(request.user)


        return Response({"message":"success"})
    
    def partial_update(self,request,pk):
        report = Report.objects.get(id = pk)
        status = Status.objects.get(status="accepted")
        report.status = status
        report.save()
        html_content = render_to_string('email_template.html', {"name":report.user.username})

        subject = 'Report Received'
        from_email = 'mykasihapp@gmail.com'
        to_email = report.user.email
        msg = EmailMultiAlternatives(subject, html_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        with open(os.path.join(settings.STATIC_ROOT, 'images', 'logo.png'), 'rb') as f:
            image_data = f.read()
        msg.attach('logo.png', image_data, 'image/png')

# Embed the image in the HTML content
        html_content = html_content.replace('<img src="logo.png">', '<img src="cid:logo.png">')
        msg.send()
        return Response({"message":"success"})



    
