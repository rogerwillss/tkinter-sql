# 💼 Tkinter + SQL - Sistema de Cadastro com Interface Gráfica

Sistema desktop desenvolvido em Python utilizando **Tkinter** para a interface gráfica e **SQL** para persistência de dados. A aplicação oferece uma solução completa de cadastro e gerenciamento de **clientes**, **usuários**, **produtos**, **funcionários** e **vendas**.

---

## 📌 Funcionalidades

- ✅ Tela de login (com splash screen)
- ✅ Cadastro e consulta de clientes
- ✅ Cadastro de produtos e funcionários
- ✅ Gerenciamento de vendas
- ✅ Inserção de registros via formulários
- ✅ Listagem de usuários cadastrados
- ✅ Interface gráfica amigável com Tkinter

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Tkinter** – Interface gráfica
- **SQL** – Armazenamento de dados (via biblioteca de conexão, ex: `sqlite3` ou `pyodbc`)
- **PIL (opcional)** – Para exibição de imagens, como a logo

---

## 📁 Estrutura do Projeto

```

tkinter-sql/
│
├── cad\_cliente.py           # Tela de cadastro de clientes
├── cad\_usuario.py           # Tela de cadastro de usuários
├── cad\_funcionario.py       # Tela de cadastro de funcionários
├── cad\_produto.py           # Tela de cadastro de produtos
├── cad\_venda.py             # Tela de cadastro de vendas
│
├── inserir\_cliente.py       # Script de inserção no banco
├── inserir\_usuario.py
├── inserir\_funcionario.py
├── inserir\_produto.py
├── inserir\_venda.py
│
├── tela\_listar\_usuarios.py  # Listagem de usuários cadastrados
├── tela\_splash.py           # Tela de splash inicial
├── principal.py             # Arquivo principal da aplicação
├── conexao.py               # Configuração de conexão com o banco
├── querygeral.sql           # Scripts SQL auxiliares
├── logo.jpg                 # Imagem/logo da aplicação

````

---

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/rogerwillss/tkinter-sql.git
cd tkinter-sql
````

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

### 3. Instale dependências

```bash
pip install tk
```

> ⚠️ Se o projeto usar `pyodbc`, `sqlite3` ou `Pillow`, instale também:

```bash
pip install pyodbc pillow
```

### 4. Configure o banco de dados

Edite o arquivo `conexao.py` e configure sua string de conexão para o banco SQL desejado.

### 5. Execute o projeto

```bash
python principal.py
```

---

## 🧪 Pré-Requisitos

* Python 3.8 ou superior
* Driver de conexão com banco de dados instalado (ex: ODBC, SQLite)
* Sistema operacional: Windows, Linux ou macOS

---

## 📸 Tela da Aplicação (opcional)

> Se desejar, você pode adicionar prints das telas principais aqui.

---

## 📄 Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙋‍♂️ Autor

Desenvolvido por **Roger William**
🔗 [GitHub](https://github.com/rogerwillss)

---

## ✨ Contribuições

Contribuições, issues e sugestões são bem-vindas!
Sinta-se livre para abrir uma issue ou pull request. 🚀

```

---
