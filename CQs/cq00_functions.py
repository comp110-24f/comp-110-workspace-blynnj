__author__ = 730749523


def mimic(message: str) -> str:
    """repeat a message"""
    return message


def main() -> None:
    """print result of mimic call"""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()
