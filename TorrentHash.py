import os, hashlib, bencode, datetime
import pandas as pd

def DataInfo(path):
	Result = []
	for i in os.listdir(path):
		if i[-8:] == ".torrent":
			with open(i, "rb") as tf_r:
				metainfo = bencode.bdecode(tf_r.read())
				info = metainfo['info']
				hashData =hashlib.sha1(bencode.bencode(info)).hexdigest() 
				DateTime = datetime.datetime.fromtimestamp(int(os.path.getmtime(i))).strftime("%Y-%m-%d %H:%M:%S")
				ResultData = {
					"FileName" : i,
					"DateTime" : DateTime,
					"FileHash" : hashData,
					"FileSize" : os.path.getsize(i)
				}
				Result.append(ResultData)
	print(Result)
	return Result
  

if __name__ == "__main__":
    Result = DataInfo(".\\")
    df = pd.DataFrame(Result)
    df.to_excel(excel_writer="TorrentHash.xlsx", sheet_name = '토렌트 시드파일 해시값', index = True)
