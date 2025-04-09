# 📊 E-Shop Brasil - Integração de MongoDB com Streamlit

Este projeto tem como objetivo demonstrar uma aplicação CRUD utilizando **MongoDB** como banco de dados NoSQL, **Streamlit** para interface visual e **Docker** para ambiente containerizado.  
A proposta simula a modernização da infraestrutura digital de uma empresa de comércio eletrônico fictícia chamada **E-Shop Brasil**.

## 📦 Tecnologias Utilizadas

- **MongoDB**: Banco de dados NoSQL para armazenamento de dados  
- **Streamlit**: Framework para construção rápida de interfaces web em Python  
- **Docker** e **Docker Compose**: Criação de ambiente isolado e portável  
- **Faker**: Geração de dados fictícios  
- **Python**: Linguagem de programação principal  

## 📁 Estrutura do Projeto

```
e-shop-brasil/
├── app/                 # Código do app Streamlit
│   ├── main.py
│   ├── crud.py
│   ├── db.py
│   └── utils.py
├── data/                # Script para inserção de dados
│   └── seed_data.py
├── Dockerfile           # Dockerfile da aplicação
├── docker-compose.yml   # Orquestração de containers
├── requirements.txt     # Dependências
└── README.md            # Documentação
```

## 🚀 Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/pedro-h7/e-shop-brasil-portfolio.git
cd e-shop-brasil-portfolio
```

### 2. Suba os containers com Docker Compose

```bash
docker-compose up --build
```

### 3. Acesse o aplicativo

Abra seu navegador e vá para:  
[http://localhost:8502](http://localhost:8502)

### 4. Inserir dados massivos (opcional)

Em um terminal novo (fora do container), execute:

```bash
python data/seed_data.py
```

## ✍️ Funcionalidades

- Cadastro de novos clientes (nome, email, telefone)  
- Listagem dos clientes cadastrados  
- Atualização de nome  
- Exclusão de registros  

## 📌 Observações

- O banco **MongoDB** está acessível localmente via porta `27018`  
- A interface **Streamlit** roda em `http://localhost:8502`  
- O script `seed_data.py` usa a biblioteca `Faker` para gerar 1 milhão de registros fictícios

> Projeto acadêmico - Curso de Gestão de Tecnologia da Informação 💻🎓
