from django.utils.http import urlencode
from django.http import HttpResponseRedirect, HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from django.contrib import sessions
from uuid import uuid4
import pprint
import requests
import datetime
from keys import client_id, client_secret, API_KEY
from .models import User

pp = pprint.PrettyPrinter(indent=4)


# Create your views here.

AUTH_URL = f'https://www.bungie.net/en/OAuth/Authorize?client_id={client_id}&response_type=code'

access_token_url = 'https://www.bungie.net/platform/app/oauth/token/'

code = ''

def index(request):
    return render(request, 'index.html', { 'url': AUTH_URL })

def auth(request):
    return HttpResponseRedirect(AUTH_URL)

def callback(request):
    code = request.GET.get('code')

    HEADERS = {
        "Content-Type": 'application/x-www-form-urlencoded',
        "X-API-Key": API_KEY,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": 'authorization_code',
        }
    post_data = f'grant_type=authorization_code&code={code}&client_id={client_id}&client_secret={client_secret}'
    response = requests.post(access_token_url, data=post_data, headers=HEADERS)

    access_token = response.json()['access_token']
    expires_in = response.json()['expires_in']
    refresh_token = response.json()['refresh_token']
    membership_id = response.json()['membership_id']
    a = datetime.datetime.now()
    expiry_date = a + datetime.timedelta(0, expires_in)

    HEADERS['Authorization'] = 'Bearer ' + access_token

    res = requests.get('https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser//', headers=HEADERS)

    displayName = res.json()['Response']['bungieNetUser']['displayName']
    membershipId = res.json()['Response']['destinyMemberships'][0]['membershipId']
    membershipType = res.json()['Response']['destinyMemberships'][0]['membershipType']

    info = requests.get(f'https://www.bungie.net/Platform/GroupV2/User/{membershipType}/{membershipId}/0/1/', headers=HEADERS)

    groupId = info.json()['Response']['results'][0]['group']['groupId']
    groupName = info.json()['Response']['results'][0]['group']['name']

    # member_list = requests.get('https://www.bungie.net/Platform/GroupV2/3697591/Members/', headers=HEADERS)

    # pp.pprint(member_list.json())

    print(expiry_date)

    User.objects.get_or_create(
        member_id = membership_id,
        defaults = {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'expiry_date': expiry_date,
            'displayName': displayName,
            'membershipId': membershipId,
            'membershipType': membershipType,
            'groupId': groupId,
            'groupName': groupName
        }
    )   
    request.session['member_id'] = membership_id
    return HttpResponseRedirect('/')

def access_session(request):
    if request.session.get('member_id'):
        return HttpResponse(request.session.get('member_id'))


