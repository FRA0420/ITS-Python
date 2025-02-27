numbers:list[int]=[1,2,3,4,5,6,7,8,9]

for n in numbers:
    match n:
        case n if n == numbers[0]:
            print(f"{n}st!")
        case n if n == numbers[1]:
            print(f"{n}nd!")
        case n if n == numbers[2]:
            print(f"{n}rd!")
        case _:
            print(f"{n}th!")