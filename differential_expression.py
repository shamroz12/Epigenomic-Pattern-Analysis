import pandas as pd
from scipy.stats import ttest_ind

def differential_expression():
    rnaseq_data = pd.read_csv("results/TCGA-BRCA_log2_fpkm.csv", index_col=0)
    tumor_samples = rnaseq_data.columns[0:500]  # Placeholder
    normal_samples = rnaseq_data.columns[500:1000]  # Placeholder
    p_values = []
    for gene in rnaseq_data.index:
        _, p_value = ttest_ind(rnaseq_data.loc[gene, tumor_samples], rnaseq_data.loc[gene, normal_samples])
        p_values.append(p_value)
    p_values_adj = pd.Series(p_values).apply(lambda x: min(x * len(p_values), 1.0))
    results = pd.DataFrame({'p_value': p_values, 'adjusted_p_value': p_values_adj})
    results.to_csv("results/differential_expression.csv")
    print("Differential expression analysis results saved to results/differential_expression.csv")

if __name__ == "__main__":
    differential_expression()
