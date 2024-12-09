def create_codon_dict(file_path):
    dictionary = {}
    file = open(file_path)
    rows = file.readlines()
    file.close()
    for row in rows:
      cells = row.strip().split('\t')
      codon = cells[0]
      amino_acid = cells[2]
      dictionary[codon] = amino_acid
    return dictionary
