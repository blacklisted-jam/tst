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
    os.system('python2 dump.py')
    
from mechanize import Browser
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]')]
br.addheaders = [('User-Agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]
os.system('clear')
done = False

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
        
logo = ('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')

back = 0
threads = []
id = []
idteman = []
idfromteman = []


def dump():
    global toket
    os.system('clear')
    try:
        toket = open('access_token.txt', 'r')
    except IOError:
        print ' Token invalid '
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.system('python2 jam.py')

    os.system('clear')
    os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    print '\x1b[0;97m1).\x1b[0;97m Dump ID Dari Daftar Teman '
    print '\x1b[0;97m2).\x1b[0;97m \x1b[0;97mDump ID Dari Teman/Publik '
    print '\x1b[0;91m0\x1b[0;97m).\x1b[0;97m \x1b[0;97mKeluar '
    print 50 * '\x1b[1;91m\xe2\x94\x80'
    dump_pilih()


def dump_pilih():
    cuih = raw_input(' *--> ')
    if cuih == '':
        print ' Isi Yg Benar Sayang!'
        dump_pilih()
    elif cuih == '1' or cuih == '01':
        id_teman()
    elif cuih == '2' or cuih == '02':
        idfrom_teman()
    elif cuih == '0' or cuih == '00':
        os.sys.exit()
    else:
        print ' Isi Yg Benar Sayang!'
        dump_pilih()


def id_teman():
    os.system('clear')
    try:
        toket = open('access_token.txt', 'r')
    except IOError:
        print ' Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.system('python2 jam.py')

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Mengambil semua ID Teman \x1b[0;97m...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/id_teman.txt', 'w')
        for a in z['data']:
            idteman.append(a['id'])
            bz.write(a['id'] + '\n')
            print '\r\x1b[0;97m(\x1b[0;93m' + str(len(idteman)) + '\x1b[0;97m)\x1b[0;94m > ',
            sys.stdout.flush()
            time.sleep(0.005)
            print '\x1b[0;97m' + a['id']

        bz.close()
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;92m\xe2\x9c\x93\x1b[0;97m) \x1b[0;97mSukses Mengambil ID \x1b[0;97m....'
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mTotal ID\x1b[0;91m :\x1b[0;97m %s' % len(idteman)
        done = raw_input('\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) Simpan Nama File\x1b[0;91m : \x1b[0;97m')
        os.rename('out/id_teman.txt', 'out/' + done)
        print '\r\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) File tersimpan \x1b[0;91m: \x1b[0;97mout/' + done
        print '\n\x1b[1;91m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
        raw_input('\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except IOError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Gagal membuat file'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except (KeyboardInterrupt, EOFError):
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Terhenti ! '
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except KeyError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Gagal !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except OSError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) File anda tidak tersimpan !'
        raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
        dump()
    except requests.exceptions.ConnectionError:
        print '\x1b[0;97m(\x1b[0;91m!\x1b[0;97m) Tidak ada koneksi !'
        keluar()


def idfrom_teman():
    os.system('clear')
    try:
        toket = open('access_token.txt', 'r')
    except IOError:
        print ' Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        os.system('python2 jam.py')

    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        os.system('clear')
        os.system('echo " •••\n  ___  _   _ __  __ ___ \n |   \| | | |  \/  | _ \ \n | |) | |_| | |\/| |  _/ \n |___/ \___/|_|  |_|_|  \n\n •••" | lolcat ')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        idt = raw_input(' User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print ' Nama Akun      : ' + op['name']
        except KeyError:
            print ' ID Publik Tidak Ada !'
            raw_input('\n\x1b[0;97m(\x1b[0;91mKembali\x1b[0;97m)')
            dump()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(50000)&access_token=' + toket)
        z = json.loads(r.text)
        jalan('\x1b[0;97m(\x1b[0;94m\xe2\x80\xa2\x1b[0;97m) \x1b[0;97mMengambil Semua ID ...')
        print 50 * '\x1b[1;91m\xe2\x94\x80'
        bz = open('out/id_teman_from_teman.txt', 'w')
        for a in z['friends']['data']:
            idfromteman.append(a['id'])
            bz.write(a['id'] + '\n')
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
	dump()
	masuk()
        

