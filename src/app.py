import dash
from .layout import layout
from .callbacks import callbacks

# Web-App
app = dash.Dash(__name__)

app.layout = layout() # Web-App UI
callbacks(app)
