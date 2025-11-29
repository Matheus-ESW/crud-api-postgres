Como rodar o projeto na sua máquina

Existem duas maneiras de rodar o projeto:

Opção 1 — Usando Docker Compose (recomendado)

Essa é a forma mais rápida e simples.
Não é necessário instalar nada além do Docker.

1️⃣ Clone o repositório
git clone https://github.com/<seu-usuario>/<seu-repo>.git
cd <seu-repo>

2️⃣ Suba todos os serviços
docker-compose up --build

Isso irá subir:

Backend (FastAPI)

Banco PostgreSQL

Frontend (Streamlit)

3️⃣ Acesse as aplicações

🔹 Frontend (Interface do usuário)
👉 http://localhost:8501

🔹 Backend (Documentação Swagger)
👉 http://localhost:8000/docs

4️⃣ Parar a aplicação
docker-compose down

✔️ Opção 2 — Rodar sem Docker (modo desenvolvedor)

Recomendado apenas para quem quer estudar o código separadamente.

1️⃣ Crie o ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

2️⃣ Instale as dependências
Instalar dependências gerais:
pip install -r requirements.txt

Instalar dependências do backend:
cd backend
pip install -r requirements.txt

Instalar dependências do frontend:
cd frontend
pip install -r requirements.txt

▶️ Rodando o Backend manualmente
cd backend
uvicorn main:app --reload


A API ficará disponível em:
👉 http://localhost:8000

👉 http://localhost:8000/docs
 (Swagger UI)

▶️ Rodando o Frontend manualmente
cd frontend
streamlit run app.py


Acesse em:
👉 http://localhost:8501

🗄️ Banco de Dados

O projeto utiliza PostgreSQL.
No Docker, o banco sobe automaticamente.

Sem Docker, você precisará criar um banco manualmente:

Nome recomendado:

crud_database

Credenciais devem ser ajustadas em:

backend/conn/connDatabase.py

🏗️ Arquitetura Geral
Usuário → Frontend (Streamlit)
              ↓
        API Backend (FastAPI)
              ↓
        Banco PostgreSQL


O backend expõe rotas CRUD e o frontend consome essa API para criar, listar, atualizar e excluir produtos.

📌 Funcionalidades Implementadas

✔ Criar produto
✔ Listar produto(s)
✔ Atualizar produto
✔ Excluir produto
✔ Interface gráfica em Streamlit
✔ API documentada com Swagger
✔ Banco Postgres persistente via Docker
✔ Arquitetura MVC no backend
✔ Comunicação entre containers via Docker Compose

📬 Autor

Matheus Ramos
Engenharia de Dados • Python • APIs • Cloud
🔗 LinkedIn: https://www.linkedin.com/in/matheussoaresramos/