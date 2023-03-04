from random import choice

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

emoji = ['🐻', '🐶', '🦄', '✍️', '✌️', '✅', '🥲', '👄']

won = 0

print(bcolors.HEADER + '=' * 100 + bcolors.ENDC)
print(f'{bcolors.OKCYAN}                                     <도박 치료용 프로그램>{bcolors.ENDC}')
print(bcolors.HEADER + '=' * 100 + bcolors.ENDC)



while True:
    try:
        run = int(input(f'{bcolors.OKBLUE}몇 판을 돌리실껀가요? : {bcolors.WARNING}{bcolors.BOLD}'))
        print(bcolors.ENDC)
        break
    except ValueError:
        print('숫자로 입력 바람.')
        print(bcolors.ENDC)
        continue

for x in range(run):
    chose1 = choice(emoji)
    chose2 = choice(emoji)
    chose3 = choice(emoji)

    # print(f'[ {chose1} ] [ {chose2} ] [ {chose3} ] / {x}')
    
    if chose1 == chose2 and chose2 == chose3 and chose3 == chose1:
        won = won + 1
        print(f'{bcolors.OKGREEN}[ {chose1} ] [ {chose2} ] [ {chose3} ] | {x} | 당첨{bcolors.ENDC}') 
        

    else:
        print(f'{bcolors.FAIL}[ {chose1} ] [ {chose2} ] [ {chose3} ] | {x}{bcolors.ENDC}')     

print(f'{bcolors.OKCYAN}{run}{bcolors.ENDC}판 실행됨 {bcolors.OKCYAN}{won}{bcolors.ENDC}판 만큼 이김')