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
with open("TheOtherRoles.zip", 'wb') as f:
    f.write(r.content)

# unzip
with zipfile.ZipFile("TheOtherRoles.zip", 'r') as zip_ref:
    zip_ref.extractall("")

# delete zip
if os.path.exists("TheOtherRoles.zip"):
    os.remove("TheOtherRoles.zip")
