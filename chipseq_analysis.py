import pyBigWig
import numpy as np
import matplotlib.pyplot as plt

def chipseq_analysis():
    bw = pyBigWig.open("data/H3K27ac.ENCFF000ABC.bigWig")
    chrom = "chr1"
    start = 100000
    end = 100100
    signal = np.array(bw.values(chrom, start, end))
    plt.figure(figsize=(8,6))
    plt.plot(np.arange(start, end), signal)
    plt.title("H3K27ac ChIP-seq Signal")
    plt.xlabel("Genomic Position")
    plt.ylabel("Signal Intensity")
    plt.savefig("results/chromatin_association.png")
    print("ChIP-seq analysis plot saved to results/chromatin_association.png")

if __name__ == "__main__":
    chipseq_analysis()
