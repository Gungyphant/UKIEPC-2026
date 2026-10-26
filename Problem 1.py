number_of_words, max_number_of_letters = map(int, input().split(" "))

words = input().split(" ")
character_frequencies = {}
for word in words:
    for char in word:
        if char not in character_frequencies:
            character_frequencies[char] = 0
        character_frequencies[char] += 1

chosen_letters = sorted(character_frequencies.keys(), key=lambda x: character_frequencies[x], reverse=True)[:max_number_of_letters]

new_words = []
for word in words:
    new_word = "".join(c if c in chosen_letters else chosen_letters[0] for c in word)
    new_words.append(new_word)

print(*new_words)
