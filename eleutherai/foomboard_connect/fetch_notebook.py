import sys, requests

notebook_url = sys.argv[1]
save_path = sys.argv[2]

resp = requests.get(notebook_url)
resp.raise_for_status()

with open(save_path, 'w') as f:
    f.write(resp.text)
