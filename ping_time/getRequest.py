import urllib.request
response = urllib.request.urlopen("http://google.com").read()

print(response)