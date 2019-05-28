#1 - Exibir o total de linhas e colunas
import pandas as pd
import seaborn as sb
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90

filename = 'despesa_2018.csv'
df = pd.read_csv(filename)
df.shape



#2 - Descrever o nome de todas as colunas
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90

filename = 'despesa_2018.csv'
df = pd.read_csv(filename)
df.info()



#3 - Agrupar os gastos dos politicos nas eleições 2018 por descrição
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90
filename = 'despesa_2018.csv'
df = pd.read_csv(filename)
df.groupby('descricao').size().sort_values()


#4 - Filtrar os gastos pelo valor com a Descrição 'ativista' somando o número de ocorrências com determinado valor
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90
filename = 'despesa_2018.csv'
df.query('descricao == "ATIVISTA"')['valor'].value_counts().head()


#5 - Filtrar os gastos pelo valor com a Descrição 'militancia' somando o número de ocorrências com determinado valor
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90
df = pd.read_csv(filename)
filename = 'despesa_2018.csv'
df.query('descricao == "MILITANCIA"')['valor'].value_counts().head()


#6 - Geração de grafico com a descrição dos 13 maiores gastos que os politicos tiveram nas eleições 2018
df.groupby('descricao').size().sort_values().tail(13).plot(title='Gastos mais frequentes por politicos nas eleições 2018', kind='barh', figsize=(10,5))


#7 - Função de retorno de quantitdade "Ativistas" e grafico de valor do beneficio
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90
df = pd.read_csv(filename)
filename = 'despesa_2018.csv'
#Função para retornar na tela a soma total de "Ativistas" que foram beneficiados com "Salario" politico    
def PRINT_ATIVISTA(query=None):
    if query:
        df_tmp = df.query(query)
    else:
        df_tmp = df
    total_rows = len(df_tmp)
    unique_rows = len(df_tmp.groupby(['descricao']))
    unique_rows_same_date = len(df_tmp.groupby(['valor']))
    reducao_fila = (total_rows - unique_rows) / total_rows
    print('    Numero total de ativista pagos por politicos nas eleições 2018:', total_rows)

#Geração de grafico Ativistas Pagos por politicos nas eleições 2018, retornando valor pago e quantidade de beneficiarios
df.query('descricao == "ATIVISTA"')['valor'].value_counts().head().plot(title='Ativistas Pagos por politicos nas eleições 2018', kind='barh', figsize=(10,5))
#Definindo descrição do Eixo X do grafico
plt.xlabel("Beneficiarios que receberam o valor")
#Definindo descrição do Eixo Y do grafico
plt.ylabel("Valor pago aos beneficiarios")
#Chamando a função
PRINT_ATIVISTA('descricao == "ATIVISTA"')


#8 - Função de retorno de quantitdade "Militantes" e grafico de valor do beneficio
low_memory=False
%matplotlib inline
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90
df = pd.read_csv(filename)

filename = 'despesa_2018.csv'

#Função para retornar na tela a soma total de "Militantes" que foram beneficiados com "Salario" politico
def PRINT_MILITANTE(query=None):
    if query:
        df_tmp = df.query(query)
    else:
        df_tmp = df
    total_rows = len(df_tmp)
    unique_rows = len(df_tmp.groupby(['descricao']))
    unique_rows_same_date = len(df_tmp.groupby(['valor']))
    reducao_fila = (total_rows - unique_rows) / total_rows
    print('    Numero total de militantes pagos por politicos nas eleições 2018:', total_rows)

#Geração de grafico Ativistas Pagos por politicos nas eleições 2018, retornando valor pago e quantidade de beneficiarios
df.query('descricao == "MILITANCIA"')['valor'].value_counts().head().plot(title='Militantes Pagos por politicos nas eleições 2018', kind='barh', figsize=(10,5))

#Definindo descrição do Eixo X do grafico
plt.xlabel("Beneficiarios que receberam o valor")

#Definindo descrição do Eixo Y do grafico
plt.ylabel("Valor pago aos beneficiarios")

#Chamando a função
PRINT_MILITANTE('descricao == "MILITANCIA"')
