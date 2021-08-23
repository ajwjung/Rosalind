"""
Finding a Motif in DNA
Link to problem: http://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""

def search_substr(s, t):
    """
    Searches for a substring within a string.
    Returns indices as a list of strings.
    """
    
    start = 0
    incr = len(t)

    indices = []
    while start < (len(s) - len(t) - 1):
        if t == s[start:start + incr]:
            indices.append(str(start + 1))
        start += 1
    
    return indices


def main():
    with open("subs_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            strand, sub = f.read().split()

            ind = search_substr(strand, sub)
            output.write(" ".join(ind))


if __name__ == "__main__":
    main()