import pandas as pd

def preprocess_rnaseq():
    rnaseq_data = pd.read_csv("data/TCGA-BRCA.htseq_fpkm.tsv", sep="\t", index_col=0)
    rnaseq_data_log = rnaseq_data.apply(lambda x: pd.np.log2(x + 1))
    rnaseq_data_log.to_csv("results/TCGA-BRCA_log2_fpkm.csv")
    print("Preprocessed RNA-seq data saved to results/TCGA-BRCA_log2_fpkm.csv")

if __name__ == "__main__":
    preprocess_rnaseq()
