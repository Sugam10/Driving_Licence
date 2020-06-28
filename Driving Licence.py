import requests
from bs4 import BeautifulSoup

BASE_URL = "https://parivahan.gov.in"
Driving_Licence_No = "DL-0420110149646"
Date_Of_Birth = "09-02-1976"

s = requests.Session()

data = {"pur_cd": "101", "form_rcdl:tf_dlNO": Driving_Licence_No, "form_rcdl:tf_dob_input": Date_Of_Birth}
r = s.post(f'{BASE_URL}/rcdlstatus/', data=data)

soup = BeautifulSoup(r.text, 'html.parser')





if soup.find(id='logout') is not None:
	print('Successfuly logged in')
else:
	print('Authentication Error')