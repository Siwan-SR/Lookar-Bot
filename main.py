import os
import sys

bot_name = 'Lookar'

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

else:
  print("That is not a command! Do !commands to see all commands.")
  sys.exit()