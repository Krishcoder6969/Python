def cyclic_swap(a, b, c):
    """
    Swaps three numbers in a cyclic order: a -> b, b -> c, c -> a.
    """
    temp = a
    a = c
    c = b
    b = temp
    return a, b, c
num1 = 10
num2 = 20
num3 = 30
print(f"Before swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")
num1, num2, num3 = cyclic_swap(num1, num2, num3)

print(f"After swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")