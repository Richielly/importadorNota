# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import search
import extract  as script
import streamlit as st
import util
import os as sys
import data

file_names = ['ServicoAeItem', 'ServicoAeSubItem', 'Entidade', 'Pessoa', 'Operador']
diretory = st.text_input('Caminho dos Arquivos:',"C:\\Users\\richielly.carvalho\Downloads\\Notas fiscais.xlsx")


menu = st.sidebar.radio('Exportador Arquivos',('Exportador Banco', 'Exportador Arquivo'))

if menu == 'Exportador Banco':

    ServicoAeItem = st.text_area('ServicoAeItem', script.ServicoAeItem, height=200)
    ServicoAeSubItem = st.text_area('ServicoAeSubItem', script.ServicoAeSubItem, height=200)
    Pessoa = st.text_area('Pessoa', script.Pessoa, height=400)
    Operador = st.text_area('Operador', script.Operador, height=400)
    PapelOperador = st.text_area('PapelOperador', script.PapelOperador, height=400)
    Nota = st.text_area('Nota', script.Nota, height=400)

    if(st.button('Alterar')):

        all_script = 'ServicoAeItem = """' + ServicoAeItem + '""" \n\n' + 'ServicoAeSubItem = """' + ServicoAeSubItem + '"""\n\n' + 'Pessoa = """' + Pessoa + '"""\n\n' + \
                 'Operador = """' + Operador + '""" \n\n' + 'PapelOperador = """' + PapelOperador + '""" \n\n' + 'Nota = """' + Nota + '""" \n\n'

        sel = search.Search()

        util.edit_file(sys.getcwd() + '\\venvimportadorNota\extract.py', all_script)

        util.create_file(diretory, 'ServicoAeItem'+'.txt', sel.select(script.ServicoAeItem))
        util.create_file(diretory, 'ServicoAeSubItem' + '.txt', sel.select(script.ServicoAeSubItem))
        util.create_file(diretory, 'Pessoa' + '.txt', sel.select(script.Pessoa))
        util.create_file(diretory, 'Operador' + '.txt', sel.select(script.Operador))
        util.create_file(diretory, 'PapelOperador' + '.txt', sel.select(script.PapelOperador))
        util.create_file(diretory, 'Nota' + '.txt', sel.select(script.Nota))

if menu == 'Exportador Arquivo':
    all_data = data.DataSheet(diretory)

    sheets = all_data.load_name_sheets()

    data_info = all_data.load_data_excel(all_data.diretory, sheets[1], 10000)

    print(sheets[1])

    st.table(data_info.head(data_info.index.stop+1))


