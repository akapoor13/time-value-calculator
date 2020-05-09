import dash_table
import dash_core_components as dcc
import dash_html_components as html


def tab_setup(idd, tabLabels, tabChildrens):
    tabChildren = [dcc.Tab(label=label, value=label, children=child)
                   for label, child in zip(tabLabels, tabChildrens)]
    tabs = dcc.Tabs(id='bond-value-tab',
                             value=tabLabels[0], children=tabChildren, vertical=True)
    return tabs


def title_bar(title):
    title = html.Div([
        html.H1(title)
    ], className='title-bar')

    return title


def create_datatable(idd, columns=[], data=[], height='', weight='', colMapping={}, rowDel=False, editable=False,
                     rowSel=False, filterActions='none', sortActions='none', pageSize=10, overflow='auto', overflowx='auto',
                     overflowy='auto', headerAlign='center', dataAlign='center', className='', style={}):

    for i in columns:
        if i not in colMapping:
            colMapping[i] = i

    dt = html.Div(dash_table.DataTable(
        id=idd,
        columns=[{"name": colMapping[i], "id":i} for i in columns],
        data=data,
        row_selectable=rowSel,
        row_deletable=rowDel,
        editable=editable,
        page_size=pageSize,
        style_header={
            "backgroundColor":"rgb(35,35,35)",
            "text_align": headerAlign
        },
        style_data={
            "text_align": dataAlign,
            'color':'rgb(100,100,100)'
        },
        filter_action=filterActions,
        sort_action=sortActions
    ), className=className, style=style)

    return dt
