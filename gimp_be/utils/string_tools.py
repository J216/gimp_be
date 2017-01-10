from gimp_be.settings.settings import *

lines = ['']
try:
    os.chdir(os.path.abspath(__file__)[0:os.path.abspath(__file__).rfind('\\')])
    text_file = open('words.txt', 'r')
    lines = list(text_file.read().split('\n'))

except:
    lines = ['File not loaded']


def imageTitle(opt=0):
    """
    assemble title string
    :param opt:
    :return:
    """
    import random,os
    global settings_data
    global lines
    try:
        os.chdir(os.path.abspath(__file__)[0:os.path.abspath(__file__).rfind('\\')])
        text_file = open('words.txt', 'r')
        lines = text_file.read().split('\n')
        if opt == 2:
            title = random.choice(lines) + ' ' + random.choice(lines)
        else:
            title = random.choice(lines) + ' ' + random.choice(lines) + ' ' + random.choice(lines)

    except:
        title = 'File not loaded'
    return title


def stringIncrement(serial_string):
    """
    string incrementer
    :param serial_string:
    :return:
    """
    init_ser = serial_string
    carry = 0
    let = 65
    for letS in serial_string[::-1]:
        let = ord(letS)
        let = let + 1
        if let > 122 or let < 65:
            carry = carry + 1
            let = 65
            serial_string = serial_string[:len(serial_string) - (carry)] + chr(let) + serial_string[
                                                                                      len(serial_string) - carry + 1:]
        elif let > 90 and let < 97:
            let = 97
            serial_string = serial_string[:len(serial_string) - (carry + 1)] + chr(let) + serial_string[
                                                                                          len(serial_string) - carry:]
            break
        else:
            serial_string = serial_string[:len(serial_string) - (carry + 1)] + chr(let) + serial_string[
                                                                                          len(serial_string) - carry:]
            break
    return serial_string
