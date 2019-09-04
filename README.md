
steps to run the sample rest service on docker -


1. Move to the directory - cd python-rest-api-docker

2 Build the docker image - docker build -t python-rest .

3. Create and run a container - docker run -d -p 5000:5000 python-rest

4. Navigate to http://0.0.0.0:5000/ to get hello world'd

Note: If the image is built inside a private network, you can mention gateway to proxy through
      Ex: docker build --build-arg proxy=<hostname:port> -t python-rest .

A Sample Client --

import requests
r = requests.post('http://0.0.0.0:5000/v1/api',verify=False, json={"name": "naren"})
headers = {'Content-type': 'application/json'}
print(r.status_code)
if r.ok:
    print r.content
