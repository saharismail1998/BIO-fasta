import matplotlib.pyplot
from Bio import Seq
from pathlib import Path

# Read the file
file_content = Path("GCA_000001405.29.fasta").read_text()

# Remove lines starting with '>'
#cleaned_sequence = "".join(line for line in file_content.splitlines() if not line.startswith('>') )

seq = Seq.Seq(file_content)
c_count = seq.count("C")
g_count = seq.count("G")
t_count = seq.count("T")
a_count = seq.count("A")
print("A",a_count)
print("C",c_count)
print("G",g_count)
print("T",t_count)
matplotlib.pyplot.bar(['A','C','G','T'],[a_count,c_count,g_count,t_count])
matplotlib.pyplot.show()