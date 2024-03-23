def greet_user(name):
    print(f'Hi {name}')
greet_user("john")


def square(number):
    return number*number
print(square(3))


def message(word):
    message_1 = word.split(" ")
    dictionary = {
        ":v" : ", Biasa aja",
        ":3" : ", Ehe"
    }
    answer = ""
    for i in message_1:
        answer += dictionary.get(i, i)+" "
    return answer


print(message("good morning :3"))





