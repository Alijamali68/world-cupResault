from collections import OrderedDict

#TODO: this will hold the Teams points and etc
Games={
'Iran':{'wins':0,'loses':0,'draws':0,'goal difference':0,'points':0},
'Spain':{'wins':0,'loses':0,'draws':0,'goal difference':0,'points':0},
'Portugal':{'wins':0,'loses':0,'draws':0,'goal difference':0,'points':0},
'Morocco':{'wins':0,'loses':0,'draws':0,'goal difference':0,'points':0}
}

#TODO: this will return the game sequence
def Gamesequence():
    yield 'Iran Spain'
    yield 'Iran Portugal'
    yield 'Iran Morocco'
    yield 'Spain Portugal'
    yield 'Spain Morocco' 
    yield 'Portugal Morocco'



#TODO: this will  call and calculate the point of the  teams with every entry
def SetWins(Gamesequence,gameresault):
    # 'Iran Spain'
    Gamesequence=Gamesequence.split()
    #i.e :2-2
    GameResault=gameresault.split('-')
    if(GameResault[0]==GameResault[1]):
        Games[Gamesequence[0]]['draws']+=1
        Games[Gamesequence[1]]['draws']+=1
    elif(GameResault[0]>GameResault[1]):
        Games[Gamesequence[0]]['wins']+=1
        Games[Gamesequence[1]]['loses']+=1
        Games[Gamesequence[0]]['goal difference']+=((int(GameResault[0]))-(int(GameResault[1])))
        Games[Gamesequence[1]]['goal difference']+=((int(GameResault[1]))-(int(GameResault[0])))
    elif(GameResault[0]<GameResault[1]):
        Games[Gamesequence[0]]['loses']+=1
        Games[Gamesequence[1]]['wins']+=1	
        Games[Gamesequence[0]]['goal difference']+=((int(GameResault[0]))-(int(GameResault[1])))
        Games[Gamesequence[1]]['goal difference']+=((int(GameResault[1]))-(int(GameResault[0])))



#TODO:this will calculate the Teams At the end     
def Calculatepoint():
    for perteam in Games:
        Games[perteam]['points']=((Games[perteam]['wins'])*3)+((Games[perteam]['draws'])*1)
    SortResault()    

#TODO: this will sort the resault
def SortResault():
    Gamesres=OrderedDict(sorted(Games.items(), key=lambda item: item[1]['points'],reverse=True))
    PrintResault(Gamesres)
def PrintResault(Gamesres):
    #temp will hold the teams Apearance i.e: wins loses etc 
    temp=''
    #this will add comma to seperate item exept last item 
    counter=1
    for everyteam in Gamesres:
        for i in Gamesres[everyteam].items():
            if(counter<5):
                temp+=str(i[0])+':'+str(i[1])+', '
                counter+=1
            else:
                temp+=str(i[0])+':'+str(i[1])
        print(everyteam,temp)
        temp=''
        counter=1
        
        
for i in Gamesequence():
    #i.e 'Iran spain,2-2'
    SetWins(i,input())
    
Calculatepoint()
