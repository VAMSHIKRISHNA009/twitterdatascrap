from bs4 import BeautifulSoup#importing necessary modules
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

PATH = 'C:\Program File (x86)\chromedriver.exe'#driver path web own for every user
target_url = "https://x.com/GTNUK1"#here we hae toput our targeted profile urls
driver=webdriver.Chrome(PATH)#setting path

driver.get(target_url)#getting link
time.sleep(2)

resp = driver.page_source
driver.close()

soup=BeautifulSoup(resp,'html.parser')#finding html content

try:
    o["profile_name"]=soup.find("span",{"class":"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"}).text #profile name
except:
    o["profile_name"]=None

try:
    o["profile_bio"]=soup.find("span",{"class":"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"}).text
except:
    o["profile_bio"]=None`

try:
    o["profile_following count"]=profile_header.find("span",{"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"}).text#following count
except:
    o["profile_following count"]=None

try:
    o["profile_follower"]=profile_header.find("span",{"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"})#for followers count
except:
    o["profile_follower"]=None

try:
    o["profile_location"]=profile_header.find("span",{"css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3"}).text#location
except:
    o["profile_location"]=None
l.append(o)#appending all data

print(l)
df=pd.DataFrame()#row columns
df["profilename"]=profile_name
df["profilebio"]=profile_bio
df["followerscount"]=profile_following count
df["followincount"]=profile_follower
df["location"]=profile_location
df.to_csv("twitter.csv")#into excel form convert