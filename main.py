import tkinter as tk #gui library
import random #random library
import pygame #for sound :D

window = tk.Tk()
pygame.mixer.init() # initialise the pygame mixer

### Variables
food_list = ["ส้มตำ",
             "ข้าวผัดกุ้ง",
             "ข้าวผัดกะเพราหมูสับ",
             "ไก่ทอดหาดใหญ่",
             "ข้าวไก่ทอดน้ำปลา",
             "ข้าวหมูทอดกระเทียม",
             "ข้าวหมูทอดเกลือ",
             "ข้าวไข่เจียวปู",
             "ผัดไทย",
             "ข้าวมันไก่",
             "ข้าวหน้าเป็ด",
             "ข้าวซอย",
             "ข้าวหมูแดง",
             "ข้าวหมูกรอบ",
             "แกงส้ม",
             "แกงเขียวหวาน",
             "แกงจืด",
             "ต้มยำ",
             "ต้มข่าไก่",
             "ข้าวไข่เจียว",
             ]

resultFoodText = ("Arial", 20, "bold")
randomButtonText = ("Arial", 15, "bold")
sound_played = False # flag this as false to start with

### Functions
def update_result(): # update the result label
    current_food = food_list.pop(0)
    resultFood.config(text=current_food)
    food_list.append(current_food)

def play_sound_once(): # play the sound once
    global sound_played
    
    if not sound_played:
        sound = "random.mp3"
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()
        sound_played = True

def scroll_items(delay_index=0): # scroll the items
    update_result()
    play_sound_once()
    
    delays = list(range(0, 600, 20)) # list all the delays

    if delay_index < len(delays): # if the delay index is less than the length of the delays
        delay = delays[delay_index]
        window.after(delay, scroll_items, delay_index + 1) # call scroll_items again after delay then plus the delay_index
        randomButton.config(state=tk.DISABLED)
    else:
        global sound_played # set the sound_played to false and enable the random button
        sound_played = False
        randomButton.config(state=tk.NORMAL)


### Window configuration
# Titlebar
window.title("กินอะไรดี")
window.minsize(500, 350) # fixed width, height
window.maxsize(500, 350)
window.attributes('-toolwindow', 1) # remove minimize and maximize button
window.configure(background='#4B4758')

# Main content
resultFood = tk.Label(window,
                       bg="black",
                       fg="white",
                       height=5,
                       width=25,
                       text="กินอะไรดีจ๊ะ?",
                       font=resultFoodText
                    )

randomButton = tk.Button(window,
                         bg="#30333C",
                         fg="#D9D9E3",
                         text="สุ่มเลย!",
                         command=scroll_items,
                         font=randomButtonText
                        )

### Packs
resultFood.pack(pady=30)
randomButton.pack(pady=25)
window.mainloop() # main loop