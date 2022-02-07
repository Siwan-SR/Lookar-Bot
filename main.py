import os
from replit import db
import sys

bot_name = 'Lookar'
discord = 'https://discord.com/'
github = 'https://github.com/'
replit = 'https://replit.com/'

print("Hello! I am Lookar Bot my prefix is '!'\n")

cmd_wish = input ("Enter command: ")

if cmd_wish == '!commands':
  print("\n")
  print(os.environ['commands'])

elif cmd_wish == '!greet':
  print("\n")
  print("Hello I am ",bot_name + ". You can type commands and see me work! Use !commands to see all commands.")

elif cmd_wish == '!trivia':

 print("Still under developement")

elif cmd_wish == '!quit':
  print("You have quited the program.")
  sys.exit()

elif cmd_wish == '!discord':
  print("The owner currently doesn't have a public discord server. Here is the link of discord's website: ",discord)

elif cmd_wish == '!github':
  print("GitHub's website: ",github + ".\nOwner GitHub: https://github.com/@Siwan-SR/")

elif cmd_wish == '!replit':
  print("Replit's website: ",replit + ".\nOwner Replit: https://replit.com/@Siwan-SR/")

else:
  print("That is not a command! Do !commands to see all commands.")
  sys.exit()