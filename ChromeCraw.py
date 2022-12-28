from bs4 import BeautifulSoup
from selenium import webdriver
import requests as req
import pandas as pd
import re, time

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}
session = req.Session()

'''
# 함수 내 입력 전 해당 태그가 잘 긁어와지는지 확인하기 위한 간이 크롤링
tmpUrl = '크롤링 사이트'
re = session.get(tmpUrl, headers = headers)
bs = BeautifulSoup(re.text, 'html.parser')
test = bs.select('구역별로 가져오면 좋을 태그.클래스이름')

print(test)
'''
def result(result, fileName):
	df_w = pd.DataFrame(result)
	df_w.to_excel(excel_writer=f"전체내역({fileName}).xlsx", sheet_name = f'전체내역', index = False, engine='xlsxwriter')

def show(orgUrl, pageNum): 
    result = []
    resultTmp = {}
    for i in range(1, pageNum):
        tmpUrl  = orgUrl+str(i)
        re      = session.get(tmpUrl, headers = headers)
        bs      = BeautifulSoup(re.text, 'html.parser')
        tmpData = bs.select('구역별로 가져오면 좋을 태그.클래스이름')

        for j in tmpData:
            title   = j.select_one('태그이름')
            link    = j.find('a', class_="클래스이름")["href"]
            year    = j.select_one('태그.클래스이름')
            
            title   = title.get_text() if title is not None else "None"
            link    = link if link is not None else "None"
            year    = year.get_text() if year is not None else "None"
            
            resultTmp = {
                "제목": title,
                "링크": link, 
                "날짜":year,
            }
            print(resultTmp)
            result.append(resultTmp)
    return result

if __name__ == "__main__":	
	orgUrl = ['크롤링 대상 사이트']
  # 사이트 넘길 페이지 수
	pageNum = [17, 5, 19, 23] 
  # 엑셀로 저장할 파일 이름
	fileName = ['예능', '시사', '미드', 'OTT']
    
	for i in range(0, len(orgUrl)):
		data = show(orgUrl[i], pageNum[i])
		result(data, fileName[i])
