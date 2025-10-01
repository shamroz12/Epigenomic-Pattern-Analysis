import os
import urllib.request

def download_rnaseq():
    url = "https://portal.gdc.cancer.gov/files/TCGA-BRCA.htseq_fpkm.tsv"
    output_path = "data/TCGA-BRCA.htseq_fpkm.tsv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    urllib.request.urlretrieve(url, output_path)
    print(f"Downloaded TCGA-BRCA RNA-seq data to {output_path}")

if __name__ == "__main__":
    download_rnaseq()
