def emoji_converter(message):
    word = message.split(" ")
    emojis = {
        ":)":"Smilyface",
        ":(":"Sadface"
    }
    output = ""
    for words in word:
        output += emojis.get(words, words)+" "
    return(output)


message = input("> ")
print(emoji_converter(message))

