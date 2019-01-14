class Pokemon:
    def __init__(self, level):
        self.level = level
        self.hp = self.level * 10
        self.stamina = self.level
        
    def set_hp(self, point):
        self.hp += point
        
        
    def check_status(self):
        if self.hp > 0:
            return True
        else: 
            return False
        
    def print_status(self):
        a = str(self.name) + '의 hp : ' + str(self.hp) +'\n'
        print(a)


import random
class Pikachu(Pokemon):
    
    name = '피카츄'
    types = ('elec')
    size = ('small')
    

    def body_attack(self, enemy):
        print(self.name +' is cast "body_attack" '+str((-1.0 * self.level))+' damaged')
        enemy.set_hp(-1.0 * self.level)
        
    def thousand_volt(self, enemy):
        if 'water' in enemy.types:
            enemy.set_hp(-1.5 * self.level)
            print(self.name +' is cast "thousand_volt" '+ str((-1.5 * self.level)) + ' damaged!')
            print('효과는 굉장했다!')
        else:
            enemy.set_hp(-1.2 * self.level)
            print(self.name +' is cast "thousand_volt" '+ ' dameged!')
            
    def roll_attack(self, enemy):
        if 'small' in enemy.size:
            enemy.set_hp(-1.3 * self.level)
            print(self.name +' is cast "roll_attack" '+ str((-1.3 * self.level))+ ' damaged!')
        else:
            enemy.set_hp(-0.9 * self.level)
            print(self.name +' is cast "roll_attack" '+ str((-0.9 * self.level))+' damaged!')
            
            
    def attack(self, enemy):
        print('-------------------------------------------------------------------------------------------\n')
        c = int(input('Enter the type of your action (1. body attack 2. thousand volt 3. roll attack): '))
        print('\n')
        if self.stamina < 2.0:
            self.body_attack(enemy)
        else:
            if c == 1:
                self.body_attack(enemy)
            elif c == 2:
                self.thousand_volt(enemy)
            elif c == 3:
                self.roll_attack(enemy)

            
            
class Squirtle(Pokemon):
    name = '꼬부기'
    types = ('water')
    size = ('small')
    picture = '''
                  _,........__
            ,-'            "`-.
          ,'                   `-.
        ,'                        \
      ,'                           .
      .'\               ,"".       `
     ._.'|             / |  `       \
     |   |            `-.'  ||       `.
     |   |            '-._,'||       | \
     .`.,'             `..,'.'       , |`-.
     l                       .'`.  _/  |   `.
     `-.._'-   ,          _ _'   -" \  .     `
`."""'-.`-...,---------','         `. `....__.
.'        `"-..___      __,'\          \  \     \
\_ .          |   `"""'    `.           . \     \
  `.          |              `.          |  .     L
    `.        |`--...________.'.        j   |     |
      `._    .'      |          `.     .|   ,     |
         `--,\       .            `7""' |  ,      |
            ` `      `            /     |  |      |    _,-'""`-.
             \ `.     .          /      |  '      |  ,'          `.
              \  v.__  .        '       .   \    /| /              \
               \/    `""\""`.       \   \  /.''                |
                `        .        `._ ___,j.  `/ .-       ,---.     |
                ,`-.      \         ."     `.  |/        j     `    |
               /    `.     \       /         \ /         |     /    j
              |       `-.   7-.._ .          |"          '         /
              |          `./_    `|          |            .     _,'
              `.           / `----|          |-............`---'
                \          \      |          |
               ,'           )     `.         |
                7____,,..--'      /          |
                                  `---.__,--.'
    '''
    
    def body_attack(self, enemy):
        print(self.name +' is cast "body_attack" '+ round(str((-1.1 * self.level)),2)+' damaged!')
        enemy.set_hp(-1.1 * self.level)
    
    def water_attack(self, enemy):
        if 'fire' in enemy.types:
            enemy.set_hp(-1.5 * self.level)
            print(self.name +' is cast "water_attack" '+ str((-1.5 * self.level))+' damaged!')
            print('효과는 굉장했다!')
        elif 'elec' in enemy.types:
            enemy.set_hp(-0.8 * self.level)
            print(self.name +' is cast "water_attack" '+ str((-0.8 * self.level))+' damaged!')
            print('효과는 ...별로...')
        else:
            print(self.name +' is cast "water_attack" '+ str((-1.2 * self.level))+' damaged!')
            enemy.set_hp(-1.2 * self.level)
    
    def throw_shells(self, enemy):
        print(self.name +' is cast "throw_shells" '+ str((-1.15 * self.level))+' damaged!')
        enemy.set_hp(-1.15 * self.level)
    
    def attack(self, enemy):
        c = random.choice([1, 2, 3])
        if c == 1:
            self.body_attack(enemy)
        elif c == 2:
            self.water_attack(enemy)
        elif c == 3:
            self.throw_shells(enemy) 
            
            
class Charmander(Pokemon):
    name = '파이리'
    types = ('fire')
    size = ('small')
    picture = '''
        _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         ""''     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \       _,-'           |       ''
        `._'               \   '"\                .      |
           |                '     \                `._  ,'
           |                 '     \                 .'|
           |                 .      \                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \                |       |           ,'   /
          ,' \               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\
   -" /`.         _,'     | _  _  _.|
    ""--'---""''""        `' '! |! /
                            `" " -' 
        '''

    
    def body_attack(self, enemy):
        print(self.name +' is cast "body_attack" '+ str((-1.0 * self.level))+' damaged!')
        enemy.set_hp(-1.0 * self.level)
    
    def fireball(self, enemy):
        if 'grass' in enemy.types:
            enemy.set_hp(-1.3 * self.level)
            print(self.name +' is cast "fireball" '+ str((-1.7 * self.level))+' damaged!')
            print('효과는 굉장했다!')
        elif 'water' in enemy.types:
            enemy.set_hp(-0.9 * self.level)
            print(self.name +' is cast "fireball" '+ str((-0.9 * self.level))+' damaged!')
            print('효과는 ...별로...')
        else:
            print(self.name +' is cast "fireball" '+ str((-1.1 * self.level))+' damaged!')
            enemy.set_hp(-1.1 * self.level)
    
    def firebreath(self, enemy):
        if 'grass' in enemy.types:
            enemy.set_hp(-1.7 * self.level)
            print(self.name +' is cast "firebreath" '+ str((-1.7 * self.level))+' damaged!')
            print('효과는 굉장했다!')
        elif 'water' in enemy.types:
            enemy.set_hp(-0.6 * self.level)
            print(self.name +' is cast "firebreath" '+ str((-0.6 * self.level))+' damaged!')
            print('효과는 ...별로...')
        else:
            print(self.name +' is cast "firebreath" '+ str((-1.2 * self.level))+' damaged!')
            enemy.set_hp(-1.2 * self.level)
    
    
    def attack(self, enemy):
        c = random.choice([1, 2, 3])
        if c == 1:
            self.body_attack(enemy)
        elif c == 2:
            self.fireball(enemy)
        elif c == 3:
            self.firebreath(enemy) 
            
            
class Bulbasaur(Pokemon):
    name = '이상해씨'
    types = ('grass')
    size = ('small')
    picture = '''
                  /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  \
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  ""''""                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''""''`.,^.`.--' 
        ''"
        '''
    
    def body_attack(self, enemy):
        print(self.name +' is cast "body_attack" '+ str((-1.0 * self.level))+' damaged!')
        enemy.set_hp(-1.25 * self.level)
    
    def whip_smash(self, enemy):
        print(self.name +' is cast "whip_smash" '+ str((-1.0 * self.level))+' damaged!')
        enemy.set_hp(-1.25 * self.level)
    
    def overgrow(self):
        print(self.name +' is cast "overgrow" '+ str((1.0 * self.level))+' healed!')
        self.set_hp(1.0 * self.level)
    
    def attack(self, enemy):
        c = random.choice([1, 2, 3])
        if c == 1:
            self.body_attack(enemy)
        elif c == 2:
            self.whip_smash(enemy)
        elif c == 3:
            self.overgrow()


def battle(p1, p2):
    import random
    # 선공 후공 결정
    vs = [p1, p2]
    random.shuffle(vs)
    winner = ''
    vs = tuple(vs)
    prev, after = tuple(vs)
    p = p2.name +'(level = '+ str(p2.level) +', hp = ' + str(p2.level*10) + ') 출현!!'
    print(p2.picture)
    print(p)
    
    print('\n\n내 포켓몬 : \n'+ p1.name +'(level = '+ str(p1.level) +', hp = ' + str(p1.level*10) + ')\n') 
    
    if p1.level > p2.level + 5:
        print('-------------------------------------------------------------/n')
        print('enemy is too weak...\n')
        print('-------------------------------------------------------------')
        k = int(input('would you let him go? yes(1) or no(2): '))
        if k == 2:
            while prev.check_status() and after.check_status():
                if prev.check_status:
                    prev.attack(after)
                    after.print_status()
                else:
                    winner = after.name
                    break
                if after.check_status():
                    after.attack(prev)
                    prev.print_status()
                else:
                    winner = prev.name
                    break

        else:
            print(p2.name + '이(가) 도망갔습니다.')
        
        
            
        
    elif p1.level < p2.level - 5:
        print('-------------------------------------------------------------\n')
        print('WARNING: enemy is way too strong to beat him.. RUN!!\n')
        print('-------------------------------------------------------------')
        k = int(input('do you want to escape from him? yes(1) or no(0): '))
        c = random.choice([1, 2])
        if k == 0:
            print('\nyou are failed to escape from him...')
            while prev.check_status() and after.check_status():
                if prev.check_status:
                    prev.attack(after)
                    after.print_status()
                else:
                    winner = after.name
                    break
                if after.check_status():
                    after.attack(prev)
                    prev.print_status()
                else:
                    winner = prev.name
                    break
        
            
        elif c == 1:
            print('\nEscape succeed!')
            
        elif c == 2:
            print('\nyou are failed to escape...Wish you survive..')
            while prev.check_status() and after.check_status():
                if prev.check_status:
                    prev.attack(after)
                    after.print_status()
                else:
                    winner = after.name
                    break
                if after.check_status():
                    after.attack(prev)
                    prev.print_status()
                else:
                    winner = prev.name
                    break
    
    if winner == '':
        print('-------------------------------------------------------------')
        print('경기 끝')
    else:
        print('-------------------------------------------------------------')
        print(winner + ' 이(가) 승리하였습니다.')

rand = random.choice(range(1,31))
monster = random.choice([Squirtle(rand), Charmander(rand), Bulbasaur(rand)])
battle(Pikachu(10), monster)