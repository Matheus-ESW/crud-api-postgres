# Como rodar o projeto na sua máquina
## Usando Docker Compose

Essa é a forma mais rápida e simples.  
Não é necessário instalar nada além do Docker.

### Clone o repositório
```bash
git clone https://github.com/Matheus-ESW/crud-api-postgres
cd crud-api-postgres
```

### Suba todos os serviços
```bash
docker-compose up --build
```

Isso irá subir:

Backend (FastAPI)
Banco PostgreSQL

Frontend (Streamlit)

Acesse as aplicações
Frontend (Interface do usuário): http://localhost:8501

Backend (Documentação Swagger): http://localhost:8000/docs

Parar a aplicação
```bash
docker-compose down
```

```scss
Arquitetura Geral

Usuário → Frontend (Streamlit)
              ↓
        API Backend (FastAPI)
              ↓
        Banco PostgreSQL
```
O backend expõe rotas CRUD e o frontend consome essa API para criar, listar, atualizar e excluir produtos.

Funcionalidades Implementadas

✔ Criar produto
✔ Listar produto(s)
✔ Atualizar produto
✔ Excluir produto

Matheus Ramos - Parte de estudos do bootcamp de Python da Jornada de Dados
