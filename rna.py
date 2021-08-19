"""
Transcribing DNA into RNA
Link to problem: http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
"""

def transcribe(dna_strand):
    return dna_strand.replace("T", "U")

def main():
    with open("rna_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read()

        output.write(transcribe(contents))


if __name__ == "__main__":
    main()
