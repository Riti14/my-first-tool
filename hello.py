print("Hello from my first bioinformatics tool!")

dna = "ATGCGCATAT"
gc = dna.count("G") + dna.count("C")
print("GC content:", 100 * gc / len(dna), "%")
