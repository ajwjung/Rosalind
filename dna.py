"""
Counting DNA Nucleotides
Link to problem: http://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

def count_bases(dna_strand):
    return dna_strand.count("A"), dna_strand.count("C"), dna_strand.count("G"), dna_strand.count("T")

def main():
    with open("dna_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read()
        
        for i in count_bases(contents):
            output.write(str(i) + " ")
    
if __name__ == "__main__":
    main()
