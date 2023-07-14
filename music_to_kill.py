import random
import musicpy as mp
import os


list_of_note_type = ["C","D","E","F","G","A","B","C#","D#","E#","F#","G#","A#","B#"]

dictionnaire = {"bois":[23,69,70,71,72,73,74,75,76,77,78,79,80,112],
                "clavier":[1,2,3,4,5,6,7,9,17,18,19,20,21,109],
                "corde":[25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,49,50,51,52,105,106,107,108,111],
                "cuivre":[57,58,59,60,61,62,63,64,65,66,67,68,110],
                "percussions":[10,12,13,14,15,16,48,115,117,119,120],
                "divers":[122,123,124,125,126,127,128,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,24,22,11],
                "voice":[53,54,55,56]
                }
value_dictionnaire =["bois","clavier","corde","cuivre","percussions","divers","voice"]


max = 7 #le max qu'une note peut avoir dans cette piece, le max réel est 9 mais c'est une trop haute fréquence (16000 Hzmin +21k Hz max)

def Generate_chore(number_of_note:int,max:int,number_of_repetion:int):
    list_of_note = []
    note_choosen = list_of_note_type[random.randint(0,len(list_of_note_type) - 1)]
    for i in range(number_of_note):
        list_of_note.append(mp.note(note_choosen,random.randint(0,max)))
        if i %2 ==0:
            note_choosen = list_of_note_type[random.randint(0,len(list_of_note_type) - 1)]
            
    interval = []
    for i in range(number_of_note):
        interval.append(round(random.uniform(0, 0.5), 1))
        
    duration = []
    for i in range(number_of_note):
        duration = 1 / random.randint(1,4)
          
    return mp.chord(list_of_note,duration=duration,interval=interval,volume=mp.volume(random.randint(0,100))) * number_of_repetion
    #return mp.chord(list_of_note,duration=duration,volume=mp.volume(random.randint(0,100))) * number_of_repetion

def Generate_piece(number_of_chore:int):
    list_of_chore = []
    for i in range(number_of_chore):
        list_of_chore.append(Generate_chore(random.randint(10,20),max,random.randint(2,6)))
    
    instrument_list = []
    for i in range(number_of_chore):
        a = value_dictionnaire[random.randint(0,len(value_dictionnaire) - 1)]
        instrument_list.append(dictionnaire[a][random.randint(0,len(dictionnaire[a]) - 1)]) # choisi un instrument d'un des types d'instruments
        
    start_time = []
    for i in range(number_of_chore):
        start_time.append(i + random.randint(0,1))
        
    start_time[0] = 0
    
    return mp.piece(tracks=list_of_chore,instruments=instrument_list,bpm=random.randint(60,150),start_times=start_time)

piece = None  

while True:
    choice = input("1:Quit \n2:Generate a piece \n3:Play a piece \n4:Write the piece \n5:Read the file test.mid \n6:Generate and play \n->")
    if choice.isnumeric():
        if int(choice) == 1:
            break
        elif int(choice) == 2:
            piece = Generate_piece(4)
            print(piece)
        elif int(choice) == 3:
            if piece != None:
                mp.play(piece,wait=True)
            else:
                print("you didn't generate a piece")
        elif int(choice) == 4:
            if piece != None:
                
                mp.write(piece,name="test.mid")
                print("Your piece has been written on the file test.mid")
            else:
                print("you didn't generate a piece")
        elif int(choice) == 5:
            piece = mp.read("test.mid")
            print("You have succeffuly read the file test.mid")
        elif int(choice) == 6:
            piece = Generate_piece(4)
            mp.play(piece,wait=True)
    else:
        print("Only number are accepted")




