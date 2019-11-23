letters = {'z': 0, 'o': 0}
for letter in input(): letters[letter] += 1
print('Yes' if letters['z'] * 2 == letters['o'] else 'No')