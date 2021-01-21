from django.utils.http import urlencode
from django.http import HttpResponseRedirect, HttpRequest, JsonResponse
from django.shortcuts import render
from django.contrib import sessions
from uuid import uuid4
import requests
import datetime
from keys import client_id, client_secret, API_KEY

# Create your views here.

AUTH_URL = f'https://www.bungie.net/en/OAuth/Authorize?client_id={client_id}&response_type=code'

access_token_url = 'https://www.bungie.net/platform/app/oauth/token/'

code = ''




def get_token(code):
    HEADERS = {"X-API-Key": API_KEY}
    post_data = {'code': code}
    response = requests.post(access_token_url, json=post_data, headers=HEADERS)

def save_session(token):
    oauth_session = requests.Session()
    oauth_session.headers["X-API-Key"] = API_KEY
    oauth_session.headers["Authorization"] = 'Bearer ' + token
    access_token = "Bearer " + token

def index(request):
    url = AUTH_URL # + urlencode(state_params)
    return render(request, 'index.html', { 'url': url })

def callback(request):
    print(f"Info I want\n---------------------\n{request.GET.get('code')}")

    code = request.GET.get('code')
    print(f'here is your code: {code}')

    access_token = ''

    HEADERS = {
        "Content-Type": 'application/x-www-form-urlencoded',
        "X-API-Key": API_KEY,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": 'authorization_code',
        "Authorization": access_token
        }
    post_data = f'grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}'
    response = requests.post(access_token_url, data=post_data, headers=HEADERS)

    print(f'here is your response:\n{response.status_code}')
    print(f'here is your response:\n{response.text}')
    print(f'here is your response:\n{response.json()}')
    print(type(response.json()))
    access_token = response.json()['access_token']
    expires_in = response.json()['expires_in']
    refresh_token = response.json()['refresh_token']
    membership_id = response.json()['membership_id']
    print(f'this is your access token: {access_token}')
    print(f'access token expires in: {expires_in}')
    print(f'this is your refresh token: {refresh_token}')
    print(f'this is your membership id: {membership_id}')
    a = datetime.datetime.now()
    expiry_date = a + datetime.timedelta(0, expires_in)
    print(f'your access token will expire at this time: {expiry_date}')
    save_session(access_token)
    res = session.get('https://www.bungie.net/Platform/User/GetBungieNetUser/')
    print(f'this is your bungie user: {res.text}')

    return render(request, 'callback.html')


