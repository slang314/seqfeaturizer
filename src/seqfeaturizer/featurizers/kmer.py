
from collections import Counter
from itertools import product

def generate_kmers(seq: str, k: int = 3) -> dict:
    seq = seq.upper()
    kmers = [seq[i:i+k] for i in range(len(seq)-k+1) if 'N' not in seq[i:i+k]]
    counts = Counter(kmers)
    total = sum(counts.values())
    all_kmers = [''.join(p) for p in product('ATGC', repeat=k)]
    return {kmer: counts.get(kmer, 0) / total if total else 0.0 for kmer in all_kmers}
