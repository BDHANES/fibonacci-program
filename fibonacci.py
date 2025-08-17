# Fibonacci sequence using iteration

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Number of terms
num_terms = int(input("Enter number of terms: "))
fibonacci(num_terms)


OUTPUT:
Enter number of terms: 10
0 1 1 2 3 5 8 13 21 34
