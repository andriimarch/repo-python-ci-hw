import requests
from faker import Faker
fake = Faker()

valid_headers = {
    "Authorization": "pk_188648872_RAUMQD7FOHL5JHKE26AJOWM65XQAFH0M",
    "Content-Type": "application/json"
}

invalid_token_headers = {
"Authorization": "pk_18648872_RAUMQDwekjfwfkewhfwuiefhwef7FOHL5JHKE26AJOWM65XQAFH0M"
}


# Get Team ID from https://app.clickup.com/team with valid token
def getTeamIdValidToken():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=valid_headers)
    return teamIdRequest.json()['teams'][0]['id']


# Get Team ID from https://app.clickup.com/team with invalid token
def getTeamIdInValidToken():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=invalid_token_headers)
    return teamIdRequest


# Create space in  https://api.clickup.com/api/v2/team/{team_id}/space with valid token
def createSpace():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=valid_headers)
    teamIdIdentifier = teamIdRequest.json()['teams'][0]['id']
    randomSpaceName = fake.name()
    body = {
        "name": randomSpaceName
    }
    result = requests.post("https://api.clickup.com/api/v2/team/"+teamIdIdentifier+"/space", headers=valid_headers,json=body)
    return result


# Create space in  https://api.clickup.com/api/v2/team/{team_id}/space with valid token and invalid body params
def createSpaceInvalidBody():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=valid_headers)
    teamIdIdentifier = teamIdRequest.json()['teams'][0]['id']
    randomSpaceName = fake.name()
    body = {
        name: randomSpaceName
    }
    result = requests.post("https://api.clickup.com/api/v2/team/"+teamIdIdentifier+"/space", headers=valid_headers,json=body)
    return result

# Create space in  https://api.clickup.com/api/v2/team/{team_id}/space with valid params
def getSpace():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=valid_headers)
    teamIdIdentifier = teamIdRequest.json()['teams'][0]['id']
    spaceIdentifier = requests.get("https://api.clickup.com/api/v2/team/" + teamIdIdentifier + "/space", headers=valid_headers)
    result = spaceIdentifier.json()
    return result


# Update space name in  https://api.clickup.com/api/v2/space/{space_id} with valid params
def updateSpace():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=valid_headers)
    teamIdIdentifier = teamIdRequest.json()['teams'][0]['id']
    spaceRequest = requests.get("https://api.clickup.com/api/v2/team/" + teamIdIdentifier + "/space",
                                headers=valid_headers)
    spaceName = spaceRequest.json()['spaces'][0]['name']
    spaceIdValue = spaceRequest.json()['spaces'][0]['id']

    randomNameForUpdate = fake.name()
    body_updated = {
        "name": "Updated from " + spaceName + " to " + randomNameForUpdate
    }
    result = requests.put("https://api.clickup.com/api/v2/space/" + spaceIdValue, json=body_updated,
                          headers=valid_headers)
    return result

# Delete space name in  https://api.clickup.com/api/v2/space/{space_id} with valid params
def removeSpace():
    teamIdRequest = requests.get("https://api.clickup.com/api/v2/team", headers=valid_headers)
    teamIdIdentifier = teamIdRequest.json()['teams'][0]['id']
    spaceRequest = requests.get("https://api.clickup.com/api/v2/team/" + teamIdIdentifier + "/space",
                                   headers=valid_headers)
    spaceIdValue = spaceRequest.json()['spaces'][0]['id']
    result = requests.delete("https://api.clickup.com/api/v2/space/" + spaceIdValue,headers=valid_headers)
    return result













