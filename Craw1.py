import requests,time
from bs4 import BeautifulSoup
import pandas as pd

def get_webtoon(SiteName, TitleName):
	with open('Data3List.xlsx', 'w+') as file_w:
		for i in range(len(SiteName)):
			response = requests.get(SiteName[i])
			if response.status_code == 200:
				html = response.text
				soup = BeautifulSoup(html, 'html.parser')
        # 해당 웹툰 사이트의 span.bt_data에 해당하는 정보값을 가져옴
				title = soup.select('span.bt_data')
        # 정보가 2이하일 경우는 각 값이 1개씩 있지만 그 이상이면 여러개 있으므로 경우를 나눔
				if len(title) > 3:
					title = title[1]
				else:
					title = title[0]
				print(title.get_text())
				webList = { 'title' : f"{TitleName[i]}",
							'AllCount'  : f"{title.get_text()}",
							'site'  : f"{SiteName[i]}"}
				file_w.writelines(f"{webList['title']}\t{webList['AllCount']}\t{webList['site']}\n")
			else : 
				print(response.status_code)

def get_title(path):
	# 엑셀 읽은 다음 전체 길이 및 이름 return
	data = pd.read_excel(path, engine="openpyxl")
	SiteName, TitleName = {}, {}
	title_num  = len(data.index)
	print(data.columns)
	for i in range(title_num):
		SiteName[i] = data.site[i]
		TitleName[i] = data.title[i]

	return SiteName, TitleName

if __name__ == "__main__":
	path = '.\\Data1.xlsx'
	SiteName, TitleName = get_title(path)
	get_webtoon(SiteName, TitleName)
