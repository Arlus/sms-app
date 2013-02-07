# Create your views here.
from test_app.models import Record
from django.http import HttpResponseRedirect, HttpResponse
import json
from django.shortcuts import render_to_response
import requests


def handle_sms(request):
    sender_no = request.GET.get('phone', '')
    message = request.GET.get('text', '')
    saves = Record(sender=sender_no, message=message)
    saves.save()
    # params = {"message": message, "sender": sender_no}
    # try:
    #   headers = {'content-type': 'application/json'}
    #   r = requests.post('http://127.0.0.1:8000/api/record/', data=json.dumps(params), headers=headers)
    #   return HttpResponse(r.text, status=r.status_code)
    # except requests.ConnectionError:
    #   return HttpResponse('ConnectionError', status=500)
    return render_to_response(index.html)
