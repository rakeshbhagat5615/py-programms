import random


playerhp = 300
attackdmgl = 40
attackdmgh = 60

while playerhp > 0:
    dmg = random.randrange(attackdmgl, attackdmgh)
    playerhp = playerhp - dmg
    
    if playerhp <= 0:
        playerhp = 0
    
    print("Enemy attack you by damage", dmg, ",Your current HP is", playerhp)
    
    if playerhp == 0:
        print("You died")
