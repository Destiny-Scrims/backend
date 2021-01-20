from django.utils.http import urlencode
from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render
from uuid import uuid4
import requests

# Create your views here.

AUTH_URL = 'https://www.bungie.net/en/OAuth/Authorize?client_id=35285&response_type=code'

access_token_url = 'https://www.bungie.net/platform/app/oauth/token/'

code = ''
client_id = '35285'
client_secret = 'LxlxbBrykmSGzq23sECKTFYew7W2.c.0TAa.frP9x4U'

def get_token(code):
    HEADERS = {"X-API-Key":'4edfaa1b570745588f516307bdc40e43'}
    post_data = {'code': code}
    response = requests.post(access_token_url, json=post_data, headers=HEADERS)

def index(request):
    url = AUTH_URL # + urlencode(state_params)
    return render(request, 'index.html', { 'url': url })

def callback(request):
    print(f"Info I want\n---------------------\n{request.GET.get('code')}")

    code = request.GET.get('code')
    print(f'here is your code: {code}')

    HEADERS = {
        "Content-Type": 'application/x-www-form-urlencoded',
        "X-API-Key":'4edfaa1b570745588f516307bdc40e43',
        "client_id": '35285',
        "client_secret": 'LxlxbBrykmSGzq23sECKTFYew7W2.c.0TAa.frP9x4U',
        "grant_type": 'authorization_code'
        }
    post_data = f'grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}'
    response = requests.post(access_token_url, data=post_data, headers=HEADERS)

    print(f'here is your response:\n{response.status_code}')
    print(f'here is your response:\n{response.text}')
    print(f'here is your response:\n{response.json()}')

    return render(request, 'callback.html')


