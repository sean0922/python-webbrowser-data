#抓取網路公開資料並解析出來存成txt檔
import urllib.request as request
import json
#串接擷取公開資料
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"#資料為json的格式
with request.urlopen(src) as reponse:
    data=json.load(reponse)
#取得公司名稱列出來
clist=data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:#若沒有此檔案會直接創建
    for company in clist:
        file.write(company["公司名稱"]+"\n")
