
import pandas as pd
from .featurizers.gc_content import gc_content
from .featurizers.kmer import generate_kmers
from .featurizers.entropy import shannon_entropy

def parse_fasta(fasta_path):
    with open(fasta_path, 'r') as f:
        seqs = []
        seq_id, seq = None, []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if seq_id:
                    seqs.append((seq_id, ''.join(seq)))
                seq_id = line[1:]
                seq = []
            else:
                seq.append(line)
        if seq_id:
            seqs.append((seq_id, ''.join(seq)))
    return seqs

def run_feature_extraction(fasta_path, output_path, features, k=3):
    records = parse_fasta(fasta_path)
    all_features = []
    for seq_id, seq in records:
        row = {'id': seq_id}
        if 'gc' in features:
            row['gc_content'] = gc_content(seq)
        if 'entropy' in features:
            row['shannon_entropy'] = shannon_entropy(seq)
        if 'kmer' in features:
            row.update(generate_kmers(seq, k))
        all_features.append(row)
    df = pd.DataFrame(all_features)
    df.to_csv(output_path, index=False)
    print(f"Feature extraction complete. Results saved to: {output_path}")
