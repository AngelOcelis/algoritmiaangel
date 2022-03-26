volar = bool(int(input('¿Puede volar? 1:Si 0:No :')))
humano = bool(int(input('¿Es humano? 1:Si 0:No :')))
mascara = bool(int(input('¿Tiene mascara? 1:Si 0:No :')))

if volar is True and humano is True and mascara is True:
    print('IROMAN')
elif volar is True and humano is True and mascara is False:
    print('CAPITAN MARVEL')
elif volar is True and humano is False and mascara is True:
    print('RONAN ACCUSER')
elif volar is True and humano is False and mascara is False:
    print('VISION')
elif volar is False and humano is True and mascara is True:
    print('SPIDERMAN')
elif volar is False and humano is True and mascara is False:
    print('HULK')
elif volar is False and humano is False and mascara is True:
    print('BLACK BOLT')
elif volar is False and humano is False and mascara is False:
    print('THANOS')
    
