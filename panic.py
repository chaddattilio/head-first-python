
phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

# pops the last four objects - plist is "Don't pa" afterward
for i in range(4):
    plist.pop()

# plist is "on't pa" afterward
plist.pop(0)

# plist is "ont pa" afterward
plist.remove("'")

# plist is "ont ap" afterward
plist.extend([plist.pop(), plist.pop()])

# plist is "on tap" afterward
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
