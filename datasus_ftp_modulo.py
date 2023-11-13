import ftplib
import regex as re

CONEXAO_DATASUS = "ftp.datasus.gov.br"

class Datasus_ftp:
    arquivos_do_diretorio_atual = []
    
    def __init__(self, path_download):
        try:
            self.ftp = ftplib.FTP(CONEXAO_DATASUS)
            self.path_download = path_download
            self.ftp.login()
            self.ftp.getwelcome()
            self.armazenar_arquivos_do_diretorio_atual()
        except Exception as ex:
            print(f'Não foi possivel realizar a conexão com o FTP DataSUS, o seguinte erro ocorreu: {ex}')

    def encerrar_conexao_datasusftp(self):
        self.ftp.close()
        
    def armazenar_arquivos_do_diretorio_atual(self):
        self.arquivos_do_diretorio_atual = self.ftp.nlst()

    def listar_diretorio(self):
        for arquivo in self.arquivos_do_diretorio_atual:
            print(arquivo)
        return
    
    def acessar_diretorio(self):
        diretorio = input("Digite o diretorio que deseja acessar: ")
        ultimo_diretorio = self.ftp.pwd()
        try:
            self.ftp.cwd(diretorio)
            self.ftp.dir()
            self.armazenar_arquivos_do_diretorio_atual()
        except Exception as ex:
            print(f"Não foi possivel acessar o diretorio, o seguinte erro ocorreu: {ex}")
            print("Voltando para o diretorio anterior...")
            self.ftp.cwd(ultimo_diretorio)
    
    def voltar_diretorio(self):
        try:
            self.ftp.cwd("..")
            self.armazenar_arquivos_do_diretorio_atual()
        except Exception as ex:
            print(f"Não foi possivel voltar o diretorio, o seguinte erro ocorreu: {ex}")
    
    def download_arquivo(self):
        filename = input("Digite o nome do arquivo que deseja realizar download: ")
        try:
            with open(self.path_download + filename, 'wb') as file:
                self.ftp.retrbinary('RETR ' + filename, file.write)
            print(f"Download do arquivo {filename} realizado com sucesso!")
        except Exception as ex:
            print(f"Não foi possivel realizar o download do arquivo, o seguinte erro ocorreu: {ex}")

    def pesquisar_arquivo_data(self):
        try:
            data_bruta = input("Digite a data que deseja pesquisar no formato MM/YYYY: (exemplo 05/2018) ")
            data_formatada = data_bruta.replace("/", "")
            data_formatada = data_formatada[2:] + data_formatada[:2]
            for arquivo in self.arquivos_do_diretorio_atual:
                if re.search(data_formatada, arquivo):
                    print(arquivo)
        except Exception as ex:
            print(f"Não foi possivel pesquisar o arquivo, o seguinte erro ocorreu: {ex}")
        
    def filtrar_por_inicio_do_arquivo(self):
        try:
            inicio_do_arquivo = input("Digite o inicio do arquivo que deseja pesquisar: ")
            for arquivo in self.arquivos_do_diretorio_atual:
                if arquivo.startswith(inicio_do_arquivo):
                    print(arquivo)
        except Exception as ex:
            print(f"Não foi possivel filtrar o arquivo, o seguinte erro ocorreu: {ex}")