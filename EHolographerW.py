
import Constellation
import os 

#%%______________________________________________________________________________
# Procedure permettant d'afficher une image ou une video sous windows
def callWMplayer(chemin):
    """ procedure qui lance Windows Media Player en plein ecran
        parametre chemin vers l'image ou la video
    """

    """  'CALL' est une instruction windows qui lanc    e un programme
         le premier chemin est celui vers windows media player
         le second est le chemin variable vers le fichier a ouvrir    
    """
    os.system('CALL "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe" /fullscreen '+chemin)
 

# Message Callback creant un fichier d'index sur le bureau
@Constellation.MessageCallback()
def InitialisationIndex():
    
    #change le chemin actuel pour aller sur le bureau
    os.chdir(os.path.expanduser('~')+'\\Desktop')
    #creer le fichier d'index
    fichier = open('Index.txt','w')
    #ecrit les consignes dans le fichier
    fichier.write('Veuillez ecrire les ligne de la forme "Alias" "Chemin" ')
    fichier.close()

#Meassage Callback qui ajoute un element a l'index
@Constellation.MessageCallback()
def AjoutElementIndex(Alias ,Path):
    """Procedure ajoutant un element a l'index
        Parametre : 1 string = le nom avec lequel on veut appeler l'element
                    1 string = le chemin vers l'element
    """

    #change le repertoire de travail pour le bureau
    os.chdir(os.path.expanduser('~')+'\\Desktop')
    #ouvre le fichier d'index en mode ajouter du texte
    fichier = open('Index.txt','a')
    # écrit un retour a la ligne puis les caracteristique de l'element
    fichier.write("\n" + Alias + " " + Path)
    fichier.close()


#Message Callback lançant une video
@Constellation.MessageCallback()
def showVideo(Alias):
    """ procedure pour lancer une video
        parametre : 1 string = le nom que l'on a definis pour l'element
    """
    
    #change le repertoire de travail pour le Bureau
    os.chdir(os.path.expanduser('~')+'\\Desktop')
    #ouvre le fichier d'index en mode lecture
    fichier = open('Index.txt','r')

    #recherche de l'alias dans le fichier
    contenu = fichier.readlines()
    nombreLigne = len(contenu)
    i = 0
    while (i < (nombreLigne - 1)):
        i = i + 1
        Ligne = contenu[i]
        Separe = Ligne.split()
        if Alias == Separe[0]:
            #lance la video par windows media player
            callWMplayer(Separe[1])
            break

    fichier.close()
   


def OnExit():
    pass

def OnStart():
    # Register callback on package shutdown
    Constellation.OnExitCallback = OnExit   
   
    # Last StateObjects of the previous instance
    if Constellation.LastStateObjects:
        for so in Constellation.LastStateObjects:
            Constellation.WriteInfo(" + %s @ %s" % (so.Name, so.LastUpdate))

Constellation.Start(OnStart);