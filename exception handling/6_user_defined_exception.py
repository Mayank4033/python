class InvalidAgeException(Exception):
    pass
voting_age = 18
while True:
    age = int(input("Enter your age"))
    try:
        if age<voting_age:
            raise InvalidAgeException
        else:
            print("you are eligible for voting")
            break
    except InvalidAgeException:
        print("you are not eligible for voting")