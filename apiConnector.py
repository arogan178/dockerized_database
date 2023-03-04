import requests

# Define API endpoint and urls
base_url = 'http://dummyapi.io/data/v1/'
users_url = f"{base_url}/user"
users_profile_url = f"{base_url}/user/{{}}"

headers = {'app-id': '##################'}

# Params
params = {'limit': 30}

# This will store all male users from request
male_users = []

response = requests.get(users_url, headers=headers, params={"limit": 0})
total_users = response.json()["total"]

for i in range(0, total_users, params["limit"]):
    params["offset"] = i
    response = requests.get(users_url, headers=headers, params=params)
    users_data = response.json()["data"]

    # Retrieve the full user profile for each user in the batch
    for user in users_data:
        user_details_response = requests.get(users_profile_url.format(user['id']), headers=headers)
        user_details = user_details_response.json()

        # Check if the user is male
        if user_details['gender'] == 'male':
            user_info = {
                'first_name': user_details['firstName'],
                'last_name': user_details['lastName'],
                'dob': user_details['dateOfBirth'],
                'gender': user_details['gender'],
                'name_character_count': len(user_details['firstName']) + len(user_details['lastName'])
            }

            male_users.append(user_info)

print(male_users)
print(len(male_users))
