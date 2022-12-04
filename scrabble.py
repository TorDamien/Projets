import random
import copy
#/////////////////////////////// PLATEAU DE JEU //////////////////////////////////////
def init_bonus():
    Bonus = [[["MT"],[""],[""],["LD"],[""],[""],[""],["MT"],[""],[""],[""],["LD"],[""],[""],["MT"]],#de 0 à 14
             [[""],["MD"],[""],[""],[""],["LT"],[""],[""],[""],["LT"],[""],[""],[""],["MD"],[""]],# de 15 à 29
             [[""],[""],["MD"],[""],[""],[""],["LD"],[""],["LD"],[""],[""],[""],["MD"],[""],[""]],#de 30 à 44
             [["LD"],[""],[""],["MD"],[""],[""],[""],["LD"],[""],[""],[""],["MD"],[""],[""],["LD"]],
             [[""],[""],[""],[""],["MD"],[""],[""],[""],[""],[""],["MD"],[""],[""],[""],[""]],
             [[""],["LT"],[""],[""],[""],["LT"],[""],[""],[""],["LT"],[""],[""],[""],["LT"],[""]],
             [[""],[""],["LD"],[""],[""],[""],["LD"],[""],["LD"],[""],[""],[""],["LD"],[""],[""]],
             [["MT"],[""],[""],["LD"],[""],[""],[""],["MD"],[""],[""],[""],["LD"],[""],[""],["MT"]],
             [[""],[""],["LD"],[""],[""],[""],["LD"],[""],["LD"],[""],[""],[""],["LD"],[""],[""]],
             [[""],["LT"],[""],[""],[""],["LT"],[""],[""],[""],["LT"],[""],[""],[""],["LT"],[""]],
             [[""],[""],[""],[""],["MD"],[""],[""],[""],[""],[""],["MD"],[""],[""],[""],[""]],
             [["LD"],[""],[""],["MD"],[""],[""],[""],["LD"],[""],[""],[""],["MD"],[""],[""],["LD"]],
             [[""],[""],["MD"],[""],[""],[""],["LD"],[""],["LD"],[""],[""],[""],["MD"],[""],[""]],
             [[""],["MD"],[""],[""],[""],["LT"],[""],[""],[""],["LT"],[""],[""],[""],["MD"],[""]],
             [["MT"],[""],[""],["LD"],[""],[""],[""],["MT"],[""],[""],[""],["LD"],[""],[""],["MT"]],
             ]


    return Bonus

def init_jeton():
    jeton_vide =[]
    for i in range(15):
        lst=[]
        for j in range(15):
              lst.append(["  "," "])
        jeton_vide.append(lst)
    return jeton_vide

def combine_bonus_jeton(jeton,bonus):
    for i in range(len(jeton)):
        for j in range(len(jeton[i])):
            if bonus[i][j] != "":
                jeton[i][j][1] = bonus[i][j]
    return jeton


        
def affiche_jeton(plateau):
    k = 1
    l = 1
    plateau = copy.deepcopy(plateau)
    for i in range(15):      
        for j in range(15):
            if plateau[i][j][0] == "  " and plateau[i][j][1] == ["MT"]:
                plateau[i][j][0] = " ~"
            if plateau[i][j][0] == "  " and plateau[i][j][1] == ["MD"]:
                plateau[i][j][0] = " °"
            if plateau[i][j][0] == "  " and plateau[i][j][1] == ["LT"]:
                plateau[i][j][0] = " *"
            if plateau[i][j][0] == "  " and plateau[i][j][1] == ["LD"]:
                plateau[i][j][0] = " ^"

    a = 0
    b = 0
    c = 0    
    if c == 0:
        for k in range(15):
            if k == 0:
                print(" ","\t",k," ","\t",sep='',end='') 
            else:
                print(" ",k," ","\t",sep='',end='')
            k+=1
        c += 1        
        print()
    while a < 15:
        while b < 15:
            if b == 0:
                
                print(a ,"\t",sep='',end='')
                if plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["MT"]: 
                    print("|",plateau[a][b][0],"~|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["MD"]: 
                    print("|",plateau[a][b][0],"°|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["LT"]:
                    print("|",plateau[a][b][0],"*|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["LD"]:
                    print("|",plateau[a][b][0],"^|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^":
                    print("|",plateau[a][b][0]," |","\t",sep='',end='')
                else:
                    print("|",plateau[a][b][0],"|","\t",sep='',end='')
          
            else:
                if plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["MT"]:
                    print("|",plateau[a][b][0],"~|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["MD"]:
                    print("|",plateau[a][b][0],"°|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["LT"]:
                    print("|",plateau[a][b][0],"*|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^" and  plateau[a][b][1] == ["LD"]:
                    print("|",plateau[a][b][0],"^|","\t",sep='',end='')
                elif plateau[a][b][0] != "  " and plateau[a][b][0] != " ~" and plateau[a][b][0] != " °" and plateau[a][b][0] != " *" and plateau[a][b][0] != " ^":
                    print("|",plateau[a][b][0]," |","\t",sep='',end='')
                else:
                    print("|",plateau[a][b][0],"|","\t",sep='',end='')
            b+=1
                  
        a+= 1        
        b = 0
        print()

      
#/////////////////////////////// PIOCHE //////////////////////////////////////////////
def ini_dico():
    dictionnaire = {
                    'A' : {'occ' : 9, 'val' : 1},
                     'B' : {'occ' : 2, 'val' : 3},
                      'C' : {'occ' : 2, 'val' : 3},
                       'D' : {'occ' : 3, 'val' : 2},
                        'E' : {'occ' : 15, 'val' : 1},
                         'F' : {'occ' : 2, 'val' : 4},
                          'G' : {'occ' : 2, 'val' : 2},
                           'H' : {'occ' : 2, 'val' : 4},
                            'I' : {'occ' : 8, 'val' : 1},
                             'J' : {'occ' : 1, 'val' : 8},
                              'K' : {'occ' : 1, 'val' : 10},
                               'L' : {'occ' : 5, 'val' : 1},
                                'M' : {'occ' : 3, 'val' : 2},
                                 'N' : {'occ' : 6, 'val' : 1},
                                  'O' : {'occ' : 6, 'val' : 1},
                                   'P' : {'occ' : 2, 'val' : 3},
                                    'Q' : {'occ' : 1, 'val' : 8},
                                     'R' : {'occ' : 6, 'val' : 1},
                                      'S' : {'occ' : 6, 'val' : 1},
                                       'T' : {'occ' : 6, 'val' : 1},
                                        'U' : {'occ' : 6, 'val' : 1},
                                         'V' : {'occ' : 2, 'val' : 4},
                                          'W' : {'occ' : 1, 'val' : 10},
                                           'X' : {'occ' : 1, 'val': 10},
                                            'Y' : {'occ' : 1, 'val' : 10},
                                             'Z' : {'occ' : 1, 'val' : 10},
                                              '?' : {'occ' : 2, 'val' : 0},

                                            }
    return dictionnaire



def ini_pioche(dico):
    pioche = []
    lettre = ord('A')
    i = 0
    while i < len(dico) and lettre <= ord('Z'):
        lettre_2 = chr(lettre)
        for i in range (dico[lettre_2]['occ']):
            pioche.append(lettre_2)
        lettre += 1
        i+=1
    for i in range(dico['?']['occ']):
        pioche.append('?')
    return pioche


def piocher(x,sac):
    i = 0
    pioche = []
    while i < x:
        if len(sac) == 0:
            i = x
        else:
            nombre = random.randint(0,len(sac)-1)
            pioche.append(sac[nombre])
            sac.remove(sac[nombre])
            i += 1
    return pioche

def completer_main(main,sac):
    nb_lettre_ajout = 7 - len(main)
    lettre_pioche = piocher(nb_lettre_ajout, sac)
    main.extend(lettre_pioche)

def echanger(jetons,main,sac):
    nb_echange = len(jetons) 
    i = 0
    while i < len(jetons):
        if jetons == [] or jeton[i] not in main:
            
            main.remove(jetons[i])     
            i+=1
    completer_main(main,sac)
    sac.extend(jetons)
    



#/////////////////////////// CONSTRUCTION DE MOTS ////////////////////////////////////


def genere_dico(nf):
  with open(nf) as f:
    mots = [ligne.rstrip() for ligne in f]
  return mots




def mot_jouable(mot,ll): #string,liste / FONCTIONNE
    nb_joker = ll.count("?") #Une lettre joker est considéré comme un "?"
    #mot = mot.upper()
    lettre_mot = list(mot)
    x=0

    while x < len(lettre_mot):
        nb_lettre = lettre_mot.count(lettre_mot[x])
        if nb_lettre > ll.count(lettre_mot[x]):
            nb_joker -= abs(nb_lettre - ll.count(lettre_mot[x]))  #enlève autant de joker de que lettre manquante
            if nb_joker < 0:#si plus de joker return False
                return False #booleen
        x+=1
    return True #booleen

#print("fzesfsefsefsf",mot_jouable('ELUCIDATION',ll))

#print(mot_jouable(mot,ll))

#motsfr = ["COURIR", "PIED", "DEPIT", "TAPIR", "MARCHER"]
#ll = ["P", "I", "D", "E", "T", "A", "R"]

def mots_jouables(liste_mots_existant,ll): #FONCTIONNE
    jouable = []
    i=0
    while i < len(liste_mots_existant):
        if mot_jouable(liste_mots_existant[i],ll):
            jouable.append(liste_mots_existant[i])
        i+=1
    return jouable #liste

#print("aaaaaaa",mots_jouables(liste_mots_existant,ll))
#print(mots_jouables(motsfr,ll))


#////////////////////////// VALEUR MOT //////////////////////////////////////////////

def valeur_mot(mot,dico): 
    #mot = upper.mot()
    liste_lettre = list(mot)
    i=0
    somme = 0
    while i < len(mot):
        #print(dico[liste_lettre[i]])
        #print(dico[liste_lettre[i]]['val'])
        somme += dico[liste_lettre[i]]['val']
        i+=1
    if len(mot) == 7: #bonus
        somme += 50
        
    return somme #int

def meilleur_mot(motsfr, ll, dico):
    jouable = mots_jouables(motsfr,ll)
    if jouable == []:
        return "" #string
    meilleur = jouable[0]
    i=0
    while i < len(jouable):
        if valeur_mot(meilleur) < valeur_mot(jouable[i]):
            meilleur = jouable[i]
        i+=1
    return meilleur #string




def meilleurs_mot(motsfr, ll, dico): #Prend la valeur du meilleur mot puis ajoute à une liste tous ceux qui on la même valeur
    meilleur = meilleur_mot(motsfr, ll, dico)
    liste_meilleurs = []
    if meilleur == "":
        return liste_meilleurs #liste
    jouable = mots_jouables(motsfr,ll)
    i = 0
    
    while i < len(jouable):
        if valeur_mot(meilleur) == valeur_mot(jouable[i]):
            liste_meilleurs.append(jouable[i])
        i+=1
    return liste_meilleurs #liste




#////////////////////////// PLACEMENT DE MOT ///////////////////////////////////




def lire_coords():
    liste_nombre_autorise = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14']
    coord_ligne = input("Entrer le numéro de la ligne : ")
    while coord_ligne not in liste_nombre_autorise:
        print("Le valeur donnée n'est pas une ligne du plateau. Entrer un nouveau numéro de ligne: ",end="")
        coord_ligne = input()
    coord_ligne = int(coord_ligne)
    coord_colonne = input("Entrer le numéro de la colonne: ")
    while coord_colonne not in liste_nombre_autorise:
        print("Le valeur donnée n'est pas une ligne du plateau. Entrer un nouveau numéro de colonne: ",end="")
        coord_colonne = input()
    coord_colonne = int(coord_colonne)
    #coord_ligne_vide = 0
    #coord_colonne_vide = 0
    #while plateau[coord_ligne][coord_colonne][0] != "  ":
        #print("La case choisit n'est pas libre.")
        #coord_ligne = input("Entrer le numéro de la ligne:")
        #while coord_ligne not in liste_nombre_autorise:
            #print("Le valeur donnée n'est pas une ligne du plateau. Entrer un nouveau numéro de ligne: ",end="")
            #coord_ligne = input()
        #coord_ligne = int(coord_ligne)
        #coord_colonne = input("Entrer le numéro de la colonne:")
        #while coord_colonne not in liste_nombre_autorise:
            #print("Le valeur donnée n'est pas une ligne du plateau. Entrer un nouveau numéro de ligne: ",end="")
            #coord_colonne = input()
        #coord_colonne= int(coord_colonne)

    return coord_ligne,coord_colonne





def tester_placement(plateau,i,j,direction,mot,ll):
    copie_mot = list(mot)
    copie_liste_lettre = copy.copy(ll)
    a = 0#incrementeur
    mot_requis = []
    copie_ligne = copy.copy(i)
    copie_colonne = copy.copy(j)   
    temp = []
    #print(jetons[0][0][0])
    while a < (len(copie_mot)): # tant qu'on attend pas la longueur du mot
        if 0<= i <= 14 and 0<= j <= 14: #tant qu'on sort pas des limites du placeau
            if direction == "haut":
                #print(1,"1")
                if 14 >= copie_ligne+1 and plateau[copie_ligne+1][j][0] != "  ": 
                    while 14 >= copie_ligne+1 and plateau[copie_ligne+1][j][0] != "  ":
                        #while plateau[copie_ligne-1][j][0] != "  ":
                        #print(2,"1")
                        temp.append(plateau[copie_ligne+1][j][0])
                        #print(temp,'temp1')
                        copie_ligne +=1
                        #print(copie_ligne,"copie_ligne1")
                        temp = retourne_lettre(temp)
                        #print(temp,'retourne temp1')
                        for w in range(len(temp)):
                            if temp[w] == mot[w]:
                                #print(temp[w],"temp[w]1")
                                #print(mot[w],"mot[w]1")
                                #print(copie_mot,"1")
                                copie_mot.pop(0)
                                #print(copie_mot,"1")
                            else:
                                #print(3,"1")
                                return []
                        a-=1
                        copie_ligne = 15
                              
                else:
                    #print(4,"1")
                    if plateau[i][j][0] == copie_mot[a]:  #or jeton[i][j][0] == "?":
                        #print(5,"1")
                        i -= 1
                    elif plateau[i][j][0] != "  ":
                        if copie_mot[a] not in copie_liste_lettre:
                            if '?' in copie_liste_lettre:
                                #print(6,"1")
                                #print(mot_requis,"avant1")
                                #print(copie_liste_lettre,"avant2")
                                mot_requis.append('?')
                                copie_liste_lettre.remove('?')
                                #print(mot_requis,"apres1")
                                #print(copie_liste_lettre,"apres2")
                                i-=1
                            else:
                                return []
                        elif plateau[i][j][0] == copie_mot[a]:
                            return []
                    #elif plateau[i][j][0] != "  ":
                        #print(7,"1")
                        #return []
                    else:
                        if copie_mot[a] in copie_liste_lettre:
                            #print(mot_requis,"avant3")
                            #print(copie_liste_lettre,"avant4")
                            mot_requis.append(copie_mot[a])
                            copie_liste_lettre.remove(copie_mot[a])
                            #print(mot_requis,"apres3")
                            #print(copie_liste_lettre,"apres4")
                            i -= 1
                        elif '?' in copie_liste_lettre :
                            mot_requis.append('?')
                            copie_liste_lettre.remove('?')
                            i-=1
                        else:
                            return []
                        
                
            elif direction == "bas":
                #print(1,"2")
                if 0 <= copie_ligne-1 and plateau[copie_ligne-1][j][0] != "  ":
                    while 0 <= copie_ligne-1 and plateau[copie_ligne-1][j][0] != "  ":
                        #print(a,"apreswhil")
                        if plateau[copie_ligne+1][j][0] != "  ":
                            #print(2,"2")
                            temp.append(plateau[copie_ligne-1][j][0])
                            #print(temp,'temp')
                            copie_ligne -=1
                            temp = retourne_lettre(temp)
                            #print(temp,'retourne temp')
                        for w in range(len(temp)):
                            if temp[w] == mot[w]:
                                #print(temp[w],"temp[w]")
                                #print(mot[w],"mot[w]")
                                #print(copie_mot)
                                copie_mot.pop(0)
                                #print(copie_mot)
                            else:
                                #print(4,"2")
                                return []
                        #print(a,"avant a-1")
                        a-=1
                        copie_ligne = -1
                              
                else:
                    #print(a,"apreselse")
                    #print(3,"2")
                    if plateau[i][j][0] == copie_mot[a]: #or jeton[i][j][0] == "?":
                        #print(4,"2")
                        i += 1
                    elif plateau[i][j][0] != "  ":
                        if copie_mot[a] not in copie_liste_lettre:
                            if '?' in copie_liste_lettre:
                                #print(5,"2")
                                #print(mot_requis,"avant")
                                #print(copie_liste_lettre,"avant")
                                mot_requis.append('?')
                                copie_liste_lettre.remove('?')
                                #print(mot_requis,"apres")
                                #print(copie_liste_lettre,"apres")
                                i+=1
                            else:
                                #print(6,"2")
                                return []
                        elif plateau[i][j][0] == copie_mot[a]:
                            return []

                    #elif plateau[i][j][0] != "  ":
                        #print(7,"2")
                        #return []
                    else:

                        if copie_mot[a] in copie_liste_lettre:
                            #print(8,"2")
                            #print(mot_requis,"avant2")
                            #print(copie_liste_lettre,"avant2")
                            mot_requis.append(copie_mot[a])
                            copie_liste_lettre.remove(copie_mot[a])
                            #print(mot_requis,"apres2")
                            #print(copie_liste_lettre,"apres2")
                            i += 1
                        elif '?' in copie_liste_lettre :
                            #print(copie_mot,"etgzey")
                            #print(copie_mot[a],"ioio")
                            #print(copie_liste_lettre,"mkmjl")

                            mot_requis.append('?')
                            copie_liste_lettre.remove('?')
                            i+=1
                        else:
                            return []
                
            elif direction == "droite":
                #print(1,"3")
                if 0 <= copie_colonne-1 and plateau[i][copie_colonne-1][0] != "  ":
                    while 0 <= copie_colonne-1 and plateau[i][copie_colonne-1][0] != "  ":
                        #print(a,"apreswhil")
                        if plateau[i][copie_colonne-1][0] != "  ":
                            #print(2,"3")
                            temp.append(plateau[i][copie_colonne-1][0])
                            #print(temp,'temp')
                            copie_colonne -=1
                            #print(temp,'retourne temp')
                            retourne_lettre(temp)
                        for w in range(len(temp)):
                            if temp[w] == mot[w]:
                                #print(temp[w],"temp[w]")
                                #print(mot[w],"mot[w]")
                                #print(copie_mot)
                                copie_mot.pop(0)
                                #print(copie_mot)
                            else:
                                #print(4,"3")
                                return []
                        #print(a,"avant a-1")
                        a-=1
                        copie_colonne = -1
                          
                else:
                    #print(a,"apreselse")
                    #print(3,"3")

                    if plateau[i][j][0] == copie_mot[a]: #or jeton[i][j][0] == "?":
                        #print(4,"3")
                        j += 1
                    elif plateau[i][j][0] != "  ":
                        if copie_mot[a] not in copie_liste_lettre:
                            if '?' in copie_liste_lettre:
                                #print(5,"3")
                                #print(mot_requis,"avant")
                                #print(copie_liste_lettre,"avant")
                                mot_requis.append('?')
                                copie_liste_lettre.remove('?')
                                #print(mot_requis,"apres")
                                #print(copie_liste_lettre,"apres")
                                j+=1
                            else:
                                #print(6,"3")
                                return []
                        elif plateau[i][j][0] == copie_mot[a]:
                            return []

                    elif plateau[i][j][0] != "  ":
                        #print(7,"3")
                        return []
                    else:
                        if copie_mot[a] in copie_liste_lettre:
                            #print(8,"3")
                            #print(mot_requis,"avant2")
                            #print(copie_liste_lettre,"avant2")
                            mot_requis.append(copie_mot[a])
                            copie_liste_lettre.remove(copie_mot[a])
                            #print(mot_requis,"apres2")
                            #print(copie_liste_lettre,"apres2")
                            j += 1
                        elif '?' in copie_liste_lettre :
                            #print(copie_mot,"zzz")
                            #print(copie_mot[a],"zeg")
                            #print(copie_liste_lettre,"ézrar")
                            mot_requis.append('?')
                            copie_liste_lettre.remove('?')
                            j+=1
                        else:
                            return []
                        
                
            elif direction == "gauche":
                if 14 >= copie_colonne+1 and plateau[i][copie_colonne+1][0] != "  ":
                    while 14 >= copie_colonne+1 and plateau[i][copie_colonne+1][0] != "  ":
                        #if plateau[i][copie_colonne+1][0] != "  ":
                        temp.append(plateau[i][copie_colonne+1][0])
                        copie_colonne +=1
                        temp = retourne_lettre(temp)
                        for w in range(len(temp)):
                            if temp[w] == mot[w]:
                                copie_mot.pop(0)
                            else:
                                return []
                        a-=1
                        copie_colonne = 15
                                  
                else:

                    if plateau[i][j][0] == copie_mot[a]: #or jeton[i][j][0] == "?":
                        j -= 1              
                    elif plateau[i][j][0] != "  ":
                        if copie_mot[a] not in copie_liste_lettre:
                            if '?' in copie_liste_lettre:
                                mot_requis.append('?')
                                copie_liste_lettre.remove('?')
                                j-=1
                            else:
                                return []
                        elif plateau[i][j][0] == copie_mot[a]:
                            return []

                    #elif plateau[i][j][0] != "  ":
                        #return []               
                    else:
                        if copie_mot[a] in copie_liste_lettre:
                            mot_requis.append(copie_mot[a])
                            copie_liste_lettre.remove(copie_mot[a])
                            j -= 1
                        elif '?' in copie_liste_lettre :
                            mot_requis.append('?')
                            copie_liste_lettre.remove('?')
                            j-=1
                        else:
                            return []
                        
            #print(a,"avant a+1")
            a+=1
        else:
            #print("aie")
            return []
    #print(a,"final")
    #print("yes papy")        
    return mot_requis #liste des lettres dans l'ordre à poser






def list_valeur_mot(dico,mot): # return une liste des valeurs du mot sans les additionner
    liste_lettre = list(mot)
    liste_valeur = []    
    for i in range(len(liste_lettre)):
        liste_valeur.append(dico[liste_lettre[i]]['val'])
    return liste_valeur

def calcule_liste_valeur_finale(liste):
    somme = 0
    for i in range(len(liste)):
        somme += int(liste[i])
    if len(liste) == 7:
        somme += 50
    return somme

def valeur_des_bonus(lettredesbonus):
    valeur = 0
    if lettredesbonus == ['MT'] or lettredesbonus == ['LT']:
        valeur = 3
    if lettredesbonus == ['MD'] or lettredesbonus == ['LD']:
        valeur = 2
    return valeur

def retourne_lettre(mot):  #fonction pour retourner les lettres récolté par combi_or_not_combi
    lettre_retourne = []
    i = len(mot)-1
    while i >= 0:
        lettre_retourne.append(mot[i])
        i-=1        
    return lettre_retourne

#Maintenant il faut une fonction booléènne qui regarde si la liste est vide ou non, regarde si les mots de la liste existe et calcule les points    
def point_mot_deja_pose(mot,dico): #Une fonction spéciale qui calcule les points combo sans les 50 du scrabble
    liste_lettre = list(mot)
    somme = 0
    for i in range(len(liste_lettre)):
        somme += dico[liste_lettre[i]]['val']
    return somme


def combo_mot_sur_plateau(plateau,i,j,mot,direction,dico):
    a,b = combi_or_not_combi(plateau,i,j,mot,direction) 
    somme = 0
    if a == []:
        return somme, False  
    for i in range(len(a)):
        if a[i] not in liste_mots_existant and b[i] not in liste_mots_existant: 
            return somme, False
        elif a[i] == b[i]: #palindrome 
            somme += point_mot_deja_pose(a[i],dico)
        elif a[i] in liste_mots_existant and b[i] not in liste_mots_existant:
            somme += point_mot_deja_pose(a[i],dico)
        elif b[i] in liste_mots_existant and a[i] not in liste_mots_existant:
            somme += point_mot_deja_pose(b[i],dico)
    return somme,True


def combi_or_not_combi(plateau,i,j,mot,direction): #MON BEBE. UN BIJOU DE TECHNOLOGIE
    haut = i
    bas = i
    gauche = j
    droite = j
    lettre_haut = []
    lettre_bas = []
    lettre_gauche = []
    lettre_droite = []
    lettre_haut_retourner = []
    lettre_bas_retourner  = []
    lettre_gauche_retourner  = []
    lettre_droite_retourner  = [] 
    liste_mot_haut = list(mot)     #on transforme ["lola"] en ['l','o','l','a'] dans ces listes ou on va injecter*
    liste_mot_bas = list(mot)       #*les lettres collectées dans les variables lettre_haut etc puis join les lettres*
    liste_mot_gauche = list(mot)   #*et regarder si ça forme un mot qui existe dans la liste des mots possibles 
    liste_mot_droite = list(mot) 
    liste_mot_totale = []
    liste_mot_totale_retourne = []
    extraction_temp = []
    variable_retourne = 0
    x = i
    for z in range(len(mot)):        
        if direction == "haut":
            while bas + 1 <= 14 and plateau[bas+1][j][0] != "  ":
                lettre_bas.append(plateau[bas+1][j][0])
                bas+=1
             
            while gauche-1 >= 0 and haut >= 0 and plateau[haut][gauche-1][0] != "  ":
                lettre_gauche.append(plateau[haut][gauche-1][0])
                gauche-=1
            while droite+1 <= 14 and haut >= 0 and plateau[haut][droite+1][0] != "  ":
                lettre_droite.append(plateau[haut][droite+1][0])
                droite+=1
            
            if z == len(mot) - 1:
                while x - 1 >= 0 and plateau[x-1][j][0] != "  ":
                    lettre_haut.append(plateau[x-1][j][0])
                    x -= 1

            if lettre_bas != [] or lettre_haut != []:
                if lettre_bas != [] and lettre_haut != []:
                    lettre_bas = retourne_lettre(lettre_bas)
                    lettre_bas.extend(liste_mot_haut)
                    lettre_bas.extend(lettre_haut)
                    lettre_bas = "".join(lettre_bas)
                    variable_retourne = "".join(retourne_lettre(lettre_bas))
                    liste_mot_totale.append(lettre_bas)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_bas != [] and lettre_haut == []:
                    lettre_bas = retourne_lettre(lettre_bas)
                    lettre_bas.extend(liste_mot_haut)
                    lettre_bas = "".join(lettre_bas)
                    variable_retourne = "".join(retourne_lettre(lettre_bas))
                    liste_mot_totale.append(lettre_bas)
                    liste_mot_totale_retourne.append(variable_retourne)

                elif lettre_haut != [] and lettre_bas == []:
                    liste_mot_haut.extend(lettre_haut)
                    liste_mot_haut = "".join(liste_mot_haut)
                    variable_retourne = "".join(retourne_lettre(liste_mot_haut))
                    liste_mot_totale.append(liste_mot_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    


            if lettre_gauche != [] or lettre_droite != []:
                if lettre_gauche != [] and lettre_droite != []:
                    lettre_gauche = retourne_lettre(lettre_gauche)
                    lettre_gauche.extend(liste_mot_gauche[z])
                    lettre_gauche.extend(lettre_droite)
                    lettre_gauche = "".join(lettre_gauche)
                    variable_retourne = "".join(retourne_lettre(lettre_gauche))
                    liste_mot_totale.append(lettre_gauche)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_gauche != [] and lettre_droite == []:
                    lettre_gauche = retourne_lettre(lettre_gauche)
                    lettre_gauche.extend(liste_mot_gauche[z])
                    lettre_gauche = "".join(lettre_gauche)
                    variable_retourne = "".join(retourne_lettre(lettre_gauche))
                    liste_mot_totale.append(lettre_gauche)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_droite != [] and lettre_gauche == []:
                    extraction_temp.append(liste_mot_droite[z])
                    extraction_temp.extend(lettre_droite)
                    liste_mot_droite = "".join(extraction_temp)
                    variable_retourne = "".join(retourne_lettre(liste_mot_droite))
                    liste_mot_totale.append(liste_mot_droite)
                    liste_mot_totale_retourne.append(variable_retourne)
            x -= 1
            haut -= 1
            extraction_temp = []
            gauche = j
            droite = j
            lettre_gauche = []
            lettre_droite = []  
            liste_mot_droite = list(mot)    #on reset pour la prochaine itération (tant que z in range len(mot) on veut qu'il teste*
            liste_mot_haut = list(mot)    #*a gauche et à droite à chaque fois pour direction haut

        if direction == "bas":
          
            while haut-1 >= 0 and plateau[haut-1][j][0] != "  ":
                lettre_haut.append(plateau[haut-1][j][0])
                haut-=1
               
            while gauche-1 >= 0 and bas <= 14 and plateau[bas][gauche-1][0] != "  ":
                lettre_gauche.append(plateau[bas][gauche-1][0])
                gauche-=1
            while droite+1 <= 14 and bas <= 14 and plateau[bas][droite+1][0] != "  ":
                lettre_droite.append(plateau[bas][droite+1][0])
                droite+=1
                
            if z == len(mot) - 1:
                while x + 1 <= 14 and plateau[x+1][j][0] != "  ":
                    lettre_bas.append(plateau[x+1][j][0])
                    x += 1

            if lettre_bas != [] or lettre_haut != []:
                if lettre_bas != [] and lettre_haut != []:
                    lettre_haut = retourne_lettre(lettre_haut)
                    lettre_haut.extend(liste_mot_haut)
                    lettre_haut.extend(lettre_bas)
                    lettre_haut = "".join(lettre_haut)
                    variable_retourne = "".join(retourne_lettre(lettre_haut))
                    liste_mot_totale.append(lettre_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_haut != [] and lettre_bas == []:
                    lettre_haut = retourne_lettre(lettre_haut)
                    lettre_haut.extend(liste_mot_haut)
                    lettre_haut = "".join(lettre_haut)
                    variable_retourne = "".join(retourne_lettre(lettre_haut))
                    liste_mot_totale.append(lettre_haut)
                    liste_mot_totale_retourne.append(variable_retourne)

                elif lettre_bas != [] and lettre_haut == []:
                    liste_mot_haut.extend(lettre_bas)
                    liste_mot_haut = "".join(liste_mot_haut)
                    variable_retourne = "".join(retourne_lettre(liste_mot_haut))
                    liste_mot_totale.append(liste_mot_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    


            if lettre_gauche != [] or lettre_droite != []:
                if lettre_gauche != [] and lettre_droite != []:
                    lettre_gauche = retourne_lettre(lettre_gauche)
                    lettre_gauche.extend(liste_mot_gauche[z])
                    lettre_gauche.extend(lettre_droite)
                    lettre_gauche = "".join(lettre_gauche)
                    variable_retourne = "".join(retourne_lettre(lettre_gauche))
                    liste_mot_totale.append(lettre_gauche)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_gauche != [] and lettre_droite == []:
                    lettre_gauche = retourne_lettre(lettre_gauche)
                    lettre_gauche.extend(liste_mot_gauche[z])
                    lettre_gauche = "".join(lettre_gauche)
                    variable_retourne = "".join(retourne_lettre(lettre_gauche))
                    liste_mot_totale.append(lettre_gauche)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_droite != [] and lettre_gauche == []:
                    extraction_temp.append(liste_mot_droite[z])
                    extraction_temp.extend(lettre_droite)
                    liste_mot_droite = "".join(extraction_temp)
                    variable_retourne = "".join(retourne_lettre(liste_mot_droite))
                    liste_mot_totale.append(liste_mot_droite)
                    liste_mot_totale_retourne.append(variable_retourne)
            x += 1
            bas += 1
            extraction_temp = []
            gauche = j
            droite = j
            lettre_gauche = []
            lettre_droite = []  
            liste_mot_droite = list(mot)    
            liste_mot_haut = list(mot)    

        if direction == "gauche":
            while droite + 1 <= 14 and plateau[i][droite+1][0] != "  ":
                lettre_droite.append(plateau[i][droite+1][0])
                droite+=1
               
            while haut-1 >= 0 and gauche >= 0 and plateau[haut-1][gauche][0] != "  ":
                lettre_haut.append(plateau[haut-1][gauche][0])
                haut-=1
            while bas+1 <= 14 and gauche >= 0 and plateau[bas+1][gauche][0] != "  ":
                lettre_bas.append(plateau[bas+1][gauche][0])
                bas+=1
                
            if z == len(mot) - 1:
                while x - 1 >= 0 and plateau[i][x-1][0] != "  ":
                    lettre_gauche.append(plateau[i][x-1][0])
                    x -= 1

            if lettre_gauche != [] or lettre_droite != []:
                if lettre_gauche != [] and lettre_droite != []:
                    lettre_droite = retourne_lettre(lettre_droite)
                    lettre_droite.extend(liste_mot_haut)#changer le nom + on en utilise que 2 list_mot_..
                    lettre_droite.extend(lettre_gauche)
                    lettre_droite = "".join(lettre_droite)
                    variable_retourne = "".join(retourne_lettre(lettre_droite))
                    liste_mot_totale.append(lettre_droite)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_droite != [] and lettre_gauche == []:
                    lettre_droite = retourne_lettre(lettre_droite)
                    lettre_droite.extend(liste_mot_haut)
                    lettre_droite = "".join(lettre_droite)
                    variable_retourne = "".join(retourne_lettre(lettre_droite))
                    liste_mot_totale.append(lettre_droite)
                    liste_mot_totale_retourne.append(variable_retourne)

                elif lettre_gauche != [] and lettre_droite == []:
                    liste_mot_haut.extend(lettre_gauche)
                    liste_mot_haut = "".join(liste_mot_haut)
                    variable_retourne = "".join(retourne_lettre(liste_mot_haut))
                    liste_mot_totale.append(liste_mot_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    


            if lettre_haut != [] or lettre_bas != []:
                if lettre_haut != [] and lettre_bas != []:
                    lettre_haut = retourne_lettre(lettre_haut)
                    lettre_haut.extend(liste_mot_gauche[z])
                    lettre_haut.extend(lettre_bas)
                    lettre_haut = "".join(lettre_haut)
                    variable_retourne = "".join(retourne_lettre(lettre_haut))
                    liste_mot_totale.append(lettre_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_haut != [] and lettre_bas == []:
                    lettre_haut = retourne_lettre(lettre_haut)
                    lettre_haut.extend(liste_mot_gauche[z])
                    lettre_haut = "".join(lettre_haut)
                    variable_retourne = "".join(retourne_lettre(lettre_haut))
                    liste_mot_totale.append(lettre_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_bas != [] and lettre_haut == []:
                    extraction_temp.append(liste_mot_droite[z])
                    extraction_temp.extend(lettre_bas)
                    liste_mot_droite = "".join(extraction_temp)
                    variable_retourne = "".join(retourne_lettre(liste_mot_droite))
                    liste_mot_totale.append(liste_mot_droite)
                    liste_mot_totale_retourne.append(variable_retourne)
            x -= 1
            gauche -= 1
            extraction_temp = []
            haut = i
            bas = i
            lettre_haut = []
            lettre_bas = []  
            liste_mot_droite = list(mot)    #on reset pour la prochaine itération (tant que z in range len(mot) on veut qu'il teste*
            liste_mot_haut = list(mot)    #*a gauche et à droite à chaque fois pour direction haut


        if direction == "droite":
            while gauche - 1 >= 0 and plateau[i][gauche-1][0] != "  ":
                lettre_gauche.append(plateau[i][gauche-1][0])
                gauche-=1
               
            while haut-1 >= 0 and droite <= 14 and plateau[haut-1][droite][0] != "  ": 
                lettre_haut.append(plateau[haut-1][droite][0])
                haut-=1
            while bas+1 <= 14 and droite <= 14 and plateau[bas+1][droite][0] != "  ":
                lettre_bas.append(plateau[bas+1][droite][0])
                bas+=1
                
            if z == len(mot) - 1:
                while x + 1 <= 14 and plateau[i][x+1][0] != "  ":
                    lettre_droite.append(plateau[i][x+1][0])
                    x += 1

            if lettre_gauche != [] or lettre_droite != []:
                if lettre_gauche != [] and lettre_droite != []:
                    lettre_gauche = retourne_lettre(lettre_gauche)
                    lettre_gauche.extend(liste_mot_haut)
                    lettre_gauche.extend(lettre_droite)
                    lettre_gauche = "".join(lettre_gauche)
                    variable_retourne = "".join(retourne_lettre(lettre_gauche))
                    liste_mot_totale.append(lettre_gauche)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_gauche != [] and lettre_droite == []:
                    lettre_gauche = retourne_lettre(lettre_gauche)
                    lettre_gauche.extend(liste_mot_haut)
                    lettre_gauche = "".join(lettre_gauche)
                    variable_retourne = "".join(retourne_lettre(lettre_gauche))
                    liste_mot_totale.append(lettre_gauche)
                    liste_mot_totale_retourne.append(variable_retourne)

                elif lettre_droite != [] and lettre_gauche == []:
                    liste_mot_haut.extend(lettre_droite)
                    liste_mot_haut = "".join(liste_mot_haut)
                    variable_retourne = "".join(retourne_lettre(liste_mot_haut))
                    liste_mot_totale.append(liste_mot_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    


            if lettre_haut != [] or lettre_bas != []:

                if lettre_haut != [] and lettre_bas != []:
                    lettre_haut = retourne_lettre(lettre_haut)
                    lettre_haut.extend(liste_mot_gauche[z])
                    lettre_haut.extend(lettre_bas)
                    lettre_haut = "".join(lettre_haut)
                    variable_retourne = "".join(retourne_lettre(lettre_haut))
                    liste_mot_totale.append(lettre_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                elif lettre_haut != [] and lettre_bas == []:

                    lettre_haut = retourne_lettre(lettre_haut)
                    lettre_haut.extend(liste_mot_gauche[z])
                    lettre_haut = "".join(lettre_haut)
                    variable_retourne = "".join(retourne_lettre(lettre_haut))
                    liste_mot_totale.append(lettre_haut)
                    liste_mot_totale_retourne.append(variable_retourne)
                    
                elif lettre_bas != [] and lettre_haut == []:
                    extraction_temp.append(liste_mot_droite[z])
                    extraction_temp.extend(lettre_bas)
                    liste_mot_droite = "".join(extraction_temp)
                    variable_retourne = "".join(retourne_lettre(liste_mot_droite))
                    liste_mot_totale.append(liste_mot_droite)
                    liste_mot_totale_retourne.append(variable_retourne)
            x += 1
            droite += 1
            extraction_temp = []
            haut = i
            bas = i
            lettre_haut = []
            lettre_bas = []  
            liste_mot_droite = list(mot)    #on reset pour la prochaine itération (tant que z in range len(mot) on veut qu'il teste*
            liste_mot_haut = list(mot)    #*a gauche et à droite à chaque fois pour direction haut
    #if mot in liste_mot_totale: 
        #liste_mot_totale.remove(mot)
        #liste_mot_totale.remove(retourne_lettre(mot))
    return liste_mot_totale,liste_mot_totale_retourne




def placer_mot(plateau,ll,mot,i,j,direction,dico):
    if '?' in ll:
        l = int(i)
        c = int(j)
        #test = tester_placement(plateau,l,c,direction,mot) 
        valeur_mot = list_valeur_mot(dico,mot)
        transition = 0
        multi_mot_bonus = 0        
        #a,b = combo_mot_sur_plateau(plateau,l,c,mot,direction,dico)
        z = 0
        #if test != []: #and b != False:
            #lettre_qui_remplace_joker = joker_enquiquinant()
        while z < len(mot):
            if mot[z] in ll and plateau[l][c][0] == "  ":                   
                if direction == "haut":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']: #On regarde si le tuple du plateau a un bonus dessus
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) # C'est égale à 2 ou à 3
                        transition = valeur_mot[z] * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " " #Faut peut être mettre une liste [" "] vide
                    elif plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                        #print(transition)
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    l-=1
                        
                elif direction == "bas":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']:
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) 
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " "
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    l+=1
                        
                        
                elif direction == "droite":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']: 
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) 
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " "
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    c+=1
                                        

                elif direction == "gauche":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']:
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) 
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " "
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    c-=1
                z += 1
            
            elif mot[z] not in ll and plateau[l][c][0] != "  ": 
                if '?' in ll:
                    if direction == "haut":
                        if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']: #On regarde si le tuple du plateau a un bonus dessus
                            valeur_mot[z] = 0
                            plateau[l][c][1] = " " #Faut peut être mettre une liste [" "] vide
                        if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                            multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                            plateau[l][c][1] = " "
                        plateau[l][c][0] = mot[z]
                        ll.remove('?')
                        l-=1
                            
                            
                    elif direction == "bas":
                        if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']:
                            valeur_mot[z] = 0
                            plateau[l][c][1] = " "
                        if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                            multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                            plateau[l][c][1] = " "
                        plateau[l][c][0] = mot[z]
                        ll.remove('?')
                        l+=1
                            
                            
                    elif direction == "droite":
                        if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']: 
                            valeur_mot[z] = 0
                            plateau[l][c][1] = " "
                        if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                            multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                            plateau[l][c][1] = " "
                        plateau[l][c][0] = mot[z]
                        ll.remove('?')
                        c+=1
                                            

                    elif direction == "gauche":
                        if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']:
                            valeur_mot[z] = 0
                            plateau[l][c][1] = " "
                        if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                            multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                            plateau[l][c][1] = " "
                        plateau[l][c][0] = mot[z]
                        ll.remove('?')
                        c-=1
                    z += 1
                else:
                    if direction == "haut":
                        l-=1
                    elif direction == "bas":
                        l+=1
                    elif direction == "droite":
                        c+=1
                    elif direction == "gauche":
                        c-=1
                    z+=1
            z+=1

        point_marque = calcule_liste_valeur_finale(valeur_mot)
        if multi_mot_bonus != 0:
            point_marque = point_marque * multi_mot_bonus
        #if a != []:
            #point_marque += a
            
        return point_marque
        
      


    else:
        l = int(i)
        c = int(j)
        #test = tester_placement(plateau,l,c,direction,mot) #liste des lettres à placer si le mot est plaçable sinon liste vide
        valeur_mot = list_valeur_mot(dico,mot) #liste des points que valent chaque lettre du mot sans l'additionner
        transition = 0  #pour pouvoir changer la valeur des points en fonction des bonus
        multi_mot_bonus = 0 #accumule la valeur avec laquelle on va multiplier les points totaux du mot
        #a,b = combo_mot_sur_plateau(plateau,l,c,mot,direction,dico) #tuple
        
        #if test != []: #and b != False: 
        for z in range(len(mot)):
            if mot[z] in ll and plateau[l][c][0] == "  ":
                if direction == "haut":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']: #On regarde si le tuple du plateau a un bonus dessus
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) # C'est égale à 2 ou à 3
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " " #Faut peut être mettre une liste [" "] vide
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    l-=1
                        
                        
                elif direction == "bas":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']:
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) 
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " "
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    l+=1
                        
                        
                elif direction == "droite":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']: 
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) 
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " "
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    c+=1
                                        

                elif direction == "gauche":
                    if plateau[l][c][1] == ['LT'] or plateau[l][c][1] == ['LD']:
                        chiffre_bonus = valeur_des_bonus(plateau[l][c][1]) 
                        transition = int(valeur_mot[z]) * chiffre_bonus
                        valeur_mot[z] = str(transition)
                        plateau[l][c][1] = " "
                    if plateau[l][c][1] == ['MT'] or plateau[l][c][1] == ['MD']:
                        multi_mot_bonus +=  valeur_des_bonus(plateau[l][c][1])
                        plateau[l][c][1] = " "
                    plateau[l][c][0] = mot[z]
                    ll.remove(mot[z])
                    c-=1
                

            else:
                if direction == "haut":
                    l-=1
                elif direction == "bas":
                    l+=1
                elif direction == "droite":
                    c+=1
                elif direction == "gauche":
                    c-=1
    

                
    point_marque = calcule_liste_valeur_finale(valeur_mot)
    if multi_mot_bonus != 0:
        point_marque = point_marque * multi_mot_bonus
        #if a != []:
            #point_marque += a
    print("Succès du placement")
    return point_marque 





def dico_joueur(liste):
    dico_joueur = {}
    for key in liste:
        dico_joueur[key] = {"main" : 0, "point" : 0}
    return dico_joueur
    


def verif_lettre(mot):
    mot_majus = []
    for i in range(len(mot)):
        if 'a' <= mot[i] <= 'z' or 'A' <= mot[i] <= 'Z' or mot[i] == '?':
            mot_majus.append(mot[i].upper())
        else:
            mot_majus = []
            return mot_majus
    return mot_majus
 
    """for j in range(len(mot_majus)):
        if mot_majus[j] not in dico_joueurs[nom_joueur]["main"]:
            print("Vous n'avez pas cette lettre dans votre main")
            print("aaaa")
            return []
    for k in range(len(mot_majus)):
        print(mot_majus2)
        print(mot_majus[k])
        if mot_majus[k] not in mot_majus2:
            print("Il vous manque des lettres dans votre main")
            print("bbbbb")
            return []
        mot_majus2.remove(mot_majus[k])
    if mot_majus2 != []:
        print("Il vous manque des lettres dans votre main")
        print("cccc")
        return []
    for l in range(len(mot_majus)):
        if mot_majus[l] not in copie_main:
            return []
        copie_main.remove(mot_majus[l])
    print(mot_majus)
    return mot_majus"""
        


def test_placement_premier_mot(mot,i,j,direction):
    for z in range(len(mot)):
        if direction == "haut":
            if i == 7 and j == 7:
                return True
            else:
                i-=1
        if direction == "bas":
            if i == 7 and j == 7:
                return True
            else:
                i+=1
        if direction == "gauche":
            if i == 7 and j == 7:
                return True
            else:
                j-=1
        if direction == "droite":
            if i == 7 and j == 7:
                return True
            else:
                j+=1
    return False 
    
def echanger_verif(jetons,main):
    jetons_copie = copy.deepcopy(jetons)
    main_copie =copy.deepcopy(main)
    nb_echange = len(jetons_copie) 
    i = 0
    while i < len(jetons_copie):
        if jetons == [] or jetons_copie[i] not in main_copie:
            return False
        main_copie.remove(jetons_copie[i])     
        i+=1
    return True                


def enleve_lettre_test_placement_a_main_joueur(ll,main):
    for i in range(len(ll)):
       main.remove(ll[i])
       




def tour_joueur():#en construction 
    liste_mots_jouables = []
    premier_tr = premier_t[0]
    #print(premier_t)
    #print("premier_tr =",premier_tr)
    test_placement_V2 = []      
    rep = None #La classe quoi  
    if nom_joueur != "Bob le bot": #La fonction va agir autrement si c'est l'IA ou un humain
        print("Au tour de",nom_joueur,"de jouer")        
        print()
        print("votre main est: ",dico_joueurs[nom_joueur]["main"])#dico -> nom du joueur -> main
        rep = None #La classe quoi
        z = 0
        while z == 0:#Boucle infini velontaire, on sortira avec un return
            if rep != 'echanger' and rep != 'placer':
                print("\"echanger\" pour échanger une ou plusieurs lettre(s) avec d'autre(s) \n \"placer\" pour essayer de placer un mot \n \"passer\" pour passer le tour \n \n Action à faire :",end="")
                rep = input()
            if rep == "passer":
                print(nom_joueur,"à passé son tour")
                return print("Fin du tour de",nom_joueur) #Sortie par passer
            if rep == 'echanger':
                verif_echange = False

                #a_echanger = input("Lettres à échanger :")
                #a_echanger = verif_lettre(a_echanger)
                a_echanger = input("Lettres à échanger: ")
                a_echanger = a_echanger.upper()
                #print(a_echanger,"avant")
                
                while not echanger_verif(a_echanger,dico_joueurs[nom_joueur]["main"]):
                    print("Regardez bien votre main:",dico_joueurs[nom_joueur]["main"])
                    a_echanger = input("Lettres à échanger: ")
                    a_echanger = a_echanger.upper()
                    #a_echanger = verif_lettre(a_echanger)
                    #print("a_echanger",a_echanger)
                #print("a_echanger",a_echanger)
                #print(dico_joueurs[nom_joueur]["main"],"avant")
                echanger(a_echanger,dico_joueurs[nom_joueur]["main"],sac_de_lettre)#J'espère que la fonction vérifie qu'il peut échanger ses lettres
                #print(a_echanger,"apres")
                #print(dico_joueurs[nom_joueur]["main"],"apres")
                return print("Fin du tour de",nom_joueur) #sortie par echanger
            elif rep == "placer":
                if premier_tr: #premier tour test si il y a des lettres sur le plateau. Si c'est négatif c'est donc qu'aucun mot n'est posé sur le plateau
                    verif_nomvariable = False
                    mot = ""
                    while premier_tr and len(mot) < 2 or not mot in liste_mots_existant:
                        if verif_nomvariable:
                            print("tapez \"!!!\" pour passer votre tour")
                        verif_nomvariable = True
                        print("Le premier mot posé doit impérativement recouvrir la case (7,7) et être composé au minimum de deux lettres")
                        mot = input("Mot à placer: ")
                        if mot == "!!!":
                            return print("Fin du tour de",nom_joueur)
                        mot = mot.upper()
                        #while len(mot) < 2 or not mot_jouable(mot,ll): #le mot doit au moins contenir deux lettres
                            #mot = input("Mot à placer : ")
                            #mot = mot.upper()
                        direction = None    
                        while direction != "haut" and direction != "bas" and direction != "gauche" and direction != "droite":#DES AND PAS DES OR ICI
                            direction = input("choisir une direction \"haut\" / \"bas\" / \"droite\" / \"gauche\" \n Direction choisie : ") 
                        i,j = lire_coords()
                        
                        test_placement = test_placement_premier_mot(mot,i,j,direction)
                        #test_placement = test_placement_premier_mot(mot,i,j,direction)
                    #placer_mot(plateau,dico_joueurs[nom_joueur]["main"],mot,i,j,direction,dico_valeur)
                    test_placement_V2 = tester_placement(plateau,i,j,direction,mot,dico_joueurs[nom_joueur]["main"])
                    enleve_lettre_test_placement_a_main_joueur(test_placement_V2,dico_joueurs[nom_joueur]["main"])
                    point_marque = placer_mot(plateau,test_placement_V2,mot,i,j,direction,dico_valeur) #Si c'est le cas, on arrive ici, reste plus qu'a placer le mot sur le vrai plateau
                    affiche_jeton(plateau) #on affiche le plateau                        
                    completer_main(dico_joueurs[nom_joueur]["main"],sac_de_lettre) #on complete sa main
                    dico_joueurs[nom_joueur]["point"] += point_marque #on met à jour les points
                    premier_t[0] = False
                    return print("Fin du tour de",nom_joueur)


                else:
                    a = 0
                    b = False
                    test_placement = []
                    mot = ""
                    verif_boucle = False
                    while b == False:
                        while test_placement == [] or not mot in liste_mots_existant or b == False:
                            if verif_boucle:
                                print(mot,"ne fait pas partie de la liste des mots autorisé, taper \"!!!\" si vous voulez quitter ce menu")
                            print("Le mot posé doit être composé au minimum de deux lettres")
                            verif_boucle = True
                            
                            #print(mots_jouables(liste_mots_existant,dico_joueurs[nom_joueur]["main"])) #pour les tests

                            print("Entrez \"@\" pour avoir une suggestion de mot")
                            mot = input("Mot à placer : ")
                            if mot == "@":
                                if mots_jouables(liste_mots_existant,dico_joueurs[nom_joueur]["main"]) == []:
                                    print("Vous ne pouvez pas placer de mot avec votre main seule, peut-être avec les lettres sur plateau...")
                                else:
                                    suggestion = random.choice(mots_jouables(liste_mots_existant,dico_joueurs[nom_joueur]["main"]))
                                    print("Aide:",suggestion)
                                mot = input("Mot à placer : ")
                                
                                
                                
                            if mot == "!!!" :
                                rep = None
                                while rep != "echanger" and rep != "passer":
                                    print("\"echanger\" pour échanger une ou plusieurs lettre(s) avec d'autre(s) \n \"passer\" pour passer le tour \n Action à faire: ",end="")
                                    rep = input()
                                if rep == "passer":
                                    print(nom_joueur,"à passé son tour")
                                    return print("Fin du tour de",nom_joueur) #Sortie par passer
                                if rep == 'echanger':
                                    verif_echange = False
                                    a_echanger = input("Lettres à échanger: ")
                                    a_echanger = a_echanger.upper()
                                    
                                    while not echanger_verif(a_echanger,dico_joueurs[nom_joueur]["main"]):
                                        print("Regardez bien votre main :",dico_joueurs[nom_joueur]["main"])
                                        a_echanger = input("Lettres à échanger :")
                                        a_echanger = a_echanger.upper()
                                    echanger(a_echanger,dico_joueurs[nom_joueur]["main"],sac_de_lettre)
                                    return print("Fin du tour de",nom_joueur) #sortie par echanger
                                
                            mot = mot.upper()                 
                            direction = None
                            verif_boucle2 = False
                            #verif_boucle2 = False
                            while direction != "haut" and direction != "bas" and direction != "gauche" and direction != "droite":
                                if verif_boucle2:
                                      print("Entrez \"!!!\" dans la direction pour sortir de ce menu")
                                verif_boucle2 = True
                                      
                                direction = input("choisir une direction \"haut\" / \"bas\" / \"droite\" / \"gauche\" \n Direction choisie: ")
                                if direction == "!!!":
                                    rep = None
                                    while rep != "echanger" and rep != "passer":
                                        print("\"echanger\" pour échanger une ou plusieurs lettre(s) avec d'autre(s) \n \"passer\" pour passer le tour \n Action à faire:",end="")
                                        rep = input()
                                    if rep == "passer":
                                        print(nom_joueur,"à passé son tour")
                                        return print("Fin du tour de",nom_joueur) #Sortie par passer
                                    if rep == 'echanger':
                                        verif_echange = False
                                        a_echanger = input("Lettres à échanger: ")
                                        a_echanger = a_echanger.upper()
                                        
                                        while not echanger_verif(a_echanger,dico_joueurs[nom_joueur]["main"]):
                                            print("Regardez bien votre main:",dico_joueurs[nom_joueur]["main"])
                                            a_echanger = input("Lettres à échanger :")
                                            a_echanger = a_echanger.upper()
                                        echanger(a_echanger,dico_joueurs[nom_joueur]["main"],sac_de_lettre)
                                        return print("Fin du tour de",nom_joueur) #sortie par echanger
                                                      
                            i,j = lire_coords()
                            test_placement = tester_placement(plateau,i,j,direction,mot,dico_joueurs[nom_joueur]["main"])
                            a,b = combo_mot_sur_plateau(plateau,i,j,mot,direction,dico_valeur)
                            
                        #point_marque = placer_mot(plateau,dico_joueurs[nom_joueur]["main"],mot,i,j,direction,dico_valeur) #A CHANCHER METTRE
                        #if a != 0:
                    
                        enleve_lettre_test_placement_a_main_joueur(test_placement,dico_joueurs[nom_joueur]["main"])
                        print(dico_joueurs[nom_joueur]["main"],"apres enlever main")
                        point_marque = placer_mot(plateau,test_placement,mot,i,j,direction,dico_valeur)
                        point_marque += a
                        print([nom_joueur],"à marqué",point_marque,"points !")
                        completer_main(dico_joueurs[nom_joueur]["main"],sac_de_lettre)
                        dico_joueurs[nom_joueur]["point"] += point_marque
                        affiche_jeton(plateau)
                        return print("Fin du tour de",nom_joueur) #Sortie par placer
                        #suite de placer si raté
                      
    else:#tour de Bob le bot
        liste_mots_jouables = []
        print("Au tour de",nom_joueur,"de jouer")
        print("La main de Bob le bot est : ",dico_joueurs[nom_joueur]["main"])#dico -> nom du joueur -> main
        liste_mots_jouables.extend(mots_jouables(liste_mots_existant, dico_joueurs[nom_joueur]["main"])) #le bot a une liste des mots qu'il peut jouer avec ses lettres
        #print(liste_mots_jouables)
        direction_1 = ['haut','bas','droite','gauche']
        incrementeur_direction  = 0
        test_placement = []
        test_placement_premier = False
        premier_tour = premier_t[0]
        #print(1)
        if premier_tour:
            print("1er tour")
            rand_direction = random.choice(direction_1)
            #print(rand_direction)
            rand_mot = random.choice(liste_mots_jouables)
            #print(rand_mot)
            ligne = 0
            while ligne < 15 and test_placement_premier == False:
                colonne = 0
                while colonne < 15 and test_placement_premier == False:
                    test_placement_premier = test_placement_premier_mot(rand_mot,ligne,colonne,rand_direction)
                    colonne += 1
                    #print(test_placement_premier)
                ligne += 1
            point_marque = placer_mot(plateau,dico_joueurs[nom_joueur]["main"],rand_mot,ligne,colonne,rand_direction,dico_valeur)
            print([nom_joueur],"à marqué",point_marque,"points !")
            completer_main(dico_joueurs[nom_joueur]["main"],sac_de_lettre)
            dico_joueurs[nom_joueur]["point"] += point_marque
            premier_t[0] = False
            affiche_jeton(plateau)                        
            return print("Fin du tour de",nom_joueur)            
                
        else:
            print("lesautrestour")
            while incrementeur_direction  < len(direction_1): #il va tester pour chacune des directions
                #print(direction_1[incrementeur_direction])
                incrementeur_mots_jouables = 0
                while incrementeur_mots_jouables < len(liste_mots_jouables): #pour chacun des mots jouables de la liste crée à partir des lettres de sa main
                    #print(incrementeur_mots_jouables,'m')
                    mot = liste_mots_jouables[incrementeur_mots_jouables]
                    incrementeur_ligne = 0
                    while incrementeur_ligne < 15: #pour les coordonées en i de chacune des lignes
                        #print(incrementeur_ligne,"l")
                        incrementeur_colonne = 0
                        while incrementeur_colonne < 15: #pour les coordonées en j de chacune des colonnes de chachune des lignes
                                #print(incrementeur_colonne,"c")
                                 #Si tu veux utiliser des f,g pour i,j fait le jusqu'au bout
                            
                            test_placement = tester_placement(plateau,incrementeur_ligne,incrementeur_colonne,direction_1[incrementeur_direction],mot,dico_joueurs[nom_joueur]["main"])
                            #print(test_placement)
                            a,b = combo_mot_sur_plateau(plateau,incrementeur_ligne,incrementeur_colonne,mot,direction_1[incrementeur_direction],dico_valeur)
                             
                            if b == True and test_placement != []: # si point_marqué n'est pas nul alors c'est qu'il peut poser le mot
                                enleve_lettre_test_placement_a_main_joueur(test_placement,dico_joueurs[nom_joueur]["main"])
                                point_marque = placer_mot(plateau,test_placement,liste_mots_jouables[incrementeur_mots_jouables],incrementeur_ligne,incrementeur_colonne,direction_1[incrementeur_direction],dico_valeur)
                                point_marque += a
                                print([nom_joueur],"à marqué",point_marque,"points !")
                                completer_main(dico_joueurs[nom_joueur]["main"],sac_de_lettre)
                                dico_joueurs[nom_joueur]["point"] += point_marque
                                affiche_jeton(plateau)
                                return print("Fin du tour de",nom_joueur)
                            else:
                                incrementeur_colonne += 1
                        incrementeur_ligne += 1
                    incrementeur_mots_jouables +=1      #incrémenteur qui parcours la liste des mots jouables
                incrementeur_direction +=1
                
            #si il ne trouve rien à poser, il rand au pif un nombre, echange au pif le nombre de lettre et ça termine son tour
            nb_lettre_echange = random.randint(1,7) 
            lettre_a_echanger = random.sample(dico_joueurs[nom_joueur]["main"],nb_lettre_echange)
            echanger(lettre_a_echanger,dico_joueurs[nom_joueur]["main"],sac_de_lettre)
            return print("Le bot echange ses lettres")




def fin_de_partie():
    print("\n \n \n \n")
    score = []
    for i in range(len(liste_joueurs)):
        nom_joueur_temp = liste_joueurs[i]
        score.append((dico_joueurs[nom_joueur_temp]["point"]))
    i=0
    position_score_max = 0
    score_max = -10000
    score_min = 4187 #record du score le plus grand au scrabble
    position_score_min = 0

    for i in range(len(liste_joueurs)): #MALUS
        nom_joueur_temp = liste_joueurs[i]
        score_a_deduire = 0
        mot = "".join(dico_joueurs[nom_joueur_temp]["main"]) #join toutes les lettres restante dans la main
        a_additionner = list_valeur_mot(dico_valeur,mot) #reçoit une liste de points
        malus = 0
        aze = 0
        for aze in range(len(a_additionner)):
            malus += a_additionner[aze]
        print("\t \t \t",nom_joueur_temp,"se prend un malus de",malus,"points",end="")
        if malus > 10:
            print(" Ouch,coup dur...")
        print()
        dico_joueurs[nom_joueur_temp]["point"] -= malus

    for i in range(len(liste_joueurs)):
        if score[i] > score_max:
            score_max = score[i]
            position_score_max = i
        if score[i] < score_min:
            score_min = score[i]
            position_score_min = i
    print('\n')
    print("\t \t \t Le gagnant est :",liste_joueurs[position_score_max].upper())
    #Mettre un écran de victoire avec un module
    print("\t \t \t Le grand perdant est :",liste_joueurs[position_score_min])
    print()
    i=0
    
    i=0
    for i in range(len(liste_joueurs)):
        nom_joueur_temp = liste_joueurs[i]
        print("\t \t \t Score du joueur",nom_joueur_temp,":",dico_joueurs[nom_joueur_temp]["point"])
    
    


def ini_petit_dico(): #Dico plus petit pour faire des tests
    dictionnaire = {
                    'A' : {'occ' : 3, 'val' : 1},
                     'B' : {'occ' : 1, 'val' : 3},
                      'C' : {'occ' : 1, 'val' : 3},
                       'D' : {'occ' : 2, 'val' : 2},
                        'E' : {'occ' : 7, 'val' : 1},
                         'F' : {'occ' : 1, 'val' : 4},
                          'G' : {'occ' : 1, 'val' : 2},
                           'H' : {'occ' : 1, 'val' : 4},
                            'I' : {'occ' : 1, 'val' : 1},
                             'J' : {'occ' : 1, 'val' : 8},
                              'K' : {'occ' : 1, 'val' : 10},
                               'L' : {'occ' : 2, 'val' : 1},
                                'M' : {'occ' : 1, 'val' : 2},
                                 'N' : {'occ' : 3, 'val' : 1},
                                  'O' : {'occ' : 3, 'val' : 1},
                                   'P' : {'occ' : 1, 'val' : 3},
                                    'Q' : {'occ' : 0, 'val' : 8},
                                     'R' : {'occ' : 3, 'val' : 1},
                                      'S' : {'occ' : 3, 'val' : 1},
                                       'T' : {'occ' : 3, 'val' : 1},
                                        'U' : {'occ' : 3, 'val' : 1},
                                         'V' : {'occ' : 1, 'val' : 4},
                                          'W' : {'occ' : 0, 'val' : 10},
                                           'X' : {'occ' : 0, 'val': 10},
                                            'Y' : {'occ' : 0, 'val' : 10},
                                             'Z' : {'occ' : 0, 'val' : 10},
                                              '?' : {'occ' : 4, 'val' : 0},

                                            }
    return dictionnaire





##////////////////////////// PROG PRINCIPAL ///////////////////////////////////


#############################
bonus = init_bonus() 
jeton = init_jeton() 
plateau = combine_bonus_jeton(jeton,bonus)
liste_mots_existant = genere_dico('liste_mots_existant.txt')
dico_valeur = ini_dico()
sac_de_lettre = ini_pioche(dico_valeur)
copie_du_plateau_vide = copy.deepcopy(plateau)


verif = False
while not verif:#J'ai du faire des boucles pour pas que l'utilisateur casse tout
    print("Nombre de joueurs maximum : 4. Vous pouvez ajouter un bot dans la limite des 4 joueurs")
    IA = input("Voulez-vous jouer avec une IA ? y/n :")
    if IA != "y" and IA != "n":
        print("Je n'ai pas bien compris, tapez \"y\" pour oui ou \"n\" pour non")
    else:
        if IA == "y":
            IA = True
        elif IA == "n":
            IA = False
        verif = True

    
verif = False

while not verif:

    pazunnombre = True
    premier_passage_dans_boucle = True
    while pazunnombre:
        if not premier_passage_dans_boucle:
            print("Entrez un nombre de joueur correct entre 1 et 4")
        premier_passage_dans_boucle = False
        nb_joueurs = input("Entrez un nombre de joueur(s) humain :")
        if nb_joueurs in ["0","1","2","3","4"]:
            pazunnombre = False
            nb_joueurs = int(nb_joueurs)
    if nb_joueurs > 3 and IA:
        print("Nombre de joueurs maximum dépassé. Veuillez entrer un nombre compris entre 1 et 3",end="")
        input()
    else:
        nb_joueurs = int(nb_joueurs)
    if nb_joueurs > 4 and not IA:
        print("Nombre de joueurs maximum dépassé. Veuillez entrer un nombre compris entre 1 et 4",end="")
        input()
    else:
        nb_joueurs = int(nb_joueurs) 
    if IA:
        nb_joueurs +=1
    if nb_joueurs < 2:
        print("Vous allez vous sentir seul, trouvez des amis avec qui jouer :)")
    else:
        verif = True



#nb_joueurs -> nombre de joueurs
#liste_joueurs -> liste avec le noms des joueurs dans l'ordre, si il y a une IA elle sera en dernier et se nommera "Bob le bot"
#IA -> booléen pour check si il y a une IA

liste_joueurs = []
temp = nb_joueurs
if IA:
    temp -= 1

verif = False
while not verif:
    i=0
    while i < temp:
        print("Nom du joueur n°",i,":",end="")
        variable_tres_temporaire = input()
        liste_joueurs.append(variable_tres_temporaire)
        i+=1
        
    verif2 = False
    
    while not verif2:
        print("Confirmer la liste des joueurs humain?\n",liste_joueurs,"\n y=oui / n=non :",end="")
        temp2 = input()
        if temp2 != "y" and temp2 != "n":
            print("Je n'ai pas bien compris, tapez \"y\" pour oui ou \"n\" pour non")
        if temp2 == "y":
            verif2 = True
            verif = True
        if temp2 == "n":#retour au début de la boucle
            verif2 = True
            liste_joueurs = []
    
if IA:
    liste_joueurs.append("Bob le bot")
i=0
#print("liste joueur:",liste_joueurs)


dico_joueurs = dict()
while i < len(liste_joueurs):
    dico_joueurs[liste_joueurs[i]] = {'main' : [], 'point' : 0}
    completer_main(dico_joueurs[liste_joueurs[i]]["main"],sac_de_lettre)
    i+=1
    #print(dico_joueurs)



i=0

num_joueur = 0

def joueur_suivant(num_joueur):
    num_joueur +=1
    if num_joueur == len(liste_joueurs):
        num_joueur = 0
    suivant = liste_joueurs[num_joueur]
    return suivant,num_joueur


nom_joueur = liste_joueurs[num_joueur]
premier_t = [True] #Liste pour profité de l'effet de bord
print("Liste des signes sur le plateau : \n ~ = Mot triple \n ° = Mot double \n * = Lettre triple \n ^ = Lettre double")


##////////////////////////// BOUCLE DE JEU ///////////////////////////////////

y = 0
trop_echange = 0
#sac_de_lettre = [] #Fin de partie instantané
affiche_jeton(plateau)
while sac_de_lettre != [] or trop_echange > 50: #sac_de_lettre est la liste où on pioche
    #print(sac_de_lettre) #A désactiver pour soutenance
    y = tour_joueur()
    if y == False:
       trop_echange = 0
    if y == True:
       trop_echange += 1
    print("Score de",nom_joueur,":",dico_joueurs[nom_joueur]["point"])
    print("---------------------------------------------------------------------------------------------------")
    

    nom_joueur,i = joueur_suivant(num_joueur)#bot joue tout seul
    #nom_joueur,num_joueur = joueur_suivant(num_joueur)#jeu normal


#dico_joueurs[nom_joueur]["point"] = 25
#dico_joueurs[joueur_suivant(num_joueur)]["point"] = 250


fin_de_partie()










#CIMETIERE DE FONCTION

def ini_pioche(dico):
    pioche = []
    for i in range (0,dico['A']['occ']):
        pioche.append('A')
    for i in range (0,dico['B']['occ']):
        pioche.append('B')
    for i in range (0,dico['C']['occ']):
        pioche.append('C')
    for i in range (0,dico['D']['occ']):
        pioche.append('D')
    for i in range (0,dico['E']['occ']):
        pioche.append('E')
    for i in range (0,dico['F']['occ']):
        pioche.append('F')
    for i in range (0,dico['G']['occ']):
        pioche.append('G')
    for i in range (0,dico['H']['occ']):
        pioche.append('H')
    for i in range (0,dico['I']['occ']):
        pioche.append('I')
    for i in range (0,dico['J']['occ']):
        pioche.append('J')
    for i in range (0,dico['K']['occ']):
        pioche.append('K')
    for i in range (0,dico['L']['occ']):
        pioche.append('L')
    for i in range (0,dico['M']['occ']):
        pioche.append('M')
    for i in range (0,dico['N']['occ']):
        pioche.append('N')
    for i in range (0,dico['O']['occ']):
        pioche.append('O')
    for i in range (0,dico['P']['occ']):
        pioche.append('P')
    for i in range (0,dico['Q']['occ']):
        pioche.append('Q')
    for i in range (0,dico['R']['occ']):
        pioche.append('R')
    for i in range (0,dico['S']['occ']):
        pioche.append('S')
    for i in range (0,dico['T']['occ']):
        pioche.append('T')
    for i in range (0,dico['U']['occ']):
        pioche.append('U')
    for i in range (0,dico['V']['occ']):
        pioche.append('V')
    for i in range (0,dico['W']['occ']):
        pioche.append('W')
    for i in range (0,dico['X']['occ']):
        pioche.append('X')
    for i in range (0,dico['Y']['occ']):
        pioche.append('Y')
    for i in range (0,dico['Z']['occ']):
        pioche.append('Z')
    for i in range (0,dico['?']['occ']):
        pioche.append('?')

    return pioche




def lire_coords(): #FONCTIONNE
    vide = False
    premiere_demande = True
    coordonnees = []
    while not vide:
        if not premiere_demande:
            print("/!\ Case non vide ! ")
        print("Ligne n° ? (entre 0 et 14) : ",end="")
        ligne = int(input())
        print("Colonne n° ? (entre 0 et 14) : ",end="")
        colonne = int(input())
        premiere_demande = False
        if jetons[ligne][colonne] == [""]:
            vide = True
    coordonnees.append(ligne)
    coordonnees.append(colonne)
    return coordonnees #si besoin de return une liste


#POUR TEST
#coord = lire_coords()
#i = coord[0]
#j = coord[1]'''




def joker_enquiquinant(mot,ll):
    a = list(mot)           #ELLE MARCHE
    b = copy.copy(ll)
    i = 0
    while i < len(mot):
        if mot[i] in b:
            a.remove(mot[i])
            b.remove(mot[i])
        i+=1
    return a      



def premier_tour(plateau,copie_du_plateau_vide):
    if plateau != copie_du_plateau_vide:
        return False
    return True



