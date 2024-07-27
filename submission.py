import requests
import json

# Create the JSON payload
my_data = {
    "github": "https://github.com/sreehari59/NxtGen_AcciVision",
    "email": "sreeharipradeepkumar1996@gmail.com",
    "url": "https://sree1996.pythonanywhere.com/apipredict",
    "notes": ""
}
# Set the headers
headers = {
    "Content-Type": "application/json"
}
# Posting to URL
url = "https://dps-challenge.netlify.app/.netlify/functions/api/challenge"
# POST request made
response = requests.post(url, headers=headers,
                          data=json.dumps(my_data))

# Check for successfull request
if response.status_code == 200:
    print("Congratulations! Achieved Mission 3")
else:
    print("Failed to complete Mission 3. Status code:", response.status_code)