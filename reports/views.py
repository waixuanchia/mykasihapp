from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import JSONParser
from .models import Report,Status
from .serializer import ReportSerializer,StatusSerializer
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
    permission_classes = []
    
    def create(self,request):
        
        id = request.user.id
        print(request.user)
        user = User.objects.get(id = id)

        image_url = request.data['image_url']
        description = request.data['description']
        ministry_id = request.data['ministry']

        ministry = Ministries.objects.get(id = ministry_id)
        status = Status.objects.get(status="pending acceptance")
        report = Report.objects.create(user=user,image_url=image_url,description=description,ministry=ministry,status=status)
        report.save()

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
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [AllowAny]




    
