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
from django.core import mail
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
        status = Status.objects.get(status=request.data['status'])
        report.status = status
        report.save()

        html_content = render_to_string('email_template.html', {"name":report.user.username,"status":request.data['status']})

        subject = f"Report {request.data['status']}"
        from_email = 'mykasihapp@gmail.com'
        to_email = report.user.email
        mail.send_mail(subject,subject, from_email, [to_email], html_message=html_content)

        
        return Response({"message":"success"})
    
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    permission_classes = [AllowAny]




    
