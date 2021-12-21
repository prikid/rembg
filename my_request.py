from pathlib import Path
import requests

# endpoint = "http://164.90.175.236/api/removebg"
endpoint = "http://127.0.0.1:5000//api/removebg"

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
            headers={'X-Api-Key': 'S6qU5LA8cNpghQkZxorc6fDQLZw2wD4xAflWkCY9zzHvMmSlJiYKQ0JJQL2iq34d'}
        )
        if response.ok:
            out_img = output_folder.joinpath(img.with_suffix('.out.png').name)
            out_img.write_bytes(response.content)
        else:
            raise Exception(response.text)

    except Exception as e:
        print(e)

    break
