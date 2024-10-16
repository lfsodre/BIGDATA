import streamlit as st          # BIBLIOTECA PARA DASHBOARDS
import pandas as pd             # BIBLIOTECA PARA DADOS
import plotly.express as px     # BIBLIOTECA PARA GRÁFICOS

st.set_page_config(layout="wide")

df = pd.read_csv("supermarket_sales.csv",sep=";", decimal=",")      # SEPARAR DADOS POR ';' E DECIMAL POR ','
df["Date"] = pd.to_datetime(df["Date"])                             # TRANSFORMA OS DADOS DA COLUNA EM DATA
df=df.sort_values("Date")                                           # ORDENAR OS DADOS POR DATA

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))  #LÓGICA PARA SELECIONAR O MÊS E O ANO
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]  # SELECIONAR MÊS

col1, col2 = st.columns(2)              # SEPARA EM COLUNAS
col3, col4, col5 = st.columns(3)

# CORES PERSONALIZADAS
custom_colors = ["#FF204E", "#A0153E", "#5D0E41", "#AB63FA", "#FFA15A", "#19D3F3", "#FF6692"]

# GRÁFICO FATURAMENTO POR DIA
fig_date = px.bar(df_filtered,
                  x="Date", 
                  y="Total", 
                  color="City", 
                  title="Faturamento por dia",
                  color_discrete_sequence=custom_colors)
col1.plotly_chart(fig_date, use_container_width=True)

# GRÁFICO FATURAMENTO POR PRODUTO
fig_prod = px.bar(df_filtered, 
                  x="Date", 
                  y="Product line", 
                  color="City", 
                  title="Faturamento por tipo de produto", 
                  orientation="h",
                  color_discrete_sequence=custom_colors)
col2.plotly_chart(fig_prod, use_container_width=True)

# GRÁFICO FATURAMENTO POR FILIAL
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, 
                  x="City", 
                  y="Total",
                  color="City",
                  title="Faturamento por Filial",
                  color_discrete_sequence=custom_colors)
col3.plotly_chart(fig_city, use_container_width=True)

# GRÁFICO FATURAMENTO POR TIPO DE PAGAMENTO
fig_kind = px.pie(df_filtered, 
                  values="Total",
                  names="Payment",
                  title="Faturamento por tipo de pagamento",
                  color_discrete_sequence=custom_colors)
col4.plotly_chart(fig_kind, use_container_width=True)

# GRÁFICO AVALIAÇÃO
city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, 
                  x="City",
                  y="Rating",
                  color="City",
                  title="Avaliação",
                  color_discrete_sequence=custom_colors)
col5.plotly_chart(fig_rating, use_container_width=True)

#----COMANDO PARA INICIAR APLICAÇÃO----#
# python -m streamlit run dashboard.py #