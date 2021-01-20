from django.utils.http import urlencode
from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render
from uuid import uuid4
import requests
from keys import client_id, client_secret, API_KEY

# Create your views here.

AUTH_URL = f'https://www.bungie.net/en/OAuth/Authorize?client_id={client_id}&response_type=code'

access_token_url = 'https://www.bungie.net/platform/app/oauth/token/'

code = ''


def get_token(code):
    HEADERS = {"X-API-Key": API_KEY}
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
        "X-API-Key": API_KEY,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": 'authorization_code'
        }
    post_data = f'grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}'
    response = requests.post(access_token_url, data=post_data, headers=HEADERS)

    print(f'here is your response:\n{response.status_code}')
    print(f'here is your response:\n{response.text}')
    print(f'here is your response:\n{response.json()}')

    return render(request, 'callback.html')


