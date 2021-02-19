'''
1. 폴더구조
Filecpature
┕File : 캡처할 대상의 파일이 있는 폴더
┕Picture : 캡처 저장 폴더
┕소스코드

2. im=ImageGrab.grab(bbox=(좌표))
- 좌표 : pyautogui.position() 통해서 캡쳐 범위의 왼쪽위, 오른쪽 아래 좌표 출력

3. title_name = dict
- {1:"hihi", 2:"hello"}
- 엑셀 파일에 대상 이름을 정리해놓았으면 별도의 함수를 통해 이름 가져오기

4. title_num = len(title_name)
'''

for i in range(title_num):
    if os.path.exists(f".\\File\\{title_name[i+1]}"):
        if '.zip' in title_name[i+1] or '.rar' in title_name[i+1]:
            # 띄어쓰기 문자열이 있을 수 있으니 "test"를 위해 \"\" 
            p = subprocess.Popen('bandizip.exe \".\\File\\%s\"' %(title_name[i+1]))
            #p = subprocess.Popen(f'bandizip.exe \"E:\\CaptureTest\\ZipFile\\{title_name[i+1]}\"')
            time.sleep(0.5)
            # 키보드 조정
            pyautogui.press('down')
            time.sleep(1)
            # 좌표 설정 하기
            im = ImageGrab.grab(bbox=(686, 283, 1791, 1015))
            # Pic 폴더 만든 다음에 하기
            im.save(f'.\\Picture\\{i+1}.{title_name[i+1]}.png')
            time.sleep(0.5)
            p.kill()

        if '.txt' in title_name[i+1]:
            p = subprocess.Popen('notepad.exe \".\\File\\%s\"' %(title_name[i+1]))
            #p = subprocess.Popen(f'notepad.exe \".\\ZipFile\\{title_name[i+1]}\"')

            time.sleep(1)
            # 좌표 설정 하기
            im = ImageGrab.grab(bbox=(686, 283, 1791, 1015))
            # Pic 폴더 만든 다음에 하기
            im.save(f'.\\Picture\\{i+1}.{title_name[i+1]}.png')
            time.sleep(0.5)
            p.kill()

        if '.mp4' in title_name[i+1] or '.mkv' in title_name[i+1]:
            print(title_name[i+1])
            p = subprocess.Popen('explorer \".\\File\\%s\"' %(title_name[i+1]))
            #p = subprocess.Popen(f'bandizip.exe \".\\ZipFile\\{title_name[i+1]}\"')
            # 동영상 넘기기위해 8번 정도 클릭해야 오프닝 생략 -> 동영상 내 설정에서 오른쪽 한 번에 150초로 설정
            time.sleep(3)
            pyautogui.press('right')
            time.sleep(2)
            # 좌표 설정 하기
            im = ImageGrab.grab(bbox=(686, 283, 1791, 1015))
            # Pic 폴더 만든 다음에 하기
            im.save(f'.\\Picture\\{i+1}.{title_name[i+1]}.png')
            time.sleep(0.5)
            os.system('taskkill /f /im PotPlayer64.exe')            

        if '.docx' in title_name[i+1]:
            p = subprocess.Popen('explorer \".\\File\\%s\"' %(title_name[i+1]))
            #p = subprocess.Popen(f'bandizip.exe \".\\ZipFile\\{title_name[i+1]}\"')
            time.sleep(2)
            # 좌표 설정 하기
            im = ImageGrab.grab(bbox=(686, 283, 1791, 1015))
            # Pic 폴더 만든 다음에 하기
            im.save(f'.\\Picture\\{i+1}.{title_name[i+1]}.png')
            time.sleep(0.5)
            os.system('taskkill /f /im WINWORD.EXE')  
    else:
        document.add_heading(f"{str(i+1)}.{title_name[i+1]}", 1)

document.save('.\\exception.docx')
