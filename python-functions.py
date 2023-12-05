# =================
# Challenge 1
# =================

print("Challenge 1: ")

def sum_to(arg):
    sum = 0
    for num in range(arg+1):
        sum += num

    return sum

print(f"sum_to(6) = {sum_to(6)}")
print(f"sum_to(10) = {sum_to(10)}")  

print("===============")
print("")


# =================
# Challenge 2
# =================

print("Challenge 2: ")

def largest(arg):
    largest_num = 0
    for num in arg:
        if num > largest_num:
            largest_num = num
    
    return largest_num

print(f"largest([1, 2, 3, 4, 0]) = {largest([1, 2, 3, 4, 0])}")
print(f"largest([10, 4, 2, 231, 91, 54]) = {largest([10, 4, 2, 231, 91, 54])}")

print("===============")
print("")


# =================
# Challenge 3
# =================

print("Challenge 3: ")

def occurrences(string, search):
    count = string.count(search)
    return count


print(f"occurrences('fleep floop', 'e') = {occurrences('fleep floop', 'e')}")
print(f"occurrences('fleep floop', 'p') = {occurrences('fleep floop', 'p')}")
print(f"occurrences('fleep floop', 'ee') = {occurrences('fleep floop', 'ee')}")
print(f"occurrences('fleep floop', 'fe') = {occurrences('fleep floop', 'fe')}")

print("===============")
print("")


# =================
# Challenge 4
# =================

print("Challenge 4: ")

def product(*args):
    num = 1
    for arg in args:
        num = num * arg
    
    return num

print(f"product(-1, 4) = {product(-1, 4)}")
print(f"product(2, 5, 5) = {product(2, 5, 5)}")
print(f"product(4, 0.5, 5) = {product(4, 0.5, 5)}")

print("===============")
print("")


# =================
# Bonus Challenge
# =================

print("Bonus Challenge: ")

def steps_to_zero(arg):
    count = 0
    num = arg

    while num > 0:
        if num % 2 == 0:
            num = num / 2
            count += 1
        else:
            num = num - 1
            count += 1

    return count

print(f"steps_to_zero(14) = {steps_to_zero(14)}")

        
