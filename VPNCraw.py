'''
Author: HH Nam
Dec: selenium 을 크롬으로 실행 시 VPN 설정 코드
'''

from bs4 import BeautifulSoup
from selenium import webdriver
import requests as req
import pandas as pd
import re, time

op = webdriver.ChromeOptions()
op.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
op.add_extension('bihmplhobchoageeokmgbdihknkjbknd.crx')
wd = webdriver.Chrome('chromedriver')

#캡챠 방지 프로그램 수동입력하기 위해 대표 게시물 하나 접속
wd.get('사이트명')
time.sleep(1)

def Result(result):
	df_w = pd.DataFrame(result)
	df_w.to_excel(excel_writer="저장파일이름.xlsx", sheet_name = f'전체내역', index = False, engine='xlsxwriter')

def WebCrawMain2(dataL): 
	result = []
	for i in dataL:
		wd.get(i)
		time.sleep(2)
		html = wd.page_source
		soup = BeautifulSoup(html, 'html.parser')
		data = soup.select('ul.list-body > li.list-item')
		try:
			title = data[0].select_one('div.wr-subject').get_text()
			chap  = data[0].select_one('div.wr-num').get_text()
			dateValue  = data[0].select_one('div.wr-date').get_text()
		except:
			title = 0
			chap = 0
			dateValue = 0

		dataDict={
			'페이지URL':i,
			'제목': title,
			'회차': chap,
			'날짜': dateValue
		}
		print(dataDict)
		result.append(dataDict)
	return result

if __name__ == "__main__":	
	dataL= [] #사이트 주소
	Data = WebCrawMain2(dataL)
	Result(Data)
