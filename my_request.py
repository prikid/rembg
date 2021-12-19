import requests

# TODO test https
endpoint = "http://164.90.175.236:5000/api/removebg"


response = requests.post(
    endpoint,
    files={'file': open('examples/animal-1.jpg', 'rb')},
    headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},
)
if response.status_code == requests.codes.ok:
    with open('no-bg.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)
