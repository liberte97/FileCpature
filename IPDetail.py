
# -*- conding: utf-8 -*-
import socket
import urllib.request, json
import pandas as pd
Country = {"GH":"가나","GA":"가봉","GY":"가이아나","GM":"감비아","GP":"프랑스","GT":"과테말라","GU":"미국",
		   "GD":"그레나다","GE":"그루지야","GR":"그리스","GL":"덴마크","GW":"기니비소","GN":"기니","NA":"나미비아",
		   "NG":"나이지리아","ZA":"남아프리카공화국","NL":"네덜란드","AN":"네덜란드","NP":"네팔","NO":"노르웨이","NF":"오스트레일리아",
		   "NZ":"뉴질랜드","NC":"프랑스","NE":"니제르","NI":"니카라과","TW":"타이완","DK":"덴마크","DM":"도미니카연방","DO":"도미니카공화국",
		   "DE":"독일","LA":"라오스","LV":"라트비아","RU":"러시아","LB":"레바논","LS":"레소토","RO":"루마니아","RW":"르완다","LU":"룩셈부르크",
		   "LR":"라이베리아","LY":"리비아","RE":"프랑스","LT":"리투아니아","LI":"리첸쉬테인","MG":"마다가스카르","MH":"미국","FM":"미크로네시아",
		   "MK":"마케도니아","MW":"말라위","MY":"말레이지아","ML":"말리","MT":"몰타","MQ":"프랑스","MX":"멕시코","MC":"모나코","MA":"모로코",
		   "MU":"모리셔스","MR":"모리타니","MZ":"모잠비크","MS":"영국","MD":"몰도바","MV":"몰디브","MN":"몽고","US":"미국","VI":"미국",
		   "AS":"미국","MM":"미얀마","VU":"바누아투","BH":"바레인","BB":"바베이도스","BS":"바하마","BD":"방글라데시","BY":"벨라루스",
		   "BM":"영국","VE":"베네수엘라","BJ":"베넹","VN":"베트남","BE":"벨기에","BZ":"벨리세","BA":"보스니아헤르체코비나","BW":"보츠와나",
		   "BO":"볼리비아","BF":"부르키나파소","BT":"부탄","MP":"미국","BG":"불가리아","BR":"브라질","BN":"브루네이","BI":"브룬디",
		   "WS":"미국","SA":"사우디아라비아","CY":"사이프러스","SM":"산마리노","SN":"세네갈","SC":"세이셸","LC":"세인트루시아",
		   "VC":"세인트빈센트그레나딘","KN":"세인트키츠네비스","SB":"솔로몬아일란드","SR":"수리남","LK":"스리랑카","SZ":"스와질랜드",
		   "SE":"스웨덴","CH":"스위스","ES":"스페인","SK":"슬로바키아","SI":"슬로베니아","SL":"시에라리온","SG":"싱가포르",
		   "AE":"아랍에미레이트연합국","AW":"네덜란드","AM":"아르메니아","AR":"아르헨티나","IS":"아이슬란드","HT":"아이티",
		   "IE":"아일란드","AZ":"아제르바이잔","AF":"아프가니스탄","AI":"영국","AD":"안도라","AG":"앤티과바부다","AL":"알바니아",
		   "DZ":"알제리","AO":"앙골라","ER":"에리트리아","EE":"에스토니아","EC":"에콰도르","SV":"엘살바도르","GB":"영국","VG":"영국",
		   "YE":"예멘","OM":"오만","AU":"오스트레일리아","AT":"오스트리아","HN":"온두라스","JO":"요르단","UG":"우간다","UY":"우루과이",
		   "UZ":"우즈베크","UA":"우크라이나","ET":"이디오피아","IQ":"이라크","IR":"이란","IL":"이스라엘","EG":"이집트","IT":"이탈리아",
		   "IN":"인도","ID":"인도네시아","JP":"일본","JM":"자메이카","ZM":"잠비아","CN":"중국","MO":"중국","HK":"중국","CF":"중앙아프리카",
		   "DJ":"지부티","GI":"영국","ZW":"짐바브웨","TD":"차드","CZ":"체코","CS":"체코슬로바키아","CL":"칠레","CA":"카나다","CM":"카메룬",
		   "CV":"카보베르데","KY":"영국","KZ":"카자흐","QA":"카타르","KH":"캄보디아","KE":"케냐","CR":"코스타리카","CI":"코트디봐르",
		   "CO":"콜롬비아","CG":"콩고","CU":"쿠바","KW":"쿠웨이트","HR":"크로아티아","KG":"키르키즈스탄","KI":"키리바티","TJ":"타지키스탄",
		   "TZ":"탄자니아","TH":"타이","TC":"영국","TR":"터키","TG":"토고","TO":"통가","TV":"투발루","TN":"튀니지","TT":"트리니다드토바고",
		   "PA":"파나마","PY":"파라과이","PK":"파키스탄","PG":"파푸아뉴기니","PW":"미국","FO":"덴마크","PE":"페루","PT":"포르투갈",
		   "PL":"폴란드","PR":"미국","FR":"프랑스","GF":"프랑스","PF":"프랑스","FJ":"피지","FI":"필란드","PH":"필리핀","HU":"헝가리"}

whois_key = '발급키'

def IPInfo(domain, a, SiteName):
	if a == 1:
		domain = domain.split(",")
	elif a == 2:
		pass
	ipList = {}
	AllList = []
	with open('ipList.txt', 'w+') as file_w:
		for n, i in enumerate(domain):
			print(f"{n}:{i}")
			if "http://" in i or "https://" in i:
				i = i.split("//")[1]
			else:
				pass
			ip = socket.gethostbyname_ex(i)
			query = f"http://whois.kisa.or.kr/openapi/whois.jsp?query={ip[2][0]}&key={whois_key}&answer=json";
			req = urllib.request.urlopen(query).read().decode("utf-8")
			data = json.loads(req)
			if a == 1:
				ipList = {"Domain" : f"https://{i}",
						"IPList" : ','.join(ip[2]),
						"countryCode" : data['whois']['countryCode']}
				file_w.writelines(f"{n+1}. {ipList['Domain']} / {ipList['IPList']} / {Country[ipList['countryCode']]}\n")
			
			if a == 2:
				ipList = {"SiteName" : f"{SiteName[n]}",
						"Domain" : f"{i}",
						"IPList" : ','.join(ip[2]),
						"countryCode" : data['whois']['countryCode']}
				#file_w.writelines(f"{n+1}. {ipList['SiteName']}: {ipList['Domain']} / {ipList['IPList']} / {Country[ipList['countryCode']]}\n")
				file_w.writelines(f"{ipList['Domain']}\t{ipList['IPList']}\t{Country[ipList['countryCode']]}\n")
	return AllList


def get_title(path):
	# 엑셀 읽은 다음 전체 길이 및 이름 return
	data = pd.read_excel(path, engine="openpyxl")
	SiteName = {}
	title_num  = len(data.index)
	print(data.columns)
	for i in range(title_num):
		SiteName[data.SiteName[i]] = data.URL[i]

	return SiteName

if __name__ == "__main__":
	domain = ''' '''
	a = int(input("hell:"))
	if a == 1:
		AllList = IPInfo(domain, a, None)

	if a == 2:
		SiteName = get_title('test.xlsx')
		domain = list(SiteName.values())
		name = list(SiteName.keys())
		print(domain)
		AllList = IPInfo(domain, a, name)
