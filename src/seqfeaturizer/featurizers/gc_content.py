
def gc_content(seq: str) -> float:
    seq = seq.upper()
    gc_count = seq.count('G') + seq.count('C')
    valid_bases = sum(seq.count(base) for base in 'ATGC')
    return (gc_count / valid_bases) * 100 if valid_bases else 0.0
