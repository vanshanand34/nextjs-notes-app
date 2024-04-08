import requests

#testing user logout by passing the token obtained during login/register
login_url = "http://127.0.0.1:8000/notesapp/logoutapi"
credentials = {"token": "9f8d24541592c0f07a6abbe1181e090fa0cebbba"}


response = requests.post(login_url, data=credentials)

# Check for successful logout
if response.status_code == 200:
    data = response.json()  # Assuming response is JSON
    print(f"Logout successful! Retrieved data: {data}")
else:
    print(f"Logout failed! Status code: {response.status_code}")
