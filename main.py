# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import search
import extract  as script
import streamlit as st
import util
import os as sys
import data

file_names = ['ServicoAeItem', 'ServicoAeSubItem', 'Entidade', 'Pessoa', 'Operador']
diretory = st.text_input('Caminho dos Arquivos:',"C:\\Users\\richielly.carvalho\\Desktop\\ExtractFrotasUnificaBalsaNova\\")


menu = st.sidebar.radio('Exportador Arquivos',('Exportador do Banco', 'Exportador de Arquivo'))


 #           util.edit_file(sys.getcwd() + '\\venvimportadorNota\extract.py', all_script)

st.sidebar.header("Opções:")
arqs = []
for arq in script.selects.keys():
    if (st.sidebar.checkbox(arq, arq)):
        arqs.append(arq)
st.header('Todal de arquivos selecionados: ' + str(len(arqs)))
if st.button("Gerar"):
    if len(arqs) > 0 :
        for select in arqs:
            sel = search.Search()

            util.create_file(diretory, str(select) + '.txt', sel.select(str(script.selects[select])))

if menu == 'Exportador Arquivo':
    all_data = data.DataSheet(diretory)

    sheets = all_data.load_name_sheets()

    data_info = all_data.load_data_excel(all_data.diretory, sheets[1], 10000)

    print(sheets[1])

    st.table(data_info.head(data_info.index.stop+1))