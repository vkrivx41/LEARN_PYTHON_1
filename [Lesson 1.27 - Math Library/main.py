
import math


def main() -> None:
    print(math)
    count: int = 0

    for method in dir(math):
        if "__" not in method:
            count += 1
            print(count, ":", method)


if __name__ == '__main__':
    main()