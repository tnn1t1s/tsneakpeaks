from tsneakpeaks import TSneakPeaks
import webbrowser
from pathlib import Path

peaks = TSneakPeaks("test_data")
peaks.load_data()
fig = peaks.visualize()

# Add click handling
def open_image(trace, points, selector):
    if points.point_inds:
        idx = points.point_inds[0]
        path = points.customdata[idx]
        webbrowser.open(f'file://{Path(path).absolute()}')

fig.data[0].on_click(open_image)
fig.show()
