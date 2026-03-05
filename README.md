# Ecommerce Backend

## Como rodar

### 1. Ative o ambiente virtual
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure o .env
Renomeie `.env.example` para `.env` e preencha:
```
DATABASE_URL=postgresql://postgres:sua_senha@localhost:5432/VaralTech
JWT_SECRET_KEY=qualquer-string-aqui
```

### 3. Crie o banco no PostgreSQL (pgAdmin ou psql)
```sql
CREATE DATABASE VaralTech;
```

### 4. Rode
```
python app.py
```
> A tabela `users` é criada automaticamente na primeira execução.

---

## Endpoints

| Método | Rota       | Descrição                        |
|--------|------------|----------------------------------|
| POST   | /register  | Cadastrar usuário                |
| POST   | /login     | Login — retorna JWT              |
| GET    | /me        | Dados do usuário (requer token)  |

### POST /register
```json
{ "name": "João", "email": "joao@email.com", "password": "123456" }
```

### POST /login
```json
{ "email": "joao@email.com", "password": "123456" }
```

### GET /me
```
Header: Authorization: Bearer <token>
```
