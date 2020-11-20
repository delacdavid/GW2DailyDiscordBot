import requests
import json
from tools import tools

class gw2api:
    def doRequest(self,path):
        r = requests.get(f"https://api.guildwars2.com{path}")
        return r.json()

    def getAchievementDetails(self,idList):
        ids = ",".join([str(id) for id in idList])
        data = self.doRequest(f"/v2/achievements?ids={ids}")
        #print(f"/v2/achievements?ids={ids}")
        desc = [e['name'] for e in data]
        #print(len(desc))
        return dict(zip(idList,desc))

    def getDailyAchievements(self,tomorrowf=False):
        tomorrow = ""
        if tomorrowf:
            tomorrow = "/tomorrow"

        data = self.doRequest(f"/v2/achievements/daily{tomorrow}")

        pve = list(dict.fromkeys([e['id'] for e in data['pve']]))
        pvp = list(dict.fromkeys([e['id'] for e in data['pvp']]))
        wvw = list(dict.fromkeys([e['id'] for e in data['wvw']]))
        fractals = list(dict.fromkeys([e['id'] for e in data['fractals']]))
        ids = pve + pvp + wvw + fractals
        data = self.getAchievementDetails(ids)

        pveList = [data[e] for e in pve]
        pvpList = [data[e] for e in pvp]
        wvwList = [data[e] for e in wvw]
        fractalsList = [data[e] for e in fractals]
    
        dailyFractalsList, recommendedFractalsList = t.splitFractals(fractalsList)

        return pveList, pvpList, wvwList, dailyFractalsList, recommendedFractalsList
        #return [],[],[],[],[]

api = gw2api()
t = tools()
#test1, test2, test3, test4, test5 = api.getDailyAchievements()


#print(r.status_code)
#print(r.headers['content-type'])
#print(r.text)
#print(r.json())