"""
Rabbits and Recurrence Relations
Link to problem: http://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months,
        if we begin with 1 pair and in each generation,
        every pair of reproduction-age rabbits produces
        a litter of k rabbit pairs (instead of only 1 pair).
"""

def fib_rabbits(n, k):
    # Months 1 and 2 = 1 pairs
    last_month = 1
    two_months_ago = 1

    # Start from Month 3
    for i in range(2, n):
        current = last_month + k * two_months_ago
        last_month, two_months_ago = current, last_month
        
    return str(current)


def main():
    with open("fib_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read().split()
            n, k = int(contents[0]), int(contents[1])

            output.write((fib_rabbits(n, k)))


if __name__ == "__main__":
    main()