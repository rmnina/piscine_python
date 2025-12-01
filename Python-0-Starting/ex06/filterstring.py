import sys
from ft_filter import ft_filter


def main():
    args = sys.argv

    try:
        assert len(args) == 3, "Two expected arguments:[string][max_len]"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    stringTab = args[1].split(" ")

    result = ft_filter(lambda x: len(x) > int(args[2]), stringTab)
    print(f"{result}")


if __name__ == "__main__":
    main()
