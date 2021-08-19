"""
Complementing a Strand of DNA
Link to problem: http://rosalind.info/problems/revc/

Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement sc of s.
"""

def rev_complement(dna_strand):
    trans_table = dna_strand.maketrans("ACGT", "TGCA")

    return dna_strand.translate(trans_table)[::-1]

def main():
    with open("revc_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read().strip()

        output.write(rev_complement(contents))


if __name__ == "__main__":
    main()
