# Epigenomic Pattern Analysis

This project analyzes publicly available **ChIP-seq** (H3K27ac) and **RNA-seq** (BRCA) datasets to study the interplay between chromatin modifications and gene expression regulation in cancer.

## Project Structure
- `data/`: Scripts to download datasets from public databases (ENCODE, TCGA).
- `scripts/`: Python scripts for preprocessing, analysis, and visualization.
- `notebooks/`: Jupyter notebooks for exploratory analysis and visualization.
- `results/`: Output files from analyses.
- `requirements.txt`: Python dependencies.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download data:
   ```bash
   python data/download_chipseq.py
   python data/download_rnaseq.py
   ```
3. Run analysis:
   ```bash
   python scripts/preprocess.py
   python scripts/differential_expression.py
   python scripts/chipseq_analysis.py
   ```
4. Explore results in `notebooks/epigenomic_analysis.ipynb`.
