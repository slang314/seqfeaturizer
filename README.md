# SeqFeaturizer

**SeqFeaturizer** is a lightweight Python CLI tool for quickly calculating and visualizing interpretable features from DNA sequences — including:

- GC content
- K-mer frequencies
- **Shannon entropy** (diversity index)

It's perfect for identifying low-complexity regions, comparing diversity across sequences, or exploring structural variation using sliding window entropy plots.

---

## Features

- GC content, k-mer frequency, Shannon entropy
- Sliding window entropy with customizable window & step size
- Plot interactive **entropy trace plots** using Plotly
- Extract only the windows or sequences that meet entropy criteria
- Fast CLI usage, ready for scripting

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/seqfeaturizer.git
cd seqfeaturizer
pip install .
```

Requires: Python 3.7+, `pandas`, `plotly`

---

## Input

FASTA file (`.fa` or `.fasta`) containing one or more sequences.

---

## Output

- `output.csv`: CSV file with feature values for each sequence
- `entropy_filtered_windows.fa`: Sequence windows matching an entropy threshold
- `window_filtered_sequences.fa`: Full sequences containing low/high entropy regions
- Plotly interactive plot (opens in browser)

---

## Example Usage

### 1. Extract entropy & plot diversity across sequences

```bash
seqfeat --input example.fa --output features.csv --features entropy \
  --window-size 100 --step-size 25 \
  --plot entropy-trace
```

### 2. Extract only subsequences with **low entropy**

```bash
seqfeat --input example.fa --output features.csv --features entropy \
  --extract-entropy-windows lt 1.5 \
  --window-size 100 --step-size 25 \
  --plot entropy-trace
```

### 3. Filter full sequences based on entropy regions

```bash
seqfeat --input example.fa --output features.csv --features entropy \
  --window-entropy-filter lt 2.0
```

---

## What Is Shannon Entropy?

Shannon entropy measures sequence diversity. Higher values = more random base usage. Lower values = repeats or homopolymers.

It helps identify:
- Low-complexity regions
- Tandem repeats or microsatellites
- Variable regions in viral genomes or amplicons

---

## Why Use This?

- Instantly compare diversity profiles across genomes
- Visually scan for entropy spikes or drops
- Automate detection of regions of interest via entropy thresholds

---

## Example Input

```fasta
>seq1
ATATATATATATATATATATATATATATATATATATA
>seq2
CGTGACTGATCGATGCGTAGCATCGATCGTACGTA
```

---

## License

MIT © 2024 STEVEN LANG

---

## 🙋 Need Help?

Open an [issue](https://github.com/YOUR_USERNAME/seqfeaturizer/issues) or submit a PR!
