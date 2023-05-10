from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.parsers import JSONParser
from .models import Report,Status
from .serializer import ReportSerializer,StatusSerializer
from ministries.models import Ministries
from accounts.models import User
from django.core.files.base import ContentFile
from PIL import Image
from drf_extra_fields.fields import Base64ImageField
from django.template.loader import render_to_string
from django.core import mail
from django.conf import settings



# Create your views here.

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [AllowAny]

    def list(self,request):
        user = request.user
        param = request.query_params["status"]
        reports = Report.objects.filter(status__status=param,user=user)
        serialized_data = self.get_serializer(instance=reports,many=True)
        return Response(serialized_data.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        
        id = request.user.id
        print(request.user)
        user = User.objects.get(id = id)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            ministry_id = request.data['ministry']
            ministry = Ministries.objects.get(id=ministry_id)
            report_status = Status.objects.get(status="pending acceptance")
            report = Report.objects.create(user=user,
                                           description=serializer.validated_data['description'],
                                           image_url=serializer.validated_data['image_url'],
                                           ministry=ministry,
                                           status=report_status)
            report.save()
            return Response({"message":"report created successfully"},status=status.HTTP_201_CREATED)
            
        else:
            return Response({"message":"error while creating report"},status=status.HTTP_400_BAD_REQUEST)
        
    
    def partial_update(self,request,pk):
        print(request.user.groups)
        report = Report.objects.get(id = pk)
        StatusSerializer(data=request.data)
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




    
