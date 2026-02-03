import random
import string
import getpass
import platform
import os
from datetime import datetime


usuario = getpass.getuser()
sistema = platform.system()
versao = platform.version()
arquitetura = platform.architecture()[0]
processador = platform.processor()
os.system('')
os.system('chcp 65001') 
print('''\033[32m
  ________                         .___                   .___           _________             .__                   
 /  _____/  ________________     __| _/___________      __| _/____      /   _____/ ____   ____ |  |__ _____    ______
/   \  ____/ __ \_  __ \__  \   / __ |/  _ \_  __ \    / __ |/ __ \     \_____  \_/ __ \ /    \|  |  \__  \  /  ___/
\    \_\  \  ___/|  | \// __ \_/ /_/ (  <_> )  | \/   / /_/ \  ___/     /        \  ___/|   |  \   Y  \/ __ \_\___ \ 
 \______  /\___  >__|  (____  /\____ |\____/|__|      \____ |\___  >   /_______  /\___  >___|  /___|  (____  /____  >
        \/     \/           \/      \/                     \/    \/            \/     \/     \/     \/     \/     \/ \033[m''')
print(f'Usuário logado: {usuario}')
print(f'Sistema: {sistema}\nVersão: {versao}\nArquitetura: {arquitetura}\nProcessador: {processador}')
print('-=-' * 21)

while True:
    while True:
        comprimento = (input('Digite o comprimento desejado para a senha: '))
        try:
            comprimento = int(comprimento)
            if comprimento < 8:
                print('Comprimento Inválido! Insira um comprimento de até 8 ou mais caracteres.')
                reiniciar = input('>>> Tentar novamente? (s/n): ').strip().lower()
                if reiniciar != 's':
                    print('Até logo!. Lembre-se de buscar sempre a sua segurança na internet!')
                    input('Aperte Enter para fechar...')
                    break
                else:
                    continue
        except ValueError:
            print('Comprimento Inválido. Por favor insira um valor válido (número)')
            continue
        
        letrasMAI = str(input('Incluir letras maiúsculas? (s/n): ')).strip().lower()
        letrasMIN = str(input('Incluir letras minúsculas? (s/n): ')).strip().lower()
        numeros = str(input('Incluir números? (s/n): ')).strip().lower()
        caracteresESPE = str(input('Incluir caracteres especiais? (s/n): ')).strip().lower()
        caracteres = ''
        
        if letrasMAI == 's':
            caracteres += string.ascii_uppercase
        if letrasMIN == 's':
            caracteres += string.ascii_lowercase
        if numeros == 's':
            caracteres += string.digits
        if caracteresESPE == 's':
            caracteres += string.punctuation
        if not caracteres:
            print('Você deve escolher ao menos um tipo de caractere! Tente novamente.')
        else:
            # Gera a senha aleatória escolhendo caracteres aleatórios da string 'caracteres' até atingir o comprimento desejado.
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            salvar = str(input('Você deseja salvar sua senha? (s/n): ')).strip().lower()
            if salvar == 's':
                print('Senha gerada com sucesso.')
                
                # Importação da biblioteca para abrir o selecionador de arquivo
                from tkinter import Tk
                from tkinter.filedialog import asksaveasfilename
                Tk().withdraw()
                caminho_arquivo = asksaveasfilename(
                title='Salvar senha como...',
                defaultextension = '.txt',
                filetypes = [("Arquivo de texto", "*.txt")]
            )
                if caminho_arquivo:
                    with open(caminho_arquivo, 'w') as file:
                        file.write(f'Senha solicitada de: {usuario}\n')
                        file.write(f'Sistema: {sistema +  versao}\n')
                        file.write(f'Gerada em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n')
                        file.write(f'Senha gerada: {senha}')
                    print('Senha salva com sucesso.')
                else:
                    print('Você cancelou a operação de salvar.')
            else:
                versenha = str(input('Então você deseja ver a senha? (s/n): ')).strip().lower()
                if versenha == 's':
                    print(f'Senha gerada: {senha}')
               
        print('Até mais! Sempre coloque senhas seguras na sua conta!')
        input('Aperte enter para fechar...')
        break
    break
