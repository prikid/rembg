from pathlib import Path

import requests

# TODO test https
endpoint = "http://164.90.175.236:5000/api/removebg"

input_folder = Path('examples')
output_folder = Path('output')

output_folder.mkdir(exist_ok=True, parents=True)

for img in input_folder.glob('*.jpg'):
    if 'out' in img.name:
        continue

    print(f'Processing image f{img}...')

    try:
        response = requests.post(
            endpoint,
            files={'file': img.open('rb')},
            # headers={'X-Api-Key': 'INSERT_YOUR_API_KEY_HERE'},
        )
        if response.ok:
            out_img = output_folder.joinpath(img.with_suffix('.out.png').name)
            out_img.write_bytes(response.content)
        else:
            raise Exception(response.status_code, response.text)

    except Exception as e:
        print(e)
