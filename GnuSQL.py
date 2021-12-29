# http://www.gnuwiz.com/ 사이트 참조
# 추가 sqlalchemy로 변경 예정

import requests, zipfile
import re, os
import pandas as pd
import pymysql

def connect_db():
	conn = pymysql.connect( host = "localhost",
							user = "root",
							password = "",
							db = "",
							charset = 'utf8' )
	return conn

def Result(i,result):
	print(type(result[0]))
	Title=["자유게시판", "갤러리", "공지사항"]
	if type(result[0]) is list:
		for idx, data in enumerate(result):
			df_w = pd.DataFrame(data)
			df_w.to_excel(excel_writer=f"데이터내역 {Title[idx]}.xlsx", sheet_name = f'전체내역', index = False, engine='xlsxwriter')
	else:
		df_w2 = pd.DataFrame(result)
		df_w2.to_excel(excel_writer=f"데이터내역(전체){i}).xlsx", sheet_name = f'전체내역', index = False, engine='xlsxwriter')

def VisitMem(conn):
	curs = conn.cursor(pymysql.cursors.DictCursor)
	# db query 작성
	table = "g5_visit"
	query = f"SELECT vi_ip, vi_date FROM {table}"
	curs.execute(query)
	data = curs.fetchall()
	resultList = []
	for j in data:
		result = {
			"IP": j["vi_ip"],
			"날짜": j["vi_date"]
		}		
		resultList.append(result)
	
	conn.commit()
	return resultList	

def MemTable(conn):
	curs = conn.cursor(pymysql.cursors.DictCursor)
	# db query 작성
	table = "g5_member"
	query = f"SELECT mb_no, mb_id, mb_password, mb_name, mb_nick, mb_nick_date, mb_email, mb_level, mb_certify, mb_sex, mb_birth, mb_tel, mb_hp, mb_adult, mb_recommend, mb_point, mb_today_login, mb_login_ip, mb_datetime, mb_ip, mb_leave_date, mb_intercept_date, mb_email_certify, mb_memo FROM {table}"
	curs.execute(query)
	data = curs.fetchall()
	resultList = []
	for j in data:
		result = {
			"아이디":j["mb_id"],
			"비밀번호(암호화)":j["mb_password"],
			"성명":j["mb_name"],
			"닉네임":j["mb_nick"],
			"닉네임 변경일자":j["mb_nick_date"],
			"이메일":j["mb_email"],
			"등급":j["mb_level"],
			"성별":j["mb_sex"],
			"생년월일":j["mb_birth"],
			"핸드폰번호":j["mb_hp"],
			"실명인증":j["mb_certify"],
			"성인유무":j["mb_adult"],
			"추천인":j["mb_recommend"],
			"포인트":j["mb_point"],
			"최근 로그인 일시":j["mb_today_login"],
			"최근 로그인 아이피":j["mb_login_ip"],
			"가입일시":j["mb_datetime"],
			"아이피":j["mb_ip"],
			"탈퇴일자":j["mb_leave_date"],
			"차단일자":j["mb_intercept_date"],
			"이메일인증일시":j["mb_email_certify"],
			"메모":j["mb_memo"]
		}		
		resultList.append(result)
	
	conn.commit()
	return resultList

def SiteTable(conn):
	curs = conn.cursor(pymysql.cursors.DictCursor)
	AllList, finalList = [], []
	# db query 작성
	
	table = ["g5_write_free", "g5_write_gallery", "g5_write_notice"]
	for idx, ta in enumerate(table):
		Titlequery = f"SELECT wr_id, wr_subject, wr_name, wr_content, wr_hit, wr_name, wr_email, wr_datetime, wr_ip FROM {ta}"
		curs.execute(Titlequery)
		data = curs.fetchall()
		resultList = []
		print(len(data))
		for j in data:
			'''
			Subquery = f"SELECT COUNT(wr_subject) as cnt FROM {ta} WHERE wr_1={j['wr_id']}"
			curs.execute(Subquery)
			data2 = curs.fetchall()
			print("print:",data2[0])
			if data2[0]["cnt"] == 0:
				cnt = 1
			else:
				cnt = data2[0]["cnt"]
			'''
			result = {
				"테이블명": ta,
				"구분": j["wr_id"],
				"게시판명": idx,
				"제목": j["wr_subject"],
				"내용": j["wr_content"],
				"게시자": j["wr_name"],
				"이메일": j["wr_email"],
				"조회수": j["wr_hit"],
				"게시일자": j["wr_datetime"],
				"IP": j["wr_ip"]
			}		
			resultList.append(result)
			AllList.append(result)
		finalList.append(resultList)
		
	conn.commit()
	return finalList, AllList




if __name__ == "__main__":
	conn = connect_db()
	# result, result2 = SiteTable(conn)
	#memresult = MemTable(conn)
	# print(memresult)
	# Result(1, result)
	# Result(2, result2)
	#Result(3, memresult)
	result = VisitMem(conn)
	Result(4, result)
	print("Done")

