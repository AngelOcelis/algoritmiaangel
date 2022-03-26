from sre_constants import AT_BEGINNING_LINE


text = str(input("inserte una palabra: "))
for char in text:
    if not char.isalpha():
        print('No Corresponde Alfabeticamente')
        break
    else:
        print('Corresponde Alfabeticamente')