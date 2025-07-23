# AD-associated cell type-specific Metabolic Signaling Entropy (alzMSR)

## Overview

AD-associated cell type-specific Metabolic Signaling Entropy (alzMSR) is a Python package designed for the analysis of single-cell RNA sequencing data with a focus on entropy calculations within metabolic gene networks. The package offers tools for data preprocessing, network analysis, and entropy computation. Reference: Cell type-specific master metabolic regulators of Alzheimer’s disease. Yunguang Qiu, Yuan Hou, Liam Wetzel, Jessica Z.K. Caldwell, Xiongwei Zhu, Andrew A. Pieper, Tian Liu, Feixiong Cheng. bioRxiv 2025.07.11.664443; doi: https://doi.org/10.1101/2025.07.11.664443

## Installation

Clone the repository:

```bash
git clone

cd alzMSR
pip install .

```

## Usage

# Import the package:
```python
from alzMSR.data_preprocess import load_and_preprocess_data, filter_genes, load_internal_data
from alzMSR.network_analysis import construct_network, get_subnetwork_matrices
from alzMSR.entropy_calculation import comp_srana
```

# Load internal data
```python
entrez_id, metabolic_Gene, network_data = load_internal_data()

```

# Load and preprocess data

```python
# Example usage

path = '/path/to/directory'
file_name = 'my_data_file.h5ad'
adata = load_and_preprocess_data(path, file_name) # adata is a normalized AnnData object.

''' note: please specify your groups to be calculated, e.g., 
cells = pd.read_csv("%s/cells.tsv" % PATH_I, sep="\t")
adata.obs["Diganosis"] =  cells["diagnosis"].values
adata.obs["celltype"] =  cells["celltype"].values
adata.obs["braak_diff"] =  cells["braak_diff"].values'''
```


# Filter genes and prepare network data
```python
adata_filtered, network_data_filtered = filter_genes(adata, entrez_id, metabolic_Gene, network_data)
```

# Construct network and get subnetwork matrices

```python
subgraph = construct_network(network_data_filtered)
adjMC_m, expMC_m = get_subnetwork_matrices(subgraph, adata_filtered)
```

# Compute entropy
```python
entropy_results = comp_srana(adjMC_m, expMC_m, local=True, mc_cores=16)
# The results now include 'SR', 'locS', 'nlocS', and 'expMC_var'
```
