from django.shortcuts import render

def home(request):
	return render(request, "fernandaApp/index.html")

def namorados(request):
	return render(request, "fernandaApp/namorados.html")