import dash
from .layout import layout
from .callbacks import callbacks

# Web-App Setup
app = dash.Dash(__name__)

app.layout = layout() # Setup web-app UI
callbacks(app) # Setup web-app interactivity
