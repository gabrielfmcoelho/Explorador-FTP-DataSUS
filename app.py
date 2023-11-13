import datasus_ftp_modulo
import os


OPCOES = {1:'Listar conteudo do diretorio', 2:'Acessar diretorio', 3:'Voltar diretorio', 4:'Download de arquivo do diretorio', 5:'Pesquisar arquivo por data', 6:'Pesquisar arquivo por inicial', 0:'Encerrar programa'}
PATH_DOWNLOAD = './Downloads/'


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
    elif(selecao==6):
        conexaoftp.filtrar_por_inicio_do_arquivo()
   
def fazer_pasta_download():
    if not os.path.exists(PATH_DOWNLOAD):
        os.makedirs(PATH_DOWNLOAD)

def main():
    conexaoftp = datasus_ftp_modulo.Datasus_ftp(PATH_DOWNLOAD)

    while(True):
        print(f"""\n----------------------------------------------
Explorador de Arquivos do Servidor FTP DataSUS
----------------------------------------------\n
DIRETORIO ATUAL: {conexaoftp.ftp.pwd()}\n""")

        for opcaoChave, opcaoValor in OPCOES.items():
            print(f'{opcaoChave} - {opcaoValor}')

        while(True):
            try:
                selecao = int(input("\nDigite o código da função desejada: "))
                if selecao in OPCOES.keys():
                    break
                else:
                    print("Código invalido, por favor digite novamente...")
            except:
                print("Código invalido, por favor digite novamente...")

        if(selecao==0):
            print("Encerrando programa...")
            break
        
        menu(conexaoftp, selecao)
        
    conexaoftp.encerrar_conexao_datasusftp()


if __name__ == '__main__':
    fazer_pasta_download()
    main()