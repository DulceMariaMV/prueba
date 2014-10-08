#encoding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
# Create your views here.
def inicio_view(request):
	return render_to_response("inicio.html",{},RequestContext(request))
def registro_view(request):
	return render_to_response("registro.html",{},RequestContext(request))