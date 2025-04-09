def operations(a:int,b:int) -> tuple[int,int]:
    sum_result:int=a+b
    diff_result:int=a-b
    molt_result:int=a*b
    return sum_result,diff_result,molt_result

sum_value,diff_value,molt_value = operations(10,5)
print(operations(10,5))
print("Sum:", sum_value)

print("Diff:", diff_value)

print("Molt:", molt_value)

print(type(operations(10,5)))