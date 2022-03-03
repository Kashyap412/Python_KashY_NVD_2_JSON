from os import listdir
from os.path import isfile, join
import zipfile
import json, os

pwd=os.getcwd()
p= pwd + '\\Output'
os.mkdir(p)

files = [f for f in listdir("nvd/") if isfile(join("nvd/", f))]
files.sort()


for file in files:
	archive = zipfile.ZipFile(join("nvd/", file), 'r')
	jsonfile = archive.open(archive.namelist()[0])
	cve_dict = json.loads(jsonfile.read())
	jsonfile.close()

	for i in range(0,len(cve_dict['CVE_Items']),1):
		filename = json.dumps(cve_dict['CVE_Items'][i]['cve']['CVE_data_meta']['ID'])
		filename = filename.split('"')[1]+".json"
		file = filename.split("-")[1]
		try: os.mkdir(p+"\\"+file)
		except: pass
		with open(p+'\\'+file+'\\'+filename, "a") as outfile:
			json_object = json.dumps(cve_dict['CVE_Items'][i], sort_keys=True, indent=4, separators=(',', ': '))
			outfile.write(json_object)
