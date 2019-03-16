import requests
session = requests.Session()
response = session.get('http://159.89.166.12:13500/')
start=(session.cookies.get_dict())['flag']
md5=[]
md5.append(start)
for i in range(50):
	response = session.get('http://159.89.166.12:13500/')
	md5.append((session.cookies.get_dict())['flag'])
d={}
import hashlib
for a1 in range(256):
	for a2 in range(256):
		word=chr(a1)+chr(a2)
		d[(hashlib.md5(word.encode()).hexdigest())]=word
flag=''
# print(d)
for q in md5:
	try:
		flag+=d[q]
	except:
		continue
print(flag)

# flag	:	pctf{c0oki3s_@re_yUm_bUt_tHEy_@ls0_r3vEaL_@_l0t}
