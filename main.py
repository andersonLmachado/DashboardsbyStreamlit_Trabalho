import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Compulog", page_icon=":watch:", layout="wide")

st.title("Controle Logístico :watch:")

st.sidebar.title("Menu")
pageSelect = st.sidebar.selectbox("Selecione a opção:", ["Painel Central","Viagens","Agendamentos","Portaria"])

if pageSelect == "Painel Central":
    st.divider()
    st.header("Painel Central :mag:")
    st.write("Aqui você pode ver os **indicadores** da sua empresa.")
    st.divider()
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    col1.metric(label="Total de Ofertas", value=1200, delta=10)
    col2.metric(label="Agendamentos", value=500, delta=-5)
    col3.metric(label="Ofertas em PNA", value=300, delta=3)
    col4.metric(label="Viagens em Andamento", value=200, delta=-5)
    col5.metric(label="Viagens em Carregamento", value=100, delta=-2)
    col6.metric(label="Viagens Canceladas", value=50, delta=12)
    col7.metric(label="Viagens Finalizadas", value=10, delta=15)
    st.divider()
    #Gráficos
    cold1, cold2, cold3 = st.columns(3)
    with cold1:
        st.subheader("Ofertas")
        data_df = pd.DataFrame({
            "Ofertas": [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100]
        })
        st.line_chart(data_df)
    
    with cold2:
        st.subheader("Transportadoras")
        data_df = pd.DataFrame({
            "Transportadoras": [500, 450, 400, 350, 300, 250, 200, 150, 100, 50]
        })
        st.bar_chart(data_df)
    with cold3:
        st.subheader("Tempo na Fábrica")
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
        chart_data['col4'] = np.random.choice(['A','B','C'], 20)

        st.scatter_chart(
            chart_data,
            x='col1',
            y='col2',
            color='col4',
            size='col3',
        )
        
elif pageSelect == "Viagens":
    st.divider()
    st.header("Viagens :truck:")
    st.write("Aqui você pode ver as **viagens** da sua empresa.")
    st.divider()

elif pageSelect == "Agendamentos":
    st.divider()
    st.header("Agendamentos :calendar:")
    st.write("Aqui você pode ver os **agendamentos** da sua empresa.")
    st.divider()

elif pageSelect == "Portaria":
    st.divider()
    st.header("Portaria :office:")
    st.write("Aqui você pode ver as **portarias** da sua empresa.")
    st.divider()

