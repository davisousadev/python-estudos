import csv
from pathlib import Path 

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'dados.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Nome', 'Idade', 'Cidade'])
        writer.writerow(['Alice', 30, 'São Paulo'])
        writer.writerow(['Bob', 25, 'Rio de Janeiro'])
        writer.writerow(['Charlie', 35, 'Belo Horizonte'])
except IOError as exc:
    print(f'Erro ao manipular o arquivo: {exc}')

try:
    with open(ROOT_PATH / 'dados.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except IOError as exc:
    print(f'Erro ao manipular o arquivo: {exc}')