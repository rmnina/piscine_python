import sys


def morseTranslate(arg: str) -> str:
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
        res += morsecode[x] + " "

    return str(res)


def main():
    args = sys.argv

    try:
        assert len(args) == 2, "One expected argument"
        assert not [x for x in args[1] if not x.isalpha() and not x == " "], \
            "Bad character in string"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    print(morseTranslate(args[1]))


if __name__ == "__main__":
    main()
