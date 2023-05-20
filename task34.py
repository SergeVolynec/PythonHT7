song = input("Введите текст песни: ")
words = song.split()
vowels = list(map(lambda w: sum([1 for x in w.lower() if x in 'аоиыуэяею']), words))

if len(vowels) == vowels.count(vowels[0]):
    print("Парам пам-пам")
else:
    print("Пам парам")
