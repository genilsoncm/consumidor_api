
import requests
import re


url = 'https://jsonplaceholder.typicode.com/comments'

response = requests.get(url)

response_json = response.json()


for list_email in response_json:
    regex_tld = (re.findall(r'[\w\.-]+@[\w\.-]+\.org', list_email['email']))
    if len(regex_tld) != 0:
        print(regex_tld) 



