#con_cuidado
import os
def letras():
    return {
    '7777': 's',
    '777': 'r',
    '555': 'l',
    '666': 'o',
    '888': 'v',
    '9999': 'z',
    '999': 'y',
    '333': 'f',
    '444': 'i',
    '77': 'q',
    '88': 'u',
    '66': 'n',
    '222': 'c',
    '99': 'x',
    '22': 'b',
    '33': 'e',
    '44': 'h',
    '55': 'k',
    '3': 'd',
    '2': 'a',
    '5': 'j',
    '4': 'g',
    '7': 'p',
    '6': 'm',
    '9': 'w',
    '8': 't',
    '0': ' ',

}

if "__main__" == __name__:
    x = []
    while True:
        os.system('clear')
        print(("").join(x))
        j = input('')
        if j == '1' and x:
            x.pop()
        else: x.append(letras().get(j, ''))

