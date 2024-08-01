#처음 부팅 할때[
OS_verison='1.1pre1'
print('disk A:\ (15GB)is selectd.')
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
    command_enter=input('A:/')
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
    else:
        print("no command")
