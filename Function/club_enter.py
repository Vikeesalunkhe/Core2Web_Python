def enter_club(name : str, age: int, has_id: bool):

    if name.lower() == "bob":
        print("Get out of here")
        return

    elif age >= 18 and has_id:
        print(f"{name} are enter in the club")

    else:
        print(f"{name} are not enter the club")


def main():
    enter_club('Bob', 29, has_id=True)
    enter_club("Vikee", 17, has_id=True)
    enter_club("Vaibhav", 21, has_id=False)
    enter_club("Dhiraj", 22, has_id=True)

if __name__ == "__main__":
    main()
