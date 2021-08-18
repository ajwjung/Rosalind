"""
Introduction to Protein Databases
Link to problem: http://rosalind.info/problems/dbpr/

Given: The UniProt ID of a protein.
Return: A list of biological processes in which the protein is involved (biological processes are found in a subsection of the protein's "Gene Ontology" (GO) section).
"""

from urllib.request import urlopen
import re

def main():
    with open("dbpr_output.txt", "w") as output:
        with open("temp_input.txt") as f:
            id = f.read().strip()
            handle = "http://www.uniprot.org/uniprot/" + id + ".txt"

            html_bytes = urlopen(handle).read()
            html = html_bytes.decode("utf-8")
            # Search for lines containing "GO; GO:ID_number; P:function"
            results = re.findall("GO:[0-9]+; P:([\w|\s]+)", html)

            for r in results:
                output.write(r + "\n")


if __name__ == "__main__":
    main()