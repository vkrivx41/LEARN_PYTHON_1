
# if __name__ == "__main__": means that the statements available in this execution will only run if the module is run
# directly and not imported into another module

import parser


def main() -> None:
    print("We are running this Initialization Function from only the main module...")


if __name__ == "__main__":
    main()
