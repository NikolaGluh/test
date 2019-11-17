from random import choice

# Tic tac toe

toetable = ["toe", "TOE", "Toe", "TOE!", "toe?", "toe.", "toeeeeeeeeeee", "ToE", "toooooooooE"]
whattable = ["fat", "big", "small", "thicc", "noob", "pro"]
table = choice(toetable)
what = choice(whattable)

print(table + what)
