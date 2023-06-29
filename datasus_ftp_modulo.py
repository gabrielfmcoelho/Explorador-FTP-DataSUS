import ftplib

CONEXAO_DATASUS = "ftp.datasus.gov.br"
DIRETORIOS = ['agvigsan', 'aih_apac_ident', 'atendimento', 'caderno', 'cartaosus', 'catalogo', 'cgsi Brasilia', 'CIH', 'CIHA', 'cnes', 'CODDS', 'degerts', 'diapt', 'dimss', 'dissemin', 'dmss', 'dumpesus', 'ftpbolsa', 'GALNacional', 'getr', 'hemovida', 'hemovida_web', 'HFSE-CGU', 'hiperdia', 'homologa-SISRCA', 'municip', 'NEMS', 'PainelExecutivo', 'PNI', 'publico', 'Siab', 'siasus', 'SIOPS', 'SIPNI', 'siscam', 'soa_cds', 'tabnet', 'tabwin', 'territorio', 'universus']

class Datasus_ftp:
    def __init__(self):
        try:
            self.ftp = ftplib.FTP(CONEXAO_DATASUS)
            self.ftp.login()
            self.ftp.getwelcome()
        except Exception as ex:
            print(f'Não foi possivel realizar a conexão com o FTP DataSUS, o seguinte erro ocorreu: {ex}')

    def encerrar_conexao_datasusftp(self):
        self.ftp.close()

    def listar_diretorio(self):
        self.ftp.dir()
        return
    
    def acessar_diretorio(self):
        diretorio = input("Digite o diretorio que deseja acessar: ")
        try:
            self.ftp.cwd(diretorio)
            self.ftp.dir()
        except Exception as ex:
            print(f"Não foi possivel acessar o diretorio, o seguinte erro ocorreu: {ex}")
    
    def voltar_diretorio(self):
        try:
            self.ftp.cwd("..")
        except Exception as ex:
            print(f"Não foi possivel voltar o diretorio, o seguinte erro ocorreu: {ex}")
        return
    
    def download_arquivo(self):
        filename = input("Digite o nome do arquivo que deseja realizar download: ")
        try:
            with open(filename, "wb") as file:
                self.ftp.retrbinary(f"RETR {filename}", file.write)
        except Exception as ex:
            print(f"Não foi possivel realizar o download do arquivo, o seguinte erro ocorreu: {ex}")

    def pesquisar_arquivo_data(self):
        data_bruta = input("Digite a data que deseja pesquisar no formato MM/YYYY: (exemplo 05/2018) ")
