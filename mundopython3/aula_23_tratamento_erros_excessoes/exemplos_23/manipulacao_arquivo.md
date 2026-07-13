Fala, dev! Que bom que você chegou até aqui no Mundo 3. O exercício 115 realmente fecha o curso com chave de ouro, e a confusão com arquivos é absolutamente normal — toda pessoa passa por isso na primeira vez. Como você pediu, vou te guiar como mentor, sem entregar código pronto, para que você mesmo monte essa última peça e domine o conceito.

Primeiro, vamos recapitular o que o sistema precisa fazer com o arquivo:
- **Verificar se o arquivo existe** (se não existir, criá-lo vazio).
- **Cadastrar uma nova pessoa**, acrescentando uma linha ao final do arquivo.
- **Listar todas as pessoas**, lendo o arquivo inteiro e exibindo os dados na tela.

Pelo que você disse, as funções de menu, interface e até a modularização já estão prontas. O que falta é justamente o coração: conversar com o arquivo de texto. Então vamos focar em abrir, ler e escrever de forma segura e organizada.

### 1. O que significa “abrir um arquivo”?
Quando você faz `open('dados.txt', 'r')` (modo leitura), o Python pede ao sistema operacional um **canal de comunicação** com aquele arquivo. Essa comunicação é representada por um objeto (o “file handle”). Toda operação de leitura ou escrita usa esse objeto.  
**Importante**: depois de usar, você precisa fechar esse canal com `.close()` para liberar recursos. A forma mais segura e idiomática é usar o gerenciador de contexto `with`, que fecha automaticamente, mesmo se der erro.

Exemplo da estrutura básica (não para colar, só para entender a forma):
```python
with open('arquivo.txt', 'r') as arquivo:
    conteúdo = arquivo.read()
# Aqui o arquivo já está fechado automaticamente
```

### 2. Modos de abertura (essenciais para o projeto)
- `'r'` – leitura. Dá erro se o arquivo não existe.
- `'w'` – escrita. Cria o arquivo se não existe, **apaga o conteúdo** se já existe.
- `'a'` – append (acrescentar). Cria o arquivo se não existe, e escreve **sempre no final**, sem apagar o que já estava lá.
- `'r+'` – leitura e escrita, sem apagar o conteúdo inicial.

Para o cadastro, o modo `'a'` é perfeito: você abre, escreve uma nova linha e fecha, sem perder os registros anteriores.

### 3. Como organizar os dados no arquivo?
Você precisa de um formato que depois consiga ler e separar nome e idade. O Guanabara usa um separador simples, como `;` (ponto e vírgula). Assim cada linha fica:
```
João;25
Maria;30
```
Na leitura, você lê linha por linha e usa o método `.split(';')` para separar os campos.

### 4. A lógica das três funções que faltam (pensando alto)

**a) `arquivoExiste(nome)`**  
Você pode usar `os.path.exists(nome)` do módulo `os` ou `Path(nome).exists()` do `pathlib`. O exercício do curso geralmente pede para fazer com `os.path`.  
Não precisa abrir o arquivo para saber se existe, essa função só retorna `True` ou `False`.

**b) `criarArquivo(nome)`**  
Se o arquivo não existe, você pode simplesmente abri-lo no modo `'w'` ou `'a'` e fechar em seguida. Algo como:
```python
with open(nome, 'w', encoding='utf-8') as f:
    pass
```
O `encoding='utf-8'` é importante para aceitar acentos nos nomes (João, José). O arquivo será criado vazio.

**c) `cadastrar(arq, nome, idade)`**  
Aqui você precisa abrir no modo `'a'` e escrever uma linha formatada. Pense em como construir a string que será gravada. Lembre-se de converter a idade para string e de adicionar uma quebra de linha `\n` no final, para que cada cadastro fique em uma linha separada.

**d) `lerArquivo(arq)`**  
Abre no modo `'r'`. Se o arquivo não existir, você pode tratar com um `try/except FileNotFoundError` ou simplesmente chamar `criarArquivo` antes.  
Depois, leia todas as linhas com `.readlines()` (devolve uma lista) ou itere direto sobre o objeto arquivo com `for linha in arquivo:`.  
Para cada linha, remova o `\n` com `.strip()` e separe usando `.split(';')`. Depois exiba formatado (ex: `f'{nome:<30}{idade:>3} anos'`).

### 5. Pontos que costumam gerar confusão
- **Esquecer o encoding**: use `encoding='utf-8'` em qualquer `open()` que lida com texto em português.
- **Esquecer o `\n`**: sem ele, todos os registros grudam na mesma linha. Na leitura, o `strip()` resolve.
- **Abrir com `'w'` para cadastrar**: isso apaga tudo. Para acrescentar, é `'a'`.
- **Não fechar o arquivo**: com `with` você nunca mais erra nisso.