from django.shortcuts import render
from django.template import RequestContext
import json
from django.http import HttpResponse, JsonResponse, HttpRequest
import re

def task1(request: HttpRequest) -> HttpResponse:
	if request.method == 'POST':
		username = request.POST['login']
		length = len(username)
		print(username)
		t = length - 2
		if t < 0:
			match = re.fullmatch(r'([a-zA-Z]{1})', username)
		else:
			match = re.fullmatch(r'([a-zA-Z]{1})([a-zA-Z0-9-.]' + r'{' + str(t) + r'})([a-zA-Z0-9]{1})', username)
		if match and length >= 1 and length <= 20:
			return HttpResponse(json.dumps({"success": True, "message": "Допустимый логин"}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({"success": False, "message": "Неправильно"}), content_type="application/json")

	context = {}
	return render(request, 'check/index.html', context)


#Второй способ 
#Второй способ хуже так как обрабатывает дольше чем первый. В первом случае мы ищем фиксированное
#количество определенных символов, а во втором случае мы ищем все возможные варианты, главное чтобы,
#общий размер был указанной длины.
"""
def task1(request: HttpRequest) -> HttpResponse:
	if request.method == 'POST':
		username = request.POST['login']
		length = len(username)
		if length < 1 and length > 20:
			return HttpResponse(json.dumps({"success": False, "message": "Неправильно"}), content_type="application/json")
		print(username)
		match = re.fullmatch(r'([a-zA-Z]+[a-zA-Z0-9-.]*[a-zA-Z0-9]*)' + r'{' + str(length) + r'}', username)
		if match:
			return HttpResponse(json.dumps({"success": True, "message": "Допустимый логин"}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({"success": False, "message": "Неправильно"}), content_type="application/json")

	context = {}
	return render(request, 'check/index.html', context)"""