import os 
import time
from datetime import date

os.system("clear")

def header():
    print("""
    $$$$$$$\               $$$$$\                                                   $$\ 
    $$  __$$\              \__$$ |                                                  $$ |
    $$ |  $$ |$$\   $$\       $$ | $$$$$$\  $$\   $$\  $$$$$$\  $$$$$$$\   $$$$$$\  $$ |
    $$$$$$$  |$$ |  $$ |      $$ |$$  __$$\ $$ |  $$ |$$  __$$\ $$  __$$\  \____$$\ $$ |
    $$  ____/ $$ |  $$ |$$\   $$ |$$ /  $$ |$$ |  $$ |$$ |  \__|$$ |  $$ | $$$$$$$ |$$ |
    $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |$$  __$$ |$$ |
    $$ |      \$$$$$$$ |\$$$$$$  |\$$$$$$  |\$$$$$$  |$$ |      $$ |  $$ |\$$$$$$$ |$$ |
    \__|       \____$$ | \______/  \______/  \______/ \__|      \__|  \__| \_______|\__|
              $$\   $$ |                                                                
              \$$$$$$  |                                                                
               \______/                                                                 
    """)

header()

print("")


today = date.today()
print(str(today) + "\n")
filename = str(today) + ".txt"

print("What do you want to do? \n")
print("1 / 2 / 3 / 4\n ")

mode = input("1/Add a line 2/View today's Journal 3/Clear today's Journal 4/Exit \n\n> ")

time.sleep(0.3)

os.system("clear")
header()

if mode == "1":
    if not os.path.exists("pages/"+str(filename)):
        open("pages/"+str(filename), "w").write(f"Journal Entry for {today}\n\n")
    if os.path.exists("pages/"+str(filename)):
        user_input = input("> ")
        open("pages/"+str(filename), "a").write(user_input + "\n")

if mode == "2":
    if not os.path.exists("pages/"+str(filename)):
            open("pages/"+str(filename), "w").write(f"Journal Entry for {today}\n\n")
    journal_content = open("pages/"+str(filename), "r").read()
    print(journal_content)

if mode == "3":
    if not os.path.exists("pages/"+str(filename)):
            open("pages/"+str(filename), "w").write(f"Journal Entry for {today}\n\n")
    os.system("clear")
    header()
    clear_confirm = input("Are you sure you want to clear today's Journal? This action can't be undone! (Y/n)")
    if clear_confirm == "y" or "\n":
        if os.path.exists("pages/"+str(filename)):
            os.remove("pages/"+str(filename))
        

if mode == "4":
    os.system("clear")
    header()
    print("Bye!")
    time.sleep(0.5)
    os.system("clear")


# SyntaxxDev
