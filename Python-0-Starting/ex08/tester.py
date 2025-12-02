from Loading import ft_tqdm
from time import sleep
from tqdm import tqdm


def main():
    for elem in ft_tqdm(range(100)):
        sleep(0.005)
    print()
    for elem in tqdm(range(100)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
