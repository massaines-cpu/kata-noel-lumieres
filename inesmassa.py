#partie 1, étape 1 : grille 1000x1000, allumé = 1, éteint = 0, on commence avec grille éteinte donc 0
#liste de listes
taille=1000
grille_lights=[]
#boucle pour 1000 lignes
for i in range(taille): #pour 1000 zéro car éteint, j'ai vu qu'on pouvait faire ça pour aller plus vite
    ligne=[0]*1000
    grille_lights.append(ligne)
#etape2: instructions, prennent la forme de [action,x1,y1,x2,y2]
instructions=[
    ["turn on", 887, 9, 959, 629],
    ["turn on", 454, 398, 844, 448],
    ["turn off", 539, 243, 559, 965],
    ["turn off", 370, 819, 676, 868],
    ["turn off", 145, 40, 370, 997],
    ["turn off", 301, 3, 808, 453],
    ["turn on", 351, 678, 951, 908],
    ["toggle", 720, 196, 897, 994],
    ["toggle", 831, 394, 904, 860]]

for instruction in instructions:
    action = instruction[0]
    x1 = instruction[1]
    y1 = instruction[2]
    x2 = instruction[3]
    y2 = instruction[4]
    for x in range(x1,x2+1): #+1 pour faire une boucle
        for y in range(y1,y2 +1):
            if action=="turn on": # == car on pose une question
                grille_lights[y][x]=1 #pour allumer
            elif action=="turn off":
                grille_lights[y][x]=0 #pour eteindre
            elif action=="toggle": #pour switch 1 devient 0 et 0 devient 1
                if grille_lights[y][x]==0:
                    grille_lights[y][x]=1
                else:
                    grille_lights[y][x]=0
#etape 4 : on compte
lights_on=0
for ligne in grille_lights:
    lights_on=lights_on+sum(ligne) #decouverte de sum
print("Lumières allumées Partie 1 :", lights_on)
#j'ai trouvé 230022 pour la partie 1


#bloqué pour la partie 2, je crois qu'il faut faire la même chose avec des règles différentes mais il faut additionner
# des lumières j'ai un peu de mal à le traduire en langage python
#6 novembre reprise
#le debut c'est pareil que pour la premiere etape
taille=1000
grille_lumi=[]
for i in range(taille): #pour 1000 zéro car éteint, j'ai vu qu'on pouvait faire ça pour aller plus vite
    ligne=[0]*1000
    grille_lumi.append(ligne)
#on utilise les memes instructions que l'etape 1
for x in range(x1,x2+1):
    for y in range(y1,y2+1):
        lumi=grille_lumi[y][x]
        if action == "turn on":
            # +1
            grille_lumi[y][x] = lumi+1

        elif action == "turn off":
            #  -1 avec minimum zéro
            grille_lumi[y][x] = lumi-1
            if grille_lumi[y][x] < 0:
                grille_lumi[y][x] = 0  #on passe pas sous zéro

        elif action == "toggle":
                # +2
                grille_lumi[y][x] = lumi+2
lumi_totale = 0
for ligne in grille_lumi:
    lumi_totale += sum(ligne) # sum() additionne tous les nombres, même s'ils sont > 1 !

print(f"Luminosité combinée Partie 2 : {lumi_totale}")
#j'ai eu pas mal de difficulté pour la deuxième partie, je crois bien que le résultat est faux
#mais je ne comprends pas ce que je peux faire de plus dans ma démarche...