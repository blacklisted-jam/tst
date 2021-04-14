#-*-coding:utf-8-*-

import os, re, sys, itertools, time, requests, random, threading, json, random
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
reload(sys)
sys.setdefaultencoding('utf8')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('termux-setup-storage')
    os.system('python2 .shahrukh.py')

from mechanize import Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]')]
br.addheaders = [('User-Agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
os.system('clear')
done = False

try:
    os.mkdir('/sdcard/out')
except OSError:
    pass
#def animate():
 #   for c in itertools.cycle(['\x1b[0;91m.', '\x1b[0;93m.', '\x1b[0;91m.', '\x1b[0;93m.']):
   #     if done:
        #    break
    #    sys.stdout.write('\r\x1b[0;97mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
      #  sys.stdout.flush()
        #time.sleep(0.1)


#t = threading.Thread(target=animasis)
#t.start()
#time.sleep(5)
#done = True

def keluar():
    print '\x1b[0;91m•\x1b[0;93m Sampai Jumpa :)\x1b[0;97m'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
        
logo = """
\033[1;92m    .S    .S_SSSs   SSS.        .SSS
\033[1;92m   .SS  .SS~SSSSS   sSSS        SSSs
\033[1;91m   S%S  S%S   SSSS  S%SSS      SSS%S
\033[1;91m   S%S  S%S    S%S  S%S  SS  SS  S%S
\033[1;97m   S&S  S%S•SSSS%S  S%S   s..s   S%S
\033[1;97m   S&S  S&S  SSS%S  S&S    ss    S&S
\033[1;94m   S&S  S&S    S&S  S&S          S&S
\033[1;94m   S&S  S&S    S&S  S&S          S&S
\033[1;93m   d*S  S*S    S&S  S*S          S*S
\033[1;93m  .S*S  S*S    S*S  S*S          S*S
\033[1;96msdSSS   S*S    S*S  S*S          S*S
\033[1;96mYSSY    SSS    S*S  SSS          S*S
\033[1;91m-----------------------------------------------
\033[1;97m➣ Author : Jam Shahrukh x Xtylo Ali Raza
\033[1;97m➣ Github : https://github.com/Stylish-Queen
\033[1;97m➣ Fb Page: Jam Shahrukh Official
\033[1;91m-----------------------------------------------"""

back = 0
threads = []
id = []
idteman = []
idfromteman = []

def masuk():
    os.system('clear')
    print logo
    print 50 * '\x1b[0;91m\xe2\x94\x80'
    time.sleep(0.07)
    print '\x1b[0;97m1).\x1b[0;97m Login With Token Facebook'
    time.sleep(0.07)
    print '\x1b[0;97m2).\x1b[0;97m Login With Cookie Facebook'
    time.sleep(0.07)
    print '\x1b[0;91m0\x1b[0;97m).\x1b[0;97m Exit'
    time.sleep(0.07)
    print 50 * '\x1b[0;91m\xe2\x94\x80'
    time.sleep(0.07)
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('* --> ')
    if msuk == '':
        print ' Wrong input!'
        pilih_masuk()
    elif msuk == '1':
        login_token()
    elif msuk == '2':
        login_cookie()
    elif msuk == '0':
        os.sys.exit()
    else:
        print ' Wrong input!'
        pilih_masuk()

def login_token():
    os.system('clear')
    print logo
    print 50 * '\x1b[0;91m\xe2\x94\x80'
    toket = raw_input(' Token \x1b[0;94m>\x1b[0;93m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan ('\x1b[0;92m Login Successful !\x1b[0;97m ')
        dump()
    except KeyError:
        print 'Token salah !'
        time.sleep(1.7)
        masuk()
    except requests.exceptions.SSLError:
        print ' Try Again'
        exit()


def login_cookie():
    os.system('clear')
    print logo
    print '\x1b[0;91m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.07)
    try:
        cookie = raw_input(' Cookie \x1b[0;94m>\x1b[0;93m ')
        data = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36', 'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8', 
           'cookie': cookie}
        coki = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers=data)
        cari = re.search('(EAAA\\w+)', coki.text)
        hasil = cari.group(1)
        zedd = open('login.txt', 'w')
        zedd.write(hasil)
        zedd.close()
        jalan ('\x1b[0;92m Login Succesful !\x1b[0;97m ')
        time.sleep(2)
        dump()
    except AttributeError:
        print ' Cookie salah !'
        time.sleep(2)
        masuk()
    except UnboundLocalError:
        print ' Cookie salah !'
        time.sleep(2)
        masuk()
    except requests.exceptions.SSLError:
        os.system('clear')
        print ' Koneksi Bermasalah'
        exit()



def dump():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    os.system('clear')
    print logo
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    print '\x1b[0;97m1).\x1b[0;97m \x1b[0;97mExtract File '
    print '\x1b[0;91m0\x1b[0;97m).\x1b[0;97m \x1b[0;97mBack To Cloning '
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    dump_pilih()


def dump_pilih():
    cuih = raw_input(' *--> ')
    if cuih == '':
        print ' Wrong input!'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        os.system('clear')
        time.sleep(1)
        os.system('python2 jam.py')
    else:
        print ' Wrong input!'
        dump_pilih()



def idfrom_teman():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print ' Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        masuk()

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        idt = raw_input(' User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' Target Name      : ' + op['name']
        except KeyError:
            print ' ID Publik Tidak Ada !'
            raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mPlease Wait ...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/jam.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'] + '\n')
            bz.write(a['id'] + '|')
            print '\r\x1b[0;92m(JAM)  \x1b[0;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m' + a['id'] +  '|' 

        bz.close()
	print 50 * '\x1b[1;91m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x9c\x93 \x1b[0;97m)\x1b[0;97m Exract ID Done \x1b[0;97m....'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mName File : ')
        os.rename('out/jam.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x88\x9a \x1b[0;97m) File Save : save/' + done
        raw_input('\n\x1b[0;97m(\x1b[0;91mBack\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File Not Found '
        raw_input('\n\x1b[0;97m(\x1b[0;91mBack\x1b[0;97m)')
        dump()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Error creating file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mBack\x1b[0;97m)')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Error '
        raw_input('\n\x1b[0;97m(\x1b[0;91mBack\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File Error !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mBack\x1b[0;97m)')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File Error !'
        keluar()
        
        
if __name__ == '__main__':
	dump()
	masuk()
        
