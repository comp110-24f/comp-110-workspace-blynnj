"Write program for a tea party"


__author__: str = "730749523"


def tea_bags(people: int) -> int:
    """number of tea bags per person"""
    return people * 2


def treats(people: int) -> int:
    """number of treats per person"""
    return int(tea_bags(people=people) * 1.5)


# to call the tea_bags function in treats function make the parameters equal to eo


def cost(tea_count: int, treat_count: int) -> float:
    """total cost of tea bags and treats per person"""
    return tea_count * 0.5 + treat_count * 0.75


# the number for tea and treats will be calculated later in the main function


def main_planner(guests: int) -> None:
    """running the program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# use contractions to put together the stings and parameters

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
