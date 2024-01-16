
import random


def main() -> None:
    counter: int = 0

    for method in dir(random):
        if "_" not in method:
            counter += 1
            print(counter, method)


if __name__ == "__main__":
    main()
