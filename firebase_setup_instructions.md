# Instruções de Configuração do Ambiente Firebase

Este documento detalha os passos necessários para configurar o ambiente Firebase para a aplicação de Gerenciamento de Peso em Python.

## 1. Criar um Projeto Firebase

1.  Aceda à [Consola do Firebase](https://console.firebase.google.com/).
2.  Clique em "Adicionar projeto" ou selecione um projeto existente.
3.  Siga os passos para criar um novo projeto. Se estiver a criar um novo projeto, pode desativar o Google Analytics para este projeto, se desejar.

## 2. Ativar o Cloud Firestore

1.  No menu lateral da Consola do Firebase, navegue até "Firestore Database" (Base de Dados Firestore).
2.  Clique em "Criar base de dados".
3.  Selecione "Iniciar em modo de produção" ou "Iniciar em modo de teste", dependendo das suas necessidades (para desenvolvimento, o modo de teste é aceitável, mas lembre-se das implicações de segurança).
4.  Escolha a localização do seu Cloud Firestore (por exemplo, `nam5 (us-central)`).
5.  Clique em "Ativar".

## 3. Gerar uma Chave de Conta de Serviço

Para que a sua aplicação Python possa autenticar-se e interagir com o Firebase, necessitará de uma chave de conta de serviço.

1.  Na Consola do Firebase, navegue até "Definições do projeto" (o ícone de engrenagem ao lado de "Visão geral do projeto").
2.  Selecione a aba "Contas de serviço".
3.  Clique em "Gerar nova chave privada" e, em seguida, em "Gerar chave".
4.  Um ficheiro JSON será descarregado para o seu computador. **Mantenha este ficheiro seguro e não o partilhe publicamente.** Este ficheiro contém as credenciais para aceder ao seu projeto Firebase.
5.  Renomeie o ficheiro descarregado para `firebase_credentials.json` (ou qualquer nome que preferir).

## 4. Configurar o Ambiente Python

1.  **Instalar a biblioteca `firebase-admin`:**
    Se ainda não o fez, instale a biblioteca `firebase-admin` no seu ambiente Python:
    ```bash
    pip install firebase-admin
    ```

2.  **Definir a variável de ambiente:**
    A sua aplicação Python espera o caminho para o ficheiro de chave da conta de serviço através da variável de ambiente `FIREBASE_SERVICE_ACCOUNT_KEY_PATH`.

    -   **No Linux/macOS:**
        Abra o seu terminal e execute:
        ```bash
        export FIREBASE_SERVICE_ACCOUNT_KEY_PATH="C:/Users/NAQUI/LeveAVidaLeve/firebase_credentials.json"
        ```
        Substitua `/caminho/para/o/seu/firebase_credentials.json` pelo caminho real onde guardou o ficheiro JSON. Para que esta variável persista entre sessões do terminal, adicione-a ao seu ficheiro `~/.bashrc`, `~/.zshrc` ou equivalente.

    -   **No Windows (Prompt de Comando):**
        ```cmd
        set FIREBASE_SERVICE_ACCOUNT_KEY_PATH="C:/Users/NAQUI/LeveAVidaLeve/firebase_credentials.json"
        ```
        Para persistência, use:
        ```cmd
        setx FIREBASE_SERVICE_ACCOUNT_KEY_PATH "C:/Users/NAQUI/Jason/firebase_credentials.json"
        ```

    -   **No Windows (PowerShell):**
        ```powershell
        $env:FIREBASE_SERVICE_ACCOUNT_KEY_PATH="C:\Users\NAQUI\LeveAVidaLeve\firebase-credentials.json"
        ```
        Para persistência, pode adicioná-lo ao seu perfil do PowerShell.

    **Importante:** Se a variável de ambiente não for definida, o projeto criará um ficheiro `firebase_credentials.json` falso para demonstração, mas este não permitirá a conexão real ao Firebase. **Deve substituir este ficheiro falso pelas suas credenciais reais para que a aplicação funcione corretamente.**

## 5. Executar a Aplicação

Após configurar a variável de ambiente e instalar as dependências, pode executar o ficheiro `main.py`:

```bash
python main.py
```

A aplicação tentará conectar-se ao Firebase, criar/recuperar dados e demonstrar as funcionalidades. Verifique a saída no terminal para quaisquer erros de conexão ou operações.

