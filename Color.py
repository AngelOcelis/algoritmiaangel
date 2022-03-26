color = input("Digite codigo color: ")
match color:
    case '#FF0000':
        print('🟥')
    case '#00FF00':
        print('🟩')
    case '#0000FF':
        print('🟦')
    case _:
        print("Unknown color")
        
    