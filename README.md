cat > README.md << 'EOF'
# Cybersecurity Studies

Pequenas ferramentas de rede em Python, feitas com a biblioteca padrão (`socket`), para estudar TCP e HTTP.

## scanner.py

Scanner de portas TCP com várias threads.

```
python3 scanner.py 127.0.0.1 -s 1 -e 1024
```

Opções:

- `-s`, `--start`: primeira porta (padrão 1)
- `-e`, `--end`: última porta (padrão 1024)
- `-w`, `--workers`: número de threads (padrão 100)

## client.py

Cliente HTTP simples feito direto sobre socket. Envia um `GET /` para `127.0.0.1:8000` e mostra o status, os headers e o corpo da resposta.

Para testar, suba um servidor local em um terminal:

```
python3 -m http.server 8000
```

E rode o cliente em outro:

```
python3 client.py
```

## Aviso

Use o scanner apenas em máquinas suas ou com autorização explícita. Escanear redes de terceiros sem permissão pode ser considerado crime.
EOF