import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


def main():
    app.run_server(debug=True)


def generate_table(max_rows=10):
    df_movies = pd.read_csv('data/IMDb movies.csv', low_memory=False)
    df_movies = df_movies.sort_values(by='avg_vote', ascending=False)[['title', 'avg_vote']]
    df_movies = df_movies.loc['Country'].equals('USA')
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df_movies.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df_movies.iloc[i][col]) for col in df_movies.columns
            ]) for i in range(min(len(df_movies), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data/IMDb ratings.csv', low_memory=False)

# fig = px.bar(df, x="us_voters_rating", y="non_us_voters_rating", color="imdb_title_id", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.H4(children='Movies Sample List'),
    generate_table(),

    html.Div(children='''
        Dash: A web application framework for Python.
    ''')

    # dcc.Graph(
    #     id='example-graph',
    #     figure=fig
    # )
])

if __name__ == '__main__':
    main()
