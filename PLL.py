import requests
import twitter
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.premierlacrosseleague.com/',
    'content-type': 'application/json',
    'Origin': 'https://stats.premierlacrosseleague.com',
    'Connection': 'keep-alive',
    'TE': 'Trailers',

 }


data = '{"operationName":null,"variables":{"sortBy":"points","season":2021,"statType":"regular","limit":5},"query":"\\nquery($sortBy: StatFieldName, $season: Int, $statType: StatType!, $limit: Int, $league: String) {\\n allPlayers(sortBy:$sortBy, season: $season, statType:$statType, limit: $limit, league: $league) {\\n\\t\\tofficialId\\n firstName\\n lastName\\n profileUrl\\n position\\n slug\\n allTeams {\\n officialId\\n league\\n position\\n positionName\\n jerseyNum\\n year\\n fullName\\n }\\n stats {\\n points\\n onePointGoals\\n twoPointGoals\\n assists\\n shotPct\\n faceoffPct\\n savePct\\n groundBalls\\n causedTurnovers\\n }\\n }\\n}\\n"}'

response = requests.post('https://api.stats.premierlacrosseleague.com/graphql', headers=headers, data=data)

fname = []
lname = []
points = []
entry = 0
Message = ""
data1 = json.loads(response.text)

for x in data1["data"]["allPlayers"]:
    fname.append(x["firstName"])
    lname.append(x["lastName"])
    points.append(x["stats"]["points"])

while entry < 5:
    Message+=(fname[entry] + " " + lname[entry] + ": " + str(points[entry])+ "\n")
    entry = entry + 1


print(Message)

api = twitter.Api(consumer_key='aabsydBZEGwnLmsMOeoALsfXm',consumer_secret='okBsYcmxI8H0uzuOvwGtx80QeRlXbVFzr9zHS0kibEmYBhPwsU', access_token_key='1417094768635510788-Q3lAsfeiChU5tQQRZLkie69HoEJ0dI',access_token_secret='OjRLMM6zrbeKDpcJeOfjGLXYndvYYj9dWvSE0HHRYXTHo')

api.PostUpdate(Message)
