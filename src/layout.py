import dash_core_components as dcc
import dash_html_components as html

from . import global_vars as gv
from . import layout_helper
import plotly.graph_objects as go


def time_value_tab():
    defaultGraph = go.Figure()
    defaultGraph.update_layout(
        {
            'title': {
                'text': 'Payouts',
            },
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'xaxis': {
                'title': {
                    'text': 'Period',
                },
                'gridcolor': 'rgb(225,225,225)',
                'linecolor': 'black',
                'zerolinecolor': 'rgb(225,225,225)',
            },
            'yaxis': {
                'title': {'text': 'Cash Flow'},
                'gridcolor': 'rgb(225,225,225)',
                'linecolor': 'black',
                'zerolinecolor': 'rgb(225,225,225)',
            },
            'font': {
                'color': 'rgb(50,50,50)'
            }
        }
    )

    inputs = html.Div([
        html.Div([
            html.Label('Periods (n)'),
            dcc.Input('pv-n', type='number', min=0, value=0)
        ]),
        html.Div([
            html.Label('Discount Rate (APR)'),
            dcc.Input('pv-discount-rate', type='number', min=0, value=0),
        ])
    ], className='row', style={'width': '100%'})

    body = html.Div([
        html.Div([
            html.H3('Cash Flow'),
            layout_helper.create_datatable('pv-cash-flow-table',  height='5vh', data=[{'0': 0}],
                                           editable=True)
        ]),
        html.Div([
            html.H3('Present Value'),
            html.Div([
                layout_helper.create_datatable('pv-present-value-table', columns=['period', 'value'], className='width-50',
                                               colMap=gv.colMapping, height='5vh', editable=True, pages=13),
                dcc.Graph(id='pv-graph',
                          figure=defaultGraph,
                          className='width-50 height-100')
            ], className='row table')])
    ])

    pvTab = html.Div([
        inputs,
        body
    ], style={
        'width': '100%',
        'paddingBottom': '50px'
    },
        className='section'
    )

    return pvTab


def layout():
    """Web-app HTML layout structure"""
    layout = html.Div([
        layout_helper.title_bar("Time-Value Calculator"),
        time_value_tab()
    ], className='app')

    return layout
