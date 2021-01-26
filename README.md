# Destiny Scrims App
An app that uses Bungie OAuth API to log in and accesses your clan list to create randomly generated teams. The app is built using Django/Djongo with MongoDB and styled using Bootstrap framework.

## What it includes

* User, tournament, and team model/migration
* Settings for MongoDB
* Sessions to keep user logged in
* Templates

### User Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| _id | String | Auto-generated |
| member_id | Interger | Provided by Bungie OAuth |
| access_token | String | Provided by Bungie OAuth / required to access API |
| refresh_token | String | Provided by Bungie OAuth / refreshes access |
| expiry_date | Date | Provided by Bungie OAuth / when token needs to be refreshed |
| displayName | String | Provided by Bungie OAuth / Bungie Username |
| membershipId | Interger | Provided by Bungie OAuth / Bungie membership ID |
| membershipType | Interger | Provided by Bungie OAuth / Bungie membership type |
| groupId | Interger | Provided by Bungie OAuth / Destiny 2 clan ID |
| groupName | String | Provided by Bungie OAuth / Destiny 2 clan name |

### Tournament Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| _id | String | Auto-generated |
| id | Interger | Auto-generated |
| member_id | String | Must be provided |
| numTeams | Interger | Must be provided / number of teams |
| date_created | Date | Generated at create |
| teams | Model | Must be provided / uses Team model |

### Team Model

| Column Name | Data Type | Notes |
| --------------- | ------------- | ------------------------------ |
| player1 | String | Must be provided |
| player2 | String | Must be provided |
| player3 | String | Must be provided |

### User Stories

* As a user, you will be able to log in via Bungie OAuth API.
* As a user, you will be able to populate players from your clan for tournaments via Bungie API.
* As a user, you will be able to create randomly generated teams for tournaments.

### Technologies

* Python
* MongoDB
* HTML
* CSS


### Code Snippet

##### Callback to Retrieve Info after OAuth 
```py
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
    request.session['displayName'] = displayName
    return HttpResponseRedirect('/')
```


## Steps To Use

#### 1. Go to Repo on Github

Repo is found here: [destiny-scrims](https://github.com/Destiny-Scrims/backend). Alternatively, you can go to this website: [destiny-scrims-app]()
* Go to repo above
* `fork` and `clone`

#### 2. Create neccessary file

* create `keys.py` in `main_app` folder
* add the variables `client_id`, `client_secret`, and `API_KEY` with your corresponding Bungie API info to `keys.py`.
* add `DJANGO_SECRET = randomstring` to `keys.py`

#### 3. Migrate and runs erver to make sure it works

* in the terminal, type `py -m manage migrate` or MacOS equivalent to migrate required information
* type `py -m manage runserver` to start server
* in your browser, navigate to `htto://localhost:8000` to access the app

