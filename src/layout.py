from . import layout_helper
import dash_core_components as dcc
import dash_html_components as html


def present_value_tab():
    inputs = html.Div([
        html.Div([
            html.Label('Number of periods'),
            dcc.Input('pv-n', type='number', min=1, value=1)
        ]),
        html.Div([
            html.Label('Discount Rate (APR)'),
            dcc.Input('pv-discount-rate', type='number', min=0),
        ])
    ], className='row', style={'width':'100%'})

    body = html.Div([
        layout_helper.create_datatable('pv-cash-flows', columns=['1','2']),
        html.Div(layout_helper.create_datatable('pv-output', columns=['1','2']), className='table')
    ], className='center table')
    
    pvTab = html.Div([
        inputs,
        body
    ], style={'width':'100%'})

    return pvTab


def future_value_tab():
    fvTab = html.Div()

    return fvTab


def bond_value_tab():
    bvTab = html.Div()

    return bvTab


def layout():
    """Web-app HTML layout structure"""
    layout = html.Div([
        layout_helper.title_bar("Bond-Value Calculator"),
        layout_helper.tab_setup('bond-value-tab',
                                ['Present-Value Calculator',
                                    'Future-Value Calculator', 'Bond-Value Calculator'],
                                [present_value_tab(), future_value_tab(), bond_value_tab()])
    ], className='app')

    return layout
