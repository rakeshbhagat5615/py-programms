import random


class Enemy:
    hp = 300
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh
    
    def getAtk(self):
        print("Enemies low attack is", self.atkl)
        print("Enemies high attack is", self.atkh)
    
    def getHp(self):
        print("Your HP is", self.hp)

enemy1 = Enemy(30, 35)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(50, 60)
enemy2.getAtk()
enemy2.getHp()



# This is single line comment and below is multiline comment
'''
playerhp = 300
attackdmgl = 40
attackdmgh = 60

while playerhp > 0:
    dmg = random.randrange(attackdmgl, attackdmgh)
    playerhp = playerhp - dmg
    
    if playerhp <= 30:
        playerhp = 30
    
    print("Enemy attack you by damage", dmg, ",Your current HP is", playerhp)
    
    if playerhp > 30:
        continue
    
    print("Your HP is low, you have taken to spawn point.")
    break
'''
