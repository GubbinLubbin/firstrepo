from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
"Accept-Language":"en-US,en;q=0.9"}
gmail="ppythonpra@gmail.com"
password="obulwwvduxbreynw"
response=requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6",headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
whole = soup.find("span", class_="a-price-whole").text.replace(",", "").strip().replace(".", "")
fraction = soup.find("span", class_="a-price-fraction").text.strip()
price = float(whole) + int(fraction) / 100
if(price<100):
    mail=SMTP("smtp.gmail.com",587)
    mail.starttls()
    mail.login(gmail,password)
    message="Subject:Regarding price drop\n\nThe price of the product has been dropped"
    mail.sendmail(from_addr=gmail,to_addrs="silwalankit27@gmail.com",msg=message)
    mail.quit()
