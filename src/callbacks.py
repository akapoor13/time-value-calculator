import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
from dash.dependencies import Output, Input, State
import dash_table.FormatTemplate as FormatTemplate
from . import time_value_calculator as tvc


def callbacks(app):
    time_value_callbacks(app)


def time_value_callbacks(app):
    @app.callback(
        Output('pv-present-value-table', 'columns'),
        [
            Input('pv-n', 'id')
        ]
    )
    def initalization(_):
        columns = [
            {
                'name': 'Period',
                'id': 'period',
                'type': 'numeric',
            },
            {
                'name': 'Value',
                'id': 'value',
                'type': 'numeric',
                'format': FormatTemplate.money(2)
            }
        ]

        return columns

    @app.callback(
        Output('pv-graph', 'figure'),
        [
            Input('pv-present-value-table', 'data')
        ],
        [
            State('pv-cash-flow-table', 'data')
        ]
    )
    def update_cashflow_graph(dataDCF, dataCF):
        if dataCF == [] or dataDCF == []:
            raise PreventUpdate

        periodDCF = [i['period'] for i in dataDCF]
        dcf = [i['value'] if i else 0 for i in dataDCF]

        periodCF = list(dataCF[0].keys())
        cf = list(dataCF[0].values())

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=periodDCF, y=dcf,
                                 mode='markers', name='Discounted'))
        fig.add_trace(go.Scatter(x=periodCF, y=cf,
                                 mode='markers', name='Cash Flows'))

        fig.update_layout(
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

        return fig

    @app.callback(
        Output('pv-cash-flow-table', 'columns'),
        [
            Input('pv-n', 'value')
        ]
    )
    def update_table_columns(cols):
        if cols is None:
            raise PreventUpdate

        columns = []

        for i in range(cols+1):
            columns.append({
                'name': str(i),
                'id': str(i),
                'type': 'numeric',
                'format': FormatTemplate.money(2)
            })

        return columns

    @app.callback(
        Output('pv-present-value-table', 'data'),
        [
            Input('pv-cash-flow-table', 'derived_virtual_data'),
            Input('pv-n', 'value'),
            Input('pv-discount-rate', 'value')
        ]
    )
    def update_cash_flow_table(data, n, discountRate):
        if n == None or data == None or discountRate == None:
            raise PreventUpdate

        value = data[0]
        cashFlows = []

        for i in range(n+1):
            amount = 0

            for period, cash in value.items():
                if cash == None:
                    continue

                if int(period) < i:  # future value
                    amount += tvc.calculator_future_value(
                        float(cash), discountRate/100, i-int(period))
                else:
                    amount += tvc.calculator_present_value(
                        float(cash), discountRate/100, int(period)-i)

            cashFlows.append({'period': i, 'value': round(amount, 2)})

        return cashFlows
