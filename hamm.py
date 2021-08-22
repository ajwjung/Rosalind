"""
Counting Point Mutations
Link to problem: http://rosalind.info/problems/hamm/

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
Return: The Hamming distance dH(s,t).
"""

# Compare two strings and returns the number of differences
def hamm_dist(a, b):
    count = 0
    for s, t in zip(a, b):
        if s != t:
            count += 1

    return str(count)

def main():
    with open("hamm_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read().split()
            
            output.write(hamm_dist(contents[0], contents[1]))


if __name__ == "__main__":
    main()