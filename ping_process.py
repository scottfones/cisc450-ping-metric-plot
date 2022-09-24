'''Processes and plot a file with `ping` output'''
import re

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def main():
    # File with ping output
    file_name = "ping_output.txt"

    rtt_vals = []
    ttl_vals = []
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            # Collect RTT values
            if match := re.search(r"(?<=time\=)\d+", line):
                rtt_vals.append(match.group(0))

            # Collect TTL values
            if match := re.search(r"(?<=ttl\=)\d+", line):
                ttl_vals.append(match.group(0))

    x = np.arange(len(rtt_vals))
    rtt_arr = np.asarray(rtt_vals)
    ttl_arr = np.asarray(ttl_vals)

    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=x,
            y=rtt_arr,
            name="RTT",
            mode="markers",
        ),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=x, y=ttl_arr, name="TTL"),
        secondary_y=True,
    )

    # Configure plot
    fig.update_layout(
        title_text="Ping Metrics: Destiny 2 Server - Hasse Germany",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1,
            xanchor="right",
            x=0.93),
    )

    # Set x-axis title
    fig.update_xaxes(title_text="sample number")

    # Set y-axes titles
    fig.update_yaxes(title_text="Round Trip Time (ms)", secondary_y=False)
    fig.update_yaxes(title_text="Time to Live", secondary_y=True)

    fig.show()


if __name__ == "__main__":
    main()
