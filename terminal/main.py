import pygame
from tkinter.filedialog import askdirectory
from os import chdir, listdir

class ExBool:
    def __nooe__(content:str, token:str):
        return content.lower().startswith(token.lower())

class SongListManager:
    def GetSongList():
        directory = askdirectory()
        chdir(directory)
        return listdir()

    def RefleshSongList():
        return listdir()

class MediaControl:
    def Play():
        index = int(COMMAND.split(" ")[1].replace("--", ""))
        pygame.mixer.music.load(play_list[index])
        pygame.mixer.music.play()
        print(index)

    def Stop():
        pygame.mixer.music.stop()
    
    def Pause():
        pygame.mixer.music.pause()
    
    def Unpause():
        pygame.mixer.music.unpause()

    def List():
        new_song_list = SongListManager.RefleshSongList()
        for i in range(len(new_song_list)):
            print(i, new_song_list[i])

song_list = SongListManager.GetSongList()

play_list = []

for i in song_list:
    pos = 0
    play_list.append(i)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

for i in range(len(play_list)):
    print(i, play_list[i])

while True:
    COMMAND = input("> ")

    if ExBool.__nooe__(COMMAND, "play"):
        MediaControl.Play()

    elif ExBool.__nooe__(COMMAND, "stop"):
        MediaControl.Stop()

    elif ExBool.__nooe__(COMMAND, "pause"):
        MediaControl.Pause()

    elif ExBool.__nooe__(COMMAND, "unpause"):
        MediaControl.Unpause()
    
    elif ExBool.__nooe__(COMMAND, "list"):
        MediaControl.List()
    
    elif ExBool.__nooe__(COMMAND, "exit"):
        exit(0)

    else:
        print("""
    COMMANDS

 play    -   play music
    HOW TO USE
        play --song_index

 stop    -   stop music
    HOW TO USE
        stop

 pause   -   pause music
    HOW TO USE
        pause

 unpause -   unpause music
    HOW TO USE
        unpause

 list    -   list playlist
    HOW TO USE
        list

 exit    -   exit the program
    HOW TO USE
        exit
""")