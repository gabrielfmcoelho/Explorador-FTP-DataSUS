import datasus_ftp_modulo

OPCOES = {1:'Listar conteudo do diretorio', 2:'Acessar diretorio', 3:'Voltar diretorio', 4:'Download de arquivo do diretorio', 5:'Pesquisar arquivo por data',0:'Encerrar programa'}
PATH_DOWNLOAD = './Downloads'

def menu(conexaoftp, selecao):
    if(selecao==1):
        conexaoftp.listar_diretorio()
    elif(selecao==2):
        conexaoftp.acessar_diretorio()
    elif(selecao==3):
        conexaoftp.voltar_diretorio()
    elif(selecao==4):
        conexaoftp.download_arquivo()
    elif(selecao==5):
        conexaoftp.pesquisar_arquivo_data()
   

def main():
    conexaoftp = datasus_ftp_modulo.Datasus_ftp()

    while(True):
        print(f"""\n----------------------------------------------
Explorador de Arquivos do Servidor FTP DataSUS
----------------------------------------------\n
DIRETORIO ATUAL: {conexaoftp.ftp.pwd()}\n""")

        for opcaoChave, opcaoValor in OPCOES.items():
            print(f'{opcaoChave} - {opcaoValor}')

        while(True):
            selecao = int(input("\nDigite o código da função desejada: "))
            if selecao in OPCOES.keys():
                break
            else:
                print("Código invalido, por favor digite novamente...")

        if(selecao==0):
            print("Encerrando programa...")
            break
        
        menu(conexaoftp, selecao)
        
    conexaoftp.encerrar_conexao()

if __name__ == '__main__':
    main()