#처음 부팅 할때[
os_pathnote='add del cmd'
OS_verison='1.2'
disk_left=15000
#mb
print('disk A:\ (15GB)is selectd.')
disk_left=disk_left-5
print('')
print('made by python3.12.3')
import time
print('  ')
time.sleep(2)
print('OS loader ver 7.1.7')
load=0
#]
#dy-dos파일 로드중[
time.sleep(3)
print('loading dy-dos files...')
time.sleep(0.5)
import tkinter as tk
while load!=101:
    print('loading', load, '%')
    load=load+1
print('complete loading dy-dos file...')
memo='[none]'
time.sleep(1)
#]
c=0
while c!='y':
    c=input('continue for press y...')

print('...')
time.sleep(3)
print('downloading system file...')
disk_left=disk_left-1000
time.sleep(3)
print('downloading user file...')
#주로 OS코딩 넣는 곳

desktop=['desktop.settings','install_dy-dos_ter_website.exe']
ter_web_installed=0
web_installed=0
time.sleep(1)

print('   ')
print(f'starting dy-dos{OS_verison}')
time.sleep(2)
#설치 과정[
print('')
print('enter your nickname')
user_name=input(':')
print('how old are you? (1~100)')
user_age=int(input(':'))
time.sleep(1)
print('Restarting...')
time.sleep(0.5)
print('')
print('starting dy-dos')
time.sleep(2)
print('')
#]
print(f'welocme, {user_name}.')
print('')
command_enter="NuLl"
while command_enter!='exit':
    cmd_link='A:/'
    command_enter=input(cmd_link)
    if command_enter=='print':
        print_in=input("print: ")
        print(print_in)
    elif command_enter=='calculator':
        command_enter_calculator=input('+ or * or / choose:')
        if command_enter_calculator=='+':
            rt=1
            ry=1
            print('help: enter ex) n+n')
            rt,ry=map(int,input(':').split('+'))
            print(rt + ry)
            rt=1
            ry=1
        elif command_enter_calculator=='*':
            rt=1
            ry=1
            print('help: enter ex) n*n')
            rt,ry=map(int,input(':').split('*'))
            print(rt*ry)
            rt=1
            ry=1
        elif command_enter_calculator=='/':
            rt=1
            ry=1
            print('help: enter ex) n/n')
            rt,ry=map(int,input(':').split('/'))
            if ry==0:
                print('It cannot be divided by 0')
            else:
                print(rt/ry)
                rt=1
                ry=1
    elif command_enter=='help':
        print("'print'==print word.")
        print("'calculator'== n+n , n*n or n/n.")
        print("'memo_enter'==memo enter.")
        print("'memo'==print memo while I enterd memo.")
        print("'exit'==shutdown dy-dos.")
        print("'OShelp'==print OSname and OSverison.")
        print("'disk_left'==print left disk mb/gb")
        print("'pathnote'==see pathnote this verison")
        print("'open'==open entered file")
        print("'del'==del entered file")
    elif command_enter=='exit':
        print('shutdowning...')
        time.sleep(2)
        exit
    elif command_enter=='memo_enter':
        print('enter memo...')
        memo=input(':')
        print('saved.')
    elif command_enter=='memo':
        print(memo)
    elif command_enter=='OShelp':
        print('OSname = dy-dos')
        print(f'OSverison = {OS_verison}')

    elif command_enter=='disk_left':
        print(f'disk left: {disk_left}mb left')
        print(f'disk left: {disk_left/1000}gb left')
    elif command_enter=='desktop':
        print(f'desk top: {desktop}')

    elif command_enter=='pathnote':
        print(os_pathnote)
    elif command_enter=='open':
        open_enter=0
        print('ex) A:/desktop/install_dy-dos_ter_website.exe')
        open_enter=input('open: ')
        if open_enter=='A:/desktop/install_dy-dos_ter_website.exe':
            if 'install_dy-dos_ter_website.exe' in desktop:
                if ter_web_installed==0:
                    ter_web_temp=['']
                    ter_web_program_code=['']
                    ter_web_program_code.append('if not OS==dy-dos:')
                    ter_web_program_code.append('   exit')
                    ter_web_program_code.append('')
                    ter_web_program_code.append('is OS==dy-dos:')
                    print("|------------------------|")
                    print("|                        |")
                    print("|        download        |")
                    print("|       cnt.website      |")
                    print("|           ...          |")
                    print("|                        |")
                    print("|                        |")
                    print("|________ver1.0.0________|")
                    disk_left=disk_left-1100
                    ter_web_program_code.append('	play_code_in_Code')
                    ter_web_program_code.append("   list(name:ter_web_temp)+'success_open_app'")
                    ter_web_program_code.append('   play code[success]:')              
                    time.sleep(3)
                    print("|------------------------|")
                    print("|                        |")
                    print("|        download        |")
                    print("|      web.expansion     |")
                    print("|           ...          |")
                    print("|                        |")
                    print("|                        |")
                    print("|________ver1.0.0________|")
                    disk_left=disk_left-260
                    time.sleep(3)
                    print("|------------------------|")
                    print("|                        |")
                    print("|        download        |")
                    print("|        complet!!       |")
                    print("|                        |")
                    print("|                        |")
                    print("|                        |")
                    print("|________ver1.0.0________|")
                    ter_web_program_code.append("		ter_web_temp+'web_load_sys:'")
                    ter_web_program_code.append("		ter_web_temp+'	connect https://'")
                    ter_web_program_code.append("		ter_web_temp+'	connect web sys'")
                    ter_web_program_code.append("		ter_web_temp+'	connect https://www.chromium.org/Home/'")
                    ter_web_program_code.append("		ter_web_temp+'	chromium project AI GPT3.0'")
                    disk_left=disk_left+59
                    ter_web_installed=1
                    disk_left=disk_left+1
                else:
                    print('This program is already installed. ')
    elif command_enter=='del':
        cmd_enter_del=0
        print('file del ex) A:/desktop/install_dy-dos_ter_website.exe')
        print('app del ex) app/dy-dos_ter_website')
        cmd_enter_del=input('del file: ')
        if cmd_enter_del=='A:/desktop/install_dy-dos_ter_website.exe':
            yorn=0
            yorn=input('real? (y,n)')
            if yorn=='y':
                if 'install_dy-dos_ter_website.exe' in desktop:
                    item_to_find = 'install_dy-dos_ter_website.exe'
                    if item_to_find in desktop:
                        index = desktop.index(item_to_find)
                        del desktop[index]
                        
        elif ter_web_installed==1:
            yorn=0
            yorn=input('real? (y,n)')
            if yorn=='y':
                ter_web_installed=0
                disk_left=disk_left+1300
            else:
                print('This file does not exist.')
    else:
        print("no command")
