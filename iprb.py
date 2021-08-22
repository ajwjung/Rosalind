"""
Mendel's First Law
Link to problem: http://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
       k individuals are homozygous dominant for a factor,
       m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce
       an individual possessing a dominant allele (and thus displaying the dominant phenotype).
       Assume that any two organisms can mate.
"""


def first_law(values):
    """
    Accepts a list of string values for k, m, and n.
    Returns the probability that two organisms produce an offspring with the dominant allele.
    """
    k, m, n = (int(x) for x in values)
    total = float(k + m + n)
    
    # Use probability of complementary event - offspring does NOT carry dominant allele
    # Parent pairs: m * m, m * n, n * m, and n * n
    q = (0.25 * m * (m - 1) + (m * n) + n * (n - 1)) / (total * (total - 1))

    return str(1 - q)


def main():
    with open("iprb_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read().split()
            
            output.write(first_law(contents))


if __name__ == "__main__":
    main()