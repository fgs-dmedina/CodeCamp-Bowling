def convert_string_to_integer_list(string: str) -> list:

    output = [-1 for _ in range(len(string))]

    for i, rune in enumerate(string):
        
        is_rune_miss = rune == '-'
        is_rune_spare = rune == '/'
        is_rune_strike = rune == 'X'

        if is_rune_miss:
            output[i] = 0
        
        if is_rune_spare:
            previous = -1 
            if string[i - 1] == '-':
                previous = 0
            else:
                previous = int(string[i - 1])
                
            output[i] = (10 - previous)

        if is_rune_strike:
            output[i] = 10

        is_rune_integer = not is_rune_miss and not is_rune_spare and not is_rune_strike
        if is_rune_integer:
            output[i] = int(rune)

    return output
