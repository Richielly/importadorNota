
def create_file(diretory, file_name,itens_extract):

    try:
        file = open(diretory + '\\' + file_name, 'r+', encoding="ANSI")
    except FileNotFoundError:
        file = open(diretory + '\\' + file_name, 'w')
        for line in itens_extract:
            file.writelines(line[0]+'\n')
    file.close()
    
def edit_file(file_name,itens_extract):

    with open(file_name, 'w',encoding="ANSI") as file:
        for line in itens_extract:
            file.write(line[0])
