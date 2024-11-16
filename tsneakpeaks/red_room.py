"""
The Red Room: Visualization components with clickable points
"""

import plotly.graph_objects as go
import numpy as np
from typing import List, Optional
import logging
from pathlib import Path

class Visualizer:
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
"""
The Red Room: Visualization components
"""

import plotly.graph_objects as go
import numpy as np
from typing import List, Optional
import logging
from pathlib import Path

class Visualizer:
    def __init__(self, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)

    def create_figure(self,
                     coords_3d: np.ndarray,
                     labels: np.ndarray,
                     image_paths: List[str],
                     title: str = "TSneakPeaks: A Vision") -> go.Figure:
        
        hover_texts = [
            f'<img src="file://{Path(path).absolute()}" width="100">'
            f"🌲 Image: {Path(path).name}\n"
            f"Colors: {int(np.sum(labels[i]))}"
            for i, path in enumerate(image_paths)
        ]
        
        fig = go.Figure(data=[go.Scatter3d(
            x=coords_3d[:, 0],
            y=coords_3d[:, 1],
            z=coords_3d[:, 2],
            mode='markers',
            marker=dict(
                size=5,
                opacity=0.8,
                color=np.sum(labels, axis=1),
                colorscale=[
                    [0, 'rgb(20,20,20)'],
                    [0.5, 'rgb(140,0,0)'],
                    [1, 'rgb(255,255,255)']
                ],
                colorbar=dict(title="Dimensional Presence"),
                showscale=True
            ),
            hovertemplate='%{text}<extra></extra>',
            text=hover_texts,
            hoverinfo='text'
        )])
        
        fig.update_layout(
            title=dict(text=title, font=dict(size=24)),
            scene=dict(
                xaxis_title="Lodge Dimension α",
                yaxis_title="Lodge Dimension β",
                zaxis_title="Lodge Dimension γ",
                bgcolor='rgb(20,20,20)'
            ),
            width=1000,
            height=800,
            paper_bgcolor='rgb(10,10,10)',
            plot_bgcolor='rgb(10,10,10)',
            font=dict(color='white')
        )
        
        return fig
