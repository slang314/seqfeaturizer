import plotly.graph_objects as go
import textwrap

def plot_entropy_trace(entropy_traces: dict, window_size: int = 50):
    fig = go.Figure()

    for seq_id, (points, seq) in entropy_traces.items():
        if not points:
            continue

        x_vals = []
        y_vals = []
        hover_texts = []

        for start, entropy in points:
            window_seq = seq[start:start + window_size]
            x_vals.append(start)
            y_vals.append(entropy)
            hover_texts.append(
                f"{seq_id}<br>Start: {start}<br>Entropy: {entropy:.2f}<br>{window_seq}"
            )

        wrapped_name="<br>".join(textwrap.wrap(seq_id, width=30))

        fig.add_trace(go.Scatter(
            x=x_vals,
            y=y_vals,
            mode='lines+markers',
            line=dict(width=2),
            marker=dict(size=4),
            text=hover_texts,
            hoverinfo='text',
            name=wrapped_name
        ))

    fig.update_layout(
        title="Sliding Window Shannon Entropy",
        xaxis_title="Window Start Position",
        yaxis_title="Shannon Entropy",
        template="plotly_white"
    )

    fig.show()

