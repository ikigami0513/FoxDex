def format_pokedex_number(number: int):
    lenght = len(str(number))
    format_number = ""
    for i in range(0, 4-lenght):
        format_number += "0"

    return format_number + str(number)