def rem(l, Word):
    n =[]
    for item in l:
        if not (item == Word):
            n.append(item.strip(Word))

l = ["Harry","rk", "Aru"]

print(rem(l, "rk"))
