import pandas as pd

df = pd.read_csv('br_ibge_censo_2022_alfabetizacao_grupo_idade_sexo_raca (1).csv')

print(df.head())

por_alfabetizacao = (
    df.groupby('alfabetizacao')['populacao']
    .sum()
    .reset_index(name='total_populacao')
)

print(por_alfabetizacao)

raca_alfa = (
    df.groupby(['alfabetizacao', 'cor_raca'])['populacao']
    .sum()
    .reset_index(name='total_populacao')
    .sort_values(['alfabetizacao', 'total_populacao'], ascending=[True, False])
)

print(raca_alfa)

sexo_alfa = (
    df.groupby(['alfabetizacao', 'sexo'])['populacao']
    .sum()
    .reset_index(name='total_populacao')
)

print(sexo_alfa)

pivot = df.pivot_table(
    index='cor_raca',
    columns='alfabetizacao',
    values='populacao',   # Somar a população
    aggfunc='sum',
    fill_value=0             # grupos sem registros aparecem como 0
)

print(pivot)

proporcao = pivot.div(pivot.sum(axis=1), axis=0).round(3) * 100
print(proporcao)

