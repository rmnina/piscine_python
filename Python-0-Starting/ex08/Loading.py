import os


ESC = '\x1b'
RESET = ESC + "[0m"
GREEN = 94
BLUE = 99
OFFSET = 40
BAR_OFFSET = 4
BLOC = '▓'


def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for x in lst:
        percentage = int((x + 1) * 100 / total)
        length = os.get_terminal_size().columns - OFFSET
        filled = int((x + 1) * (length) / total)
        bar = ""

        for i in range(filled):
            color = GREEN + int((BLUE - GREEN) * i / filled)
            bar += f"{ESC}[38;5;{color}m{BLOC}"
            length += len(f"{ESC}[38;5;{color}m")

        bar += RESET

        print(f"\r{percentage:3d}%|", end='')
        print(bar.ljust(length + BAR_OFFSET), "| ", sep='', end='')
        print(f"{x + 1}/{total}", end='')
        yield x
