class DNA:

  def __init__(self,string):
    self.string = string

  def count_nucleotides(self):
    dict1 = {}
    dict1['A'] = self.string.count('A')
    dict1['C'] = self.string.count('C')
    dict1['G'] = self.string.count('G')
    dict1['T'] = self.string.count('T')
    return dict1
  def calculate_complement(self):
    concatenate = ''
    for i in self.string:
      if i=='A':
        i='T'
      elif i=='T':
        i='A'
      elif i=='C':
        i='G'
      else:
        i='C'
      concatenate+=i
    return concatenate

dna1 = DNA('GATATATGCATATACTT')
print(dna1.count_nucleotides())
