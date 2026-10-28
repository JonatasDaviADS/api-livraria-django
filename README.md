# API Livraria - Django REST + MariaDB (XAMPP)

API REST de uma livraria feita com com **DJANGO** e **DJANGO REST FRAMEWORK**, com o banco **MariaDB** (XAMPP) e um front-end em HTML/JavaScript estilo vitrie que consome a API.

Exercício da disciplina **Desenvolvimento de Serviços e APIs** - CST Análise e Desenvolvimento de Sistemas (Unisenac). 

---

## 🧰 Tecnologias

| Ferramenta | Papel |
|---|---|
| `Python` + `venv` | linguagem e ambiente isolado |
| `Django` | framework web (estrutura do projeto) |
| `djangorestframework` | transforma o Django em API REST |
| `mysqlclient` | conecta o Python ao MySQL/MariaDB |
| `django-cors-headers` | libera o front-end para acessar a API |
| `XAMPP` | MariaDB (banco) + Apache (serve o front) |

---

## 📁 Estrutura

```
Projeto_Livraria
├── frontend/
│   └── index.html          # vitrine que consome a API (fetch)
├── livraria/
│   ├── manage.py           # "controle remoto" do Django
│   ├── core/               # app dos livros
│   │   ├── models.py       # tabela Livro (ORM)
│   │   ├── serializers.py  # tradutor Livro <-> JSON
│   │   ├── views.py        # CRUD + filtros
│   │   ├── urls.py         # rotas do app (router)
│   │   └── migrations/     # "receitas" de criação das tabelas
│   └── livraria/           # configurações do projeto
│       ├── __init__.py     # ajuste para MariaDB 10.4
│       ├── settings.py     # apps, banco, CORS
│       └── urls.py         # rotas principais (/admin, /api)
├── requirements.txt
└── .gitignore
```

---

## 🚀 Como rodar

1. No XAMPP, ligue `Apache` e `MySQL`.
2. No phpMyAdmin, crie o banco:
```sql
   CREATE DATABASE livraria CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
3. No terminal, na raiz do projeto:
```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   cd livraria
   python manage.py migrate
   python manage.py runserver
```
4. API: `http://127.0.0.1:8000/api/livros/`
5. Front-end: `http://localhost/Projeto_Livraria/frontend/`

---

## 🔗 Endpoints

| Método | Rota | Ação |
|---|---|---|
| `GET` | `/api/livros/` | lista todos |
| `POST` | `/api/livros/` | cadastra |
| `GET` | `/api/livros/{id}/` | busca por ID |
| `PUT` | `/api/livros/{id}/` | atualiza (todos os campos) |
| `PATCH` | `/api/livros/{id}/` | atualiza parcialmente |
| `DELETE` | `/api/livros/{id}/` | exclui |
| `GET` | `/api/livros/autor/{nome}/` | filtra por autor |
| `GET` | `/api/livros/ano/{ano}/` | filtra por ano |
| `GET` | `/api/livros/genero/{genero}/` | filtra por gênero |
| `GET` | `/api/livros/titulo/{titulo}/` | filtra por título |

> ⚠️ Sempre termine a URL com `/`. Sem a barra, `PUT` e `DELETE` dão erro.

### Exemplo de JSON (POST/PUT)

```json
{
    "titulo": "Livro Teste",
    "autor": "Jonatas",
    "ano": 2026,
    "genero": "Tecnologia",
    "valor": "19.90",
    "url_imagem": null
}
```

---

## 🧠 Conceitos aprendidos

| Conceito | Resumo |
|---|---|
| **ORM** | a tabela é descrita em Python (`models.py`) e o Django gera o SQL |
| **Migração** | `makemigrations` escreve a receita; `migrate` executa no banco |
| **Serializer** | converte objeto Python ⇄ JSON e valida os dados |
| **ModelViewSet** | entrega o CRUD completo pronto (GET, POST, PUT, PATCH, DELETE) |
| **@action** | cria endpoints extras no ViewSet (os filtros) |
| **`__icontains`** | filtro "contém", sem diferenciar maiúsculas |
| **Router** | gera as URLs do CRUD automaticamente |
| **CORS** | permite que uma página de outra origem (porta 80) acesse a API (porta 8000) |
| **Tabela `core_livro`** | nome = `app` + `_` + `model` |

### Códigos HTTP

| Código | Significado |
|---|---|
| `200 OK` | sucesso (GET, PUT) |
| `201 Created` | registro criado (POST) |
| `204 No Content` | registro apagado (DELETE) |
| `302 Found` | redirecionamento |
| `404 Not Found` | rota ou registro inexistente |
| `500 Internal Server Error` | erro no servidor |

---

## 🛠️ Comandos usados

### Ambiente

| Comando | O que faz |
|---|---|
| `python -m venv venv` | cria o ambiente virtual |
| `.\venv\Scripts\activate` | ativa o ambiente |
| `pip install ...` | instala bibliotecas |
| `pip freeze > requirements.txt` | salva a lista de bibliotecas |

### Django

| Comando | O que faz |
|---|---|
| `django-admin startproject livraria` | cria o projeto |
| `python manage.py startapp core` | cria o app |
| `python manage.py makemigrations` | gera a migração |
| `python manage.py migrate` | cria as tabelas no banco |
| `python manage.py runserver` | liga o servidor (porta 8000) |

### Git

| Comando | O que faz |
|---|---|
| `git init` | cria o repositório local |
| `git add .` | prepara as alterações |
| `git commit -m "msg"` | salva uma versão |
| `git branch -M main` | nomeia o ramo principal |
| `git remote add origin URL` | liga ao GitHub |
| `git push -u origin main` | primeiro envio (memoriza o destino) |
| `git push` | envios seguintes |

---

## ⚠️ Problemas resolvidos

| Problema | Solução |
|---|---|
| Django 6 recusa MariaDB 10.4 | regras no `livraria/__init__.py` desligando a checagem de versão e o retorno no INSERT |
| `404` em `http://127.0.0.1:8000/` | a raiz não tinha rota; usar `/api/livros/` (ou `RedirectView`) |
| `fatal: not a git repository` | `cd ..` a mais; comandos Git rodam em `Projeto_Livraria` |
| `cannot lock ref 'HEAD'... reference broken` | apagar `.git\refs\heads\main` e rodar `git update-ref refs/heads/main origin/main` |
| Capa quebrada no front | `url_imagem` vazia → capa provisória com `placehold.co` |