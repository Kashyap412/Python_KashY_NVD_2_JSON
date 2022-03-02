import requests,re,os

pwd=os.getcwd()
p= pwd + '\\nvd'
os.mkdir(p)


r = requests.get('https://nvd.nist.gov/vuln/data-feeds#JSON_FEED')
	
for filename in re.findall("nvdcve-1.1-[0-9]*\.json\.zip",r.text):
	print(filename)
	r_file = requests.get("https://nvd.nist.gov/feeds/json/cve/1.1/" + filename, stream=True)			
	#print(r_file)
	with open("nvd/" + filename, 'wb') as f:
		for chunk in r_file:
			f.write(chunk)
