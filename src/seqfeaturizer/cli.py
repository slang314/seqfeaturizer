import argparse
from .runner import run_feature_extraction

def main():
    parser = argparse.ArgumentParser(description="Extract features from FASTA sequences.")
    parser.add_argument('--input', '-i', required=True, help='Path to input FASTA file')
    parser.add_argument('--output', '-o', required=True, help='Output CSV path')
    parser.add_argument('--features', '-f', nargs='+', choices=['gc', 'kmer', 'entropy'], required=True)
    parser.add_argument('--k', type=int, default=3, help='k-mer size (default: 3)')
    parser.add_argument('--plot', choices=['entropy-trace'], help='Plot type to generate')
    parser.add_argument('--window-size', type=int, default=50, help='Sliding window size (default: 50)')
    parser.add_argument('--step-size', type=int, default=10, help='Sliding window step size (default: 10)')
    parser.add_argument('--window-entropy-filter', nargs=2, metavar=('lt|gt', 'value'),
                        help='Filter full sequences with any entropy window matching the condition.')
    parser.add_argument('--extract-entropy-windows', nargs=2, metavar=('lt|gt', 'value'),
                        help='Extract window subsequences whose entropy matches the threshold.')

    args = parser.parse_args()

    # Extract window subsequences
    if args.extract_entropy_windows:
        from .featurizers.entropy import sliding_entropy
        from .runner import parse_fasta

        op, threshold = args.extract_entropy_windows
        threshold = float(threshold)
        windowed_hits = []

        for seq_id, seq in parse_fasta(args.input):
            entropy_windows = sliding_entropy(seq, window=args.window_size, step=args.step_size, seq_id=seq_id)
            for i, ent in entropy_windows:
                if (op == 'lt' and ent < threshold) or (op == 'gt' and ent > threshold):
                    window_seq = seq[i:i + args.window_size]
                    header = f">{seq_id}|start:{i}|end:{i + args.window_size}|entropy:{ent:.2f}"
                    windowed_hits.append((header, window_seq))

        with open("entropy_filtered_windows.fa", "w") as out:
            for header, subseq in windowed_hits:
                out.write(f"{header}\n{subseq}\n")

        print(f"[INFO] Extracted {len(windowed_hits)} window(s) matching entropy {op} {threshold}. Saved to entropy_filtered_windows.fa")

    # Extract full sequences that contain matching windows
    if args.window_entropy_filter:
        from .featurizers.entropy import sliding_entropy
        from .runner import parse_fasta

        op, threshold = args.window_entropy_filter
        threshold = float(threshold)
        filtered = []

        for seq_id, seq in parse_fasta(args.input):
            entropy_windows = sliding_entropy(seq, window=args.window_size, step=args.step_size, seq_id=seq_id)
            if (op == 'lt' and any(ent < threshold for _, ent in entropy_windows)) or \
               (op == 'gt' and any(ent > threshold for _, ent in entropy_windows)):
                filtered.append((seq_id, seq))

        with open("window_filtered_sequences.fa", "w") as out:
            for seq_id, seq in filtered:
                out.write(f">{seq_id}\n{seq}\n")

        print(f"[INFO] {len(filtered)} sequences had at least one window with entropy {op} {threshold}. Saved to window_filtered_sequences.fa")

    # Extract selected features to CSV
    run_feature_extraction(args.input, args.output, args.features, args.k)

    # Optional entropy trace plot
    if args.plot == 'entropy-trace':
        from .visualizer import plot_entropy_trace
        from .featurizers.entropy import sliding_entropy
        from .runner import parse_fasta

        traces = {}
        for seq_id, seq in parse_fasta(args.input):
            entropy_points = sliding_entropy(seq, window=args.window_size, step=args.step_size, seq_id=seq_id)
            traces[seq_id] = (entropy_points, seq)  # include full sequence too

        plot_entropy_trace(traces, window_size=args.window_size)


if __name__ == '__main__':
    main()
