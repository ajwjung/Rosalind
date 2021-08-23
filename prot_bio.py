"""
Translating RNA into Protein
Link to problem: http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA
       (of length at most 10 kbp).
Return: The protein string encoded by s.

This solution uses Biopython.
"""

from Bio.Seq import Seq


def main():
    with open("prot_bio_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read()
            rna = Seq(contents)
            
            output.write(str(rna.translate(to_stop=True)))


if __name__ == "__main__":
    main()