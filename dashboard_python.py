from dash import Dash, html, dcc, Output, Input
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('Vendas.xlsx')

#Criando gráfico
fig = px.bar(df, x='Produto', y='Quantidade', color='ID Loja', barmode='group')
op = list(df['ID Loja'].unique())
op.append('Todas as lojas')

app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H2(children='Gráfico com o faturamento de todos os produtos separados por loja.'),
    html.Div(children='''
        Obs: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),

    dcc.Dropdown(op, value='Todas as lojas', id='lista_lojas'),

    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)

def update_output(value):
    if value == 'Todas as lojas':
        fig = px.bar(df, x='Produto', y='Quantidade', color='ID Loja', barmode='group')
    else:
        tabela_filtro = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtro, x='Produto', y='Quantidade', color='ID Loja', barmode='group')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)