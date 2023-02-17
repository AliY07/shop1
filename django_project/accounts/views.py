from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def first_page(request):
    return  HttpResponse(request,"shop/first_page.html")

#API
@api_view(['GET'])
def getFood(request):
    return Response()






