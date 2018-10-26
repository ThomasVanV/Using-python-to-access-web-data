import json
import urllib.request, urllib.error

url = input("Enter URL: ")
hnd = urllib.request.urlopen(url).read()

print('Retrieving', url)
uh = urllib.request.urlopen(url)  # this opens the user's url
data = uh.read()  # read all of the characters in the url
print('Retrieved', len(data), 'characters')  # print the number of characters

sum = 0
total_count = 0

info = json.loads(hnd)
js_object = info['comments']


for item in js_object:
    num = item.get('count')
    sum = sum + num
    total_count = total_count + 1

print('Count: ', total_count)
print('Sum: ', sum)
