from dash import Dash, html,dcc,Output,Input
import pandas as pd
import plotly.express as px

app = Dash('__name___')

df = pd.read_excel("Vendas2004.xlsx")

fig = px.bar(df, x="Genre", y="Global_Sales", color="Platform", barmode="group")

opcoes = list(df['Platform'].unique())

opcoes.append("Todas as plataformas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento por gênero'),
    html.H2(children='Gráfico com o faturamento de todos os gêneros em 2004 separados por console'),
    dcc.Dropdown(opcoes, value='Todas as lojas', id='lista_lojas'),
    dcc.Graph(
        id='grafico_quantidade_produto',
        figure=fig
    )
])

@app.callback(
    Output('grafico_quantiade_produto', 'figura'),
    Input('lista_generos', 'value')
)

def update_output(value):
    if value == "Todos as plataformas":
        fig = px.bar(df, x="Genre", y="Global_Sales", color="Platform", barmode="group")
    else:
        tabela_filtrada = df.loc[df["Platform"] == value, :]
        fig = px.bar(tabela_filtrada, x="Genre", y="Global_Sales", color="Platform", barmode="group")

    return fig

if __name__ == '__main__':
    app.run(debug=True)