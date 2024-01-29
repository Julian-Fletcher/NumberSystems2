import random
import time

vals = {
    "0": {"binary": "0000", "hex": "0"},
    "1": {"binary": "0001", "hex": "1"},
    "2": {"binary": "0010", "hex": "2"},
    "3": {"binary": "0011", "hex": "3"},
    "4": {"binary": "0100", "hex": "4"},
    "5": {"binary": "0101", "hex": "5"},
    "6": {"binary": "0110", "hex": "6"},
    "7": {"binary": "0111", "hex": "7"},
    "8": {"binary": "1000", "hex": "8"},
    "9": {"binary": "1001", "hex": "9"},
    "10": {"binary": "1010", "hex": "A"},
    "11": {"binary": "1011", "hex": "B"},
    "12": {"binary": "1100", "hex": "C"},
    "13": {"binary": "1101", "hex": "D"},
    "14": {"binary": "1110", "hex": "E"},
    "15": {"binary": "1111", "hex": "F"}
}

conversion = {
    "b": "binary",
    "h": "hex",
    "d": "decimal"
}

correct = 0
wrongs = 0
time = 0.0

def main():
    global correct
    global wrongs
    global time

    correct = 0
    wrongs = 0
    time = 0.0


    print("MODES:\nDecimal to Binary -> dtb\nDecimal to Hex -> dth\nBinary to Decimal -> btd")
    print("Binary to Hex -> bth\nHex to Decimal -> htd\nHex to Binary -> htb")
    print()
    mode = input("What mode? ")
    rounds = int(input("How rounds would you like to do? "))

    
    
    if mode == 'dtb' or mode == 'dth':
        dtx(rounds, conversion[mode[-1]])
    elif mode == 'btd' or mode == 'bth':
        btx(rounds, conversion[mode[-1]])
    elif mode == 'htd' or mode == 'htb':
        htx(rounds, conversion[mode[-1]])

    # Printing out the score
    print("\nGame Complete! Final Score:")
    print("Correct: " + str(correct) + "\nIncorrect: " + str(wrongs) + "\nAccuracy: " + str((correct/rounds) * 100) + "%")

    replay = input("Play Again? [y/n] ")
    if replay == 'y':
        print()
        main()


def dtx(rounds, converting_to):
    for _ in range(rounds):
        index = get_num(0, 15)
        print(index)
        answer = input(": ")
        get_answer(index, converting_to, answer)


def btx(rounds, converting_to):
    for _ in range(rounds):
        index = get_num(0, 15)
        print(vals[index]['binary'])
        answer = input(": ")
        get_answer(index, converting_to, answer)


def htx(rounds, converting_to):
    for _ in range(rounds):
        index = get_num(0, 15)
        print(vals[index]['hex'])
        answer = input(": ")
        get_answer(index, converting_to, answer)


# Returns a string for dict lookup
def get_num(min, max):
    return str(random.randint(min, max))


def get_answer(index, mode, answer):
    global correct
    global wrongs

    if mode == 'decimal':
        if answer == index:
            correct += 1
            print("Correct!")
            return
        else:
            wrongs += 1
            print("Incorrect! Correct answer is: " + str(index))
            return

    if answer == vals[index][mode]:
        correct += 1
        print("Correct!")
    else:
        wrongs += 1
        print(f"Incorrect! Correct answer is: " + vals[index][mode])


main()
