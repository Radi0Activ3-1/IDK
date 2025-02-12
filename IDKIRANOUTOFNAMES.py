def collatz_conjecture(num):
    """Prints the sequence of numbers in the Collatz conjecture until it reaches 1."""
    while num != 1:
        print(int(num))  # Print the current number as an integer
        if num % 2 == 0:  # If the number is even
            num = num / 2
        else:  # If the number is odd
            num = num * 3 + 1
    print(int(num))  # Print the final number (which should be 1)

def add_numbers(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def sum_natural_numbers(n):
    """Calculates the sum of all natural numbers from 1 to n."""
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

if __name__ == "__main__":
    try:
        user_input = float(input("Enter a number for the Collatz conjecture: "))  # Take input for Collatz
        collatz_conjecture(user_input)
        
        n = int(input("Enter a positive integer for sum calculation: "))  # Take input for sum calculation
        if n < 1:
            print("Please enter a positive integer.")
        else:
            sum_result = sum_natural_numbers(n)
            print(f"Sum: {sum_result}")
            
    except ValueError:
        print("Please enter a valid number.")