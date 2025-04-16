
import math
from collections import Counter

def shannon_entropy(seq: str) -> float:
    seq = seq.upper()
    counts = Counter(seq)
    total = sum(counts.values())
    return -sum((count/total) * math.log2(count/total) for count in counts.values() if count > 0) if total else 0.0

def sliding_entropy(seq: str, window: int = 50, step: int = 10, seq_id: str = "") -> list:
    values = []
    seq_len = len(seq)
    if seq_len < window:
        print(f"[INFO] Sequence '{seq_id}' is shorter than the window size ({window}). Using full sequence length ({seq_len}) as the window instead.")
        window = seq_len
    for i in range(0, seq_len - window + 1, step):
        window_seq = seq[i:i + window]
        entropy = shannon_entropy(window_seq)
        values.append((i, entropy))
    return values
