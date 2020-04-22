import requests
def GetRedditStories():
   base_url = 'https://www.reddit.com/'
   data = {'grant_type': 'password', 'username': "Brettb888", 'password': "Brettb23"}
   auth = requests.auth.HTTPBasicAuth("QWYvE5GqiNXdsw", "-YMKQcT8GCHWTUWFzHsm931aCAo")
   r = requests.post(base_url + 'api/v1/access_token', data=data, headers={'user-agent': 'HW10 by Brettb888'},auth=auth)
   d = r.json()
   #print(d)
   token = 'bearer ' + d['access_token']
   base_url = 'https://oauth.reddit.com'
   headers = {'Authorization': token, 'User-Agent': 'HW10 by Brettb888'}
   response = requests.get(base_url + "/r/coronavirus/top.json",headers=headers)
   raw_data = response.json()['data']['children']
   #print(raw_data)
   store_titles =[]
   store_links =[]
   for i in range(len(raw_data)):
       title = raw_data[i]['data']['title']
       links = raw_data[i]['data']['permalink']
       store_titles.append(title)
       store_links.append(links) 
   return store_titles, store_links
def GetNewsAPI(topic):
   base_url = 'http://newsapi.org/'
   r = requests.get(base_url + f'v2/everything?q={topic}&from=2020-03-21&sortBy=publishedAt&apiKey=2050df7a6a014501a04c5f42fa6eef54')
   d = r.json()
   raw_data = d['articles']
   '''for element in raw_data:
       print(element['title'])'''
     return raw_data
GetNewsAPI("coronavirus obesity")
'''titles = GetRedditStories()
for element in titles[0]:
   #print(element)
   if "Asthma" in element:
       print(element)'''