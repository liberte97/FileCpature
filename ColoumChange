import pandas as pd
def excelChange(listExcel):
	for idx, r in enumerate(listExcel):
		df = pd.read_excel(r)
    #특정 컬럼 없애기
		df.drop(labels = ['없앨컬럼1', '없앨컬럼2'], axis=1, inplace=True)

    #특정 컬럼 이름 변경
		df.rename(columns={
			"기존컬럼1":"변경컬럼1",
			"기존컬럼2":"변경컬럼2",
			"기존컬럼3":"변경컬럼3"
		}, inplace=True)

		df.to_excel(f'새로 저장할 엑셀 제목({idx+1}).xlsx', index=False)

listExcel= ["Excel1.xlsx", "Excel2.xlsx", "Excel3.xlsx"]
excelChange(listExcel)
