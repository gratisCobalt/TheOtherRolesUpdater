import requests
import json
import zipfile
import os

# get latest version
response = requests.get("https://api.github.com/repos/Eisbison/TheOtherRoles/releases/latest").json()
y = json.dumps(response)
x = json.loads(y)
tag_name = x["tag_name"]

# download latest zip
url = "https://github.com/Eisbison/TheOtherRoles/releases/download/{0}/TheOtherRoles.zip".format(tag_name)
r = requests.get(url)

try:
    with open("TheOtherRoles.zip", 'wb') as f:
        print('downloading...')
        f.write(r.content)
except Exception:
    pass

# unzip
try:
    with zipfile.ZipFile("TheOtherRoles.zip", 'r') as zip_ref:
        print('extracting...')
        zip_ref.extractall("")
except Exception:
    pass

# delete zip
try:
    if os.path.exists("TheOtherRoles.zip"):
        print('removing ZIP...')
        os.remove("TheOtherRoles.zip")
except Exception:
    pass
