import os
import urllib.request

def download_chipseq():
    url = "https://hgdownload.cse.ucsc.edu/goldenpath/hg19/encodeDCC/wgEncodeRegMarkH3k27ac/ENCFF000ABC.bigWig"
    output_path = "data/H3K27ac.ENCFF000ABC.bigWig"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    urllib.request.urlretrieve(url, output_path)
    print(f"Downloaded H3K27ac ChIP-seq data to {output_path}")

if __name__ == "__main__":
    download_chipseq()
