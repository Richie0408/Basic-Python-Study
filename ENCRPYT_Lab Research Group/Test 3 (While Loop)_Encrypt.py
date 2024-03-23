#Test 3
# def game(command):
#     print("============ WELCOME TO LIFE SIMULATOR ============\n"
#           "press help to see all of the command")
#     list = []
#     rest = False
#     eat = False
#     while command != "quit":
#         command = input("> ").lower()
#         if command == "play":
#             rest = False
#             eat = False
#             count = 0
#             list.append(command)
#             for x in list:
#                 if x == "play":
#                     count+=1
#             if count >= 3:
#                 print("Huh, i'm tired, i want to go home...\n")
#             else:
#                 print("I'm so excited to play outside, here i go...\n")
#         elif command == "rest":
#             eat = False
#             list.clear()
#             if rest == False:
#                 print("I think i need to go to bed...\n")
#                 rest = True
#             else:
#                 print("I'm not that tired to sleep.\n")
#         elif command == "eat":
#             rest = False
#             list.clear()
#             if eat == False:
#                 print("Argh, i want to eat baso ayam\n")
#                 eat = True
#             else:
#                 print("I'm not hungry yet...\n")
#         elif command == "help":
#             print("========== Game Guide ==========\n"
#                 "play - to play outside\n" 
#                 "rest - to rest\n"
#                 "eat - to eat\n"
#                 "quit - to quit the game\n"
#                 "================================\n")
#         elif command == "quit":
#             print("Thank you for playing this game...\n")
#             break
#         else:
#             print("Sorry, i don't understand that code...\n")
# game('')


print("============ WELCOME TO LIFE SIMULATOR ============\n"
          "press help to see all of the command")
command = ''
while command != "quit":
    command = input("> ").lower()
    if command == "play":
        print("Let's Play ...\n")
    elif command == "rest":
        print("I think i need to go to bed...\n")
    elif command == "eat":
        print("Argh, i want to eat baso ayam\n")
    elif command == "help":
        print("========== Game Guide ==========\n"
                "play - to play outside\n" 
                "rest - to rest\n"
                "eat - to eat\n"
                "quit - to quit the game\n"
                "================================\n")
    elif command == "quit":
        print("Thank you for playing this game...\n")
    else:
        print("Sorry, i don't understand that code...\n")