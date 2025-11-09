# blibioteca para caminho de arquivos
from pathlib import Path

# pegando o caminho raiz do arquivo atual que esta no diretorio manipulando_arquivo
ROOT_PATH = Path(__file__).parent

# tratamento de erro ao manipular arquivo
try:
    #abrindo arquivo para escrita e ja fechando ele com o with
    with open(ROOT_PATH / 'arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Linha 1\n')
except FileNotFoundError as e:
    print(f'Arquivo não encontrado: {e}')
except IOError as e:
    print(f'Erro ao manipular o arquivo: {e}')