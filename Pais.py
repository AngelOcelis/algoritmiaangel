pais = str(input("Digite su pais: "))
match pais:
    case 'Italia':
        print('🇮🇹')
    case 'Brasil':
        print('🇧🇷')
    case 'Colombia':
        print('🇨🇴')
    case 'España':
        print('🇪🇸')
    case 'Francia':
        print('🇫🇷')
    case _:
        print("Unknown Pais")