import requests
import api_scripts.database as database
import datetime

start_time = datetime.datetime.now()

# Define API endpoint and urls
base_url = "http://dummyapi.io/data/v1/"
users_url = f"{base_url}/user"
users_profile_url = f"{base_url}/user/{{}}"

# Define headers for API request
headers = {"app-id": "6401c57240b15c493ba72bea"}

batch_size = 50

# Send a request to the API to get the total number of users
response = requests.get(users_url, headers=headers)
total_users = response.json()["total"]
print(f"Total number of users: {total_users}")


# Calculate the number of page iterations required based on batch size
pages = (total_users + batch_size - 1) // batch_size
print(f"Number of pages: {pages}")

# Dict to store all males in case needed for future purposes
male_users = []

# Loop pages and extract user data and id
for page in range(pages):
    print(f"Page: {page}")
    params = {"limit": batch_size, "page": page}
    users_response = requests.get(users_url, headers=headers, params=params)
    users = users_response.json()["data"]

    for user in users:
        # Loop through each user and extract their profile
        user_profile_response = requests.get(
            f"{users_url}/{user['id']}", headers=headers
        )
        user_profile = user_profile_response.json()

        # Check if male
        if user_profile["gender"] == "male":
            user_info = {
                "first_name": user_profile["firstName"],
                "last_name": user_profile["lastName"],
                "gender": user_profile["gender"],
                "dob": datetime.datetime.fromisoformat(
                    user_profile["dateOfBirth"].replace(
                        "Z", "+00:00"
                    )  # convert from ISO format to mySQL compatible format
                ).strftime("%Y-%m-%d %H:%M:%S"),
                "name_char_count": len(user_profile["firstName"])
                + len(user_profile["lastName"]),
            }
            print(
                f"The name {user_info['first_name']} {user_info['last_name']} contains {user_info['name_char_count']} characters."
            )
            male_users.append(user_info)
            # Insert male user data into database
            database.insert_users(user_info)

print(f"Males in total: {len(male_users)}")

# Print execution time duration
end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
print(f"Script execution time: {elapsed_time}")
