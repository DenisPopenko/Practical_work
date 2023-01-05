text = input('Введите строку: ') # ПитоН - этО хорошО

lowers = len([letter for letter in text if letter.islower()])
uppers = len([letter for letter in text if letter.isupper()])

#print(lowers, uppers)
if lowers > uppers:
    print("Результат:", text.lower())
else:
    print("Результат:", text.upper())
