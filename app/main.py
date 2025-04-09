import streamlit as st
from crud import create_cliente, read_clientes, update_cliente, delete_cliente
import pandas as pd

st.title("E-Shop Brasil - Gestão de Clientes")

st.subheader("Cadastrar Novo Cliente")
with st.form("form_cliente"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    submitted = st.form_submit_button("Salvar")
    if submitted:
        create_cliente({"nome": nome, "email": email, "telefone": telefone})
        st.success("Cliente salvo com sucesso!")

st.subheader("Lista de Clientes")
clientes = read_clientes()
if clientes:
    for cliente in clientes:
        st.markdown(f"**{cliente['nome']}** - {cliente['email']} - {cliente['telefone']}")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Atualizar", key=f"update_{cliente['_id']}"):
                novo_nome = st.text_input("Novo nome", value=cliente['nome'], key=f"nome_{cliente['_id']}")
                update_cliente(cliente['_id'], {"nome": novo_nome})
        with col2:
            if st.button("Excluir", key=f"delete_{cliente['_id']}"):
                delete_cliente(cliente['_id'])
                st.warning("Cliente excluído")
