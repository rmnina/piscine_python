import sys


def morseTranslate(arg: str) -> any:
    morsecode = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--."
    }

    res = ""

    for x in arg.upper():
        if x.isalpha() or x == " ":
            res += morsecode[x] + " "
        else:
            return None

    return str(res)


def main():
    args = sys.argv

    try:
        assert len(args) == 2, "One expected argument"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    res = morseTranslate(args[1])

    try:
        assert res, "Bad character in string"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    print(res)


if __name__ == "__main__":
    main()
