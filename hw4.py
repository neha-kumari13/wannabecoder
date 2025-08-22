prime_numbers = [num for num in range(1, 51) if all(num % i != 0 for i in range(2, num))]

print("Prime numbers from 1 to 50:")
print(prime_numbers)
