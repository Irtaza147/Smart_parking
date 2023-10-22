import sys
from django.http import HttpResponse,HttpResponseRedirect
from subprocess import run,PIPE
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout
from django.urls import reverse_lazy

from django.http import JsonResponse
def plate(request):
    inp=request.POST.get('param')

    out = run(sys.executable, ["C:\\Users\\aliir\\Downloads\\Django Car Parking\\Django_Car_Parking\\eagle\\plate_processing.py"], inp, shell=False, stdout=PIPE)
    print(out)
    return render(request,'upload.html',{'datal',out})