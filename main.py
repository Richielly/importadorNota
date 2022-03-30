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

import minerador

file_names = ['ServicoAeItem', 'ServicoAeSubItem', 'Entidade', 'Pessoa', 'Operador']



menu = st.sidebar.radio('Exportador Arquivos',('Exportador do Banco', 'Exportador de Arquivo', 'Minerar'))


 #           util.edit_file(sys.getcwd() + '\\venvimportadorNota\extract.py', all_script)

st.sidebar.header("Opções:")
if menu == 'Exportador do Banco':
    diretory = st.text_input('Caminho dos Arquivos:',
                             "C:\\Users\\richielly.carvalho\\Desktop\\ExtractFrotasUnificaBalsaNova\\")
    arqs = []
    for arq in script.selects.keys():
        if (st.sidebar.checkbox(arq, arq)):
            arqs.append(arq)
    st.header('Todal de arquivos selecionados: ' + str(len(arqs)))
    if st.button("Gerar"):
        if len(arqs) > 0 :
            for select in arqs:
                sel = search.Search()

                # util.create_file(diretory, str(select) + '.txt', sel.select(str(script.selects[select])))

if menu == 'Exportador Arquivo':
    all_data = data.DataSheet(diretory)

    sheets = all_data.load_name_sheets()

    data_info = all_data.load_data_excel(all_data.diretory, sheets[1], 10000)

    print(sheets[1])

    st.table(data_info.head(data_info.index.stop+1))

if menu == 'Minerar':
    informe = st.empty
    like = st.checkbox("esta contido na pesquisa")

    pesquisa_coluna = st.text_input('Encontrar tabela por nome de coluna: ')
    if st.button('Pesquisar:'):
        tabela_coluna = minerador.colunas(pesquisa_coluna, like)
        st.header(str(len(tabela_coluna)) + ' tabela ' + ' com a colunas pesquisada')
        for tabela in tabela_coluna:
            st.info('select * from bethadba.' + tabela[0])

    pesquisa = st.text_input('Pesquisa por dados: ')

    if st.button('Pesquisar'):
        tabelas, dados = minerador.minenar(pesquisa,like)
        tabelas_encontradas = (set(tabelas))
        st.header(str(len(tabelas_encontradas)) + ' tabela, ' + ' com ' + str(len(dados)) + 'registros.')


        for select in tabelas_encontradas:
            st.success('select * from bethadba.' + str(select))
        for dado in dados:
            st.info(dado)






