"""
Computing GC Content
Link to problem: http://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content,
        followed by the GC-content of that string.
        Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated.
"""

def parse_fasta(data):
    """
    Parses a FASTA file and stores sequences in a dictionary.
    Format: dict = {sequence_id: sequence}
    """
    seqs = {}
    for line in data:
        if line.startswith(">"):
            header = line
            seqs[header] = ""
        else:
            seqs[header] += line

    return seqs


def gc_content(dna):
    return (dna.count("G") + dna.count("C"))/len(dna) * 100


def get_max(dna_dict):
    """
    Compares GC content for each sequence.
    Returns ID of the sequence with the highest GC content.
    """
    max_val = 0
    id = ""
    for key, val in dna_dict.items():
        if gc_content(val) > max_val:
            max_val = gc_content(val)
            id = key
    
    return id[1:], round(max_val, 6)


def main():
    with open("gc_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            contents = f.read().split()
            sequences = parse_fasta(contents)
            seq_id, gc = get_max(sequences)

            output.write(seq_id)
            output.write("\n")
            output.write(str(gc))


if __name__ == "__main__":
    main()