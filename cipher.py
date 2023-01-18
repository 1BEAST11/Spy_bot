def cipher(phrase):
    alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz0123456789№@%,./!?#-&$'

    key = 5
    search = 0
    cipher = ''

    for i in phrase:
        if i == ' ':
            cipher += i
            continue

        while i != alphabet[search]:
            search += 1

        for j in range(key):
            if alphabet[search] == '$':
                search = 0

            else:
                search += 1

        cipher += alphabet[search]
        search = 0
    return cipher
