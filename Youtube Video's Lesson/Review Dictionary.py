message = input("> ")
message_1 = message.split(" ")

dictionary = {
    ":v" : "SIUUUUU",
    ":)" : "HEHEHE"
}
answer = ""
for i in message_1:
    answer += dictionary.get(i, i) + " "

print(answer)


for x in range(10):
    print("kevin babi")



