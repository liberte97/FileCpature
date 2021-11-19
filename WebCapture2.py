'''
조건 및 고려사항
1. 팝업창이 뜨는 경우
2. URL 구조인 경우
3. URL1, URL2를 구분지어 캡처
'''

import pandas as pd
from selenium import webdriver
import time, pyautogui
import pandas as pd
from selenium.webdriver.common.alert import Alert
from PIL import ImageGrab


def WebCrawMain(title_site, title_site2, title_idx):
	wd = webdriver.Chrome(executable_path="chromedriver.exe")
	alt = Alert(wd)
	wd.implicitly_wait(3)
	wd.set_window_position(50,50)
	wd.set_window_size(1100, 1000)
	err, errL = {}, {}
	cnt = 0
	for i in range(len(title_idx)):
		if title_site[i][0:4] == "http" and title_site2[i][0:4] == "http":
			time.sleep(2)
			try:
				wd.get(title_site[i])
				print(title_site[i])
				time.sleep(7)
				im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
				#driver.save_screenshot(f'.\\Capture2\\Capture{i+1}.png')
				im.save(f'.\\Capture\\{i+1}.{title_idx[i]}-1.png')
				wd.get(title_site2[i])
				time.sleep(7)
				im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
				im.save(f'.\\Capture\\{i+1}.{title_idx[i]}-2.png')
			except Exception as e:
				time.sleep(2)
				pyautogui.press("enter")
				im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
				#driver.save_screenshot(f'.\\Capture2\\Capture{i+1}.png')
				im.save(f'.\\Capture\\{i+1}.{title_idx[i]}.png')
				continue

		elif title_site[i][0:4] == "http" or title_site2[i][0:4] == "http":
			if title_site[i][0:4] == "http":
				URL = title_site[i]
			else:
				URL = title_site2[i]
			try:
				time.sleep(2)
				wd.get(URL)
				print(URL)
				time.sleep(7)
				im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
				#driver.save_screenshot(f'.\\Capture2\\Capture{i+1}.png')
				im.save(f'.\\Capture\\{i+1}.{title_idx[i]}.png')
			except Exception as e:
				time.sleep(2)
				pyautogui.press("enter")
				im = ImageGrab.grab(bbox=(60, 50, 1140, 1040))
				#driver.save_screenshot(f'.\\Capture2\\Capture{i+1}.png')
				im.save(f'.\\Capture\\{i+1}.{title_idx[i]}.png')
				continue

		else:
			err[title_idx[i]] = title_site[i]
			errL[cnt] = title_idx[i]
			cnt = cnt +1

	wd.quit()
	return err, errL

def capture_title(path):
	# 엑셀 읽은 다음 전체 길이 및 이름 return
	data = pd.read_excel(path, engine="openpyxl")
	title_site, title_idx, title_site2 = {}, {}, {}
	title_num  = len(data.index)
	print(data.columns)
	for i in range(title_num):
		title_site[i] = str(data.URL[i])
		title_site2[i] = str(data.URL2[i])
		title_idx[i] = data.idx[i]
	return title_site, title_site2, title_idx

if __name__ == "__main__":
	path = '.\\Capture.xlsx'
	title_site, title_site2, title_idx  = capture_title(path)
	print(title_site)
	err, errL = WebCrawMain(title_site, title_site2, title_idx)
	with open("NotURL.txt", "w") as file_w:
		for i in errL:
			idx = errL[i]
			file_w.write(f"{idx}\t{err[idx]}\n")
      
      
'''
엑셀구조

idx    title    URL1    URL2

'''
