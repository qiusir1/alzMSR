# test_alzMSR.py

# 1. top‑level import
import alzMSR
print("alzMSR package version:", alzMSR.__version__ if hasattr(alzMSR, "__version__") else "(no __version__)")

# 2. submodule imports
from alzMSR.data_preprocess import load_internal_data, load_and_preprocess_data, filter_genes
from alzMSR.network_analysis import construct_network, get_subnetwork_matrices
from alzMSR.entropy_calculation import comp_srana

print("All imports succeeded.")

# 3. call a lightweight function to confirm it runs
entrez_df, metab_genes, net_df = load_internal_data()
print(f"Loaded internal data: {entrez_df.shape[0]} mappings, "
      f"{len(metab_genes)} metabolic genes, net matrix {net_df.shape}")

# 4. (optional) if you have a small .h5ad on hand:
# adata = load_and_preprocess_data("/some/path", "example.h5ad")
# print("adata shape:", adata.shape)

