top = "qqwertyuiopp"
mid = "aasdfghjkl;;"
bot = "zzxcvbnm,.//"

shift = input()
s = input()
for i, char in enumerate(s):
    if shift == 'R':
        if char in top:
            index = top.find(char, 1)
            char = top[index - 1]
            print(char,end="")
        if char in mid:
            index = mid.find(char, 1)
            char = mid[index - 1]
            print(char, end="")
        if char in bot:
            index = bot.find(char, 1)
            char = bot[index - 1]
            print(char, end="")
    else:
        if char in top:
            index = top.find(char, 1)
            char = top[index + 1]
            print(char, end="")
        if char in mid:
            index = mid.find(char, 1)
            char = mid[index + 1]
            print(char, end="")
        if char in bot:
            index = bot.find(char, 1)
            char = bot[index + 1]
            print(char, end="")

# print(s)

