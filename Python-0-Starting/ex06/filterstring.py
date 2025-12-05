import sys
from ft_filter import ft_filter


def main():
    args = sys.argv

    try:
        assert len(args) == 3, "Two expected arguments:[string][max_len]"
        assert not [x for x in args[1] if not x.isalpha() and not x == " "], \
            "Bad argument (argv[1])"
        assert not [x for x in args[2] if not x.isdigit()], \
            "Bad argument (argv[2])"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    stringTab = args[1].split(" ")

    result = ft_filter(lambda x: len(x) > int(args[2]), stringTab)

    print(f"{result}")


if __name__ == "__main__":
    main()
