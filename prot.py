"""
Translating RNA into Protein
Link to problem: http://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA
       (of length at most 10 kbp).
Return: The protein string encoded by s.
"""


def translate(raw_seq):
    # Convert codon/amino acid string to dictionary
    codons = """
        UUU F      CUU L      AUU I      GUU V
        UUC F      CUC L      AUC I      GUC V
        UUA L      CUA L      AUA I      GUA V
        UUG L      CUG L      AUG M      GUG V
        UCU S      CCU P      ACU T      GCU A
        UCC S      CCC P      ACC T      GCC A
        UCA S      CCA P      ACA T      GCA A
        UCG S      CCG P      ACG T      GCG A
        UAU Y      CAU H      AAU N      GAU D
        UAC Y      CAC H      AAC N      GAC D
        UAA Stop   CAA Q      AAA K      GAA E
        UAG Stop   CAG Q      AAG K      GAG E
        UGU C      CGU R      AGU S      GGU G
        UGC C      CGC R      AGC S      GGC G
        UGA Stop   CGA R      AGA R      GGA G
        UGG W      CGG R      AGG R      GGG G 
    """
    trans = codons.split()
    trans_dict = dict(zip(trans[::2], trans[1::2])) # Codon: Amino Acid
    
    protein = ""
    for i in range(0, len(raw_seq) - 2, 3):
        protein += trans_dict[raw_seq[i:i + 3]]
    
    return(protein.replace("Stop", ""))


def main():
    with open("prot_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read()

            output.write(translate(contents))
            

if __name__ == "__main__":
    main()