message = input(">")
words = message.split(' ')
emojis ={
    ":)":   "😀",
    ":(":   "😥",
    ";)":   "😉",
    ";/":   "🤔",
    ":/":   "😐",
    ":||":  "😑",
    ":o":   "😮",
    ":D":   "😁"
}
output= ""
for word in words:
   output += emojis.get(word, word) + ""
print(output)
