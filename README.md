# Dir Structure
```
.
├── app
│   ├── api
│   │   ├── routers
│   │   └── schemas
│   ├── common
│   ├── core
│   │   ├── domain
│   │   └── services
│   ├── infrastructure
│   │   ├── cache
│   │   ├── db
│   │   └── repositories
├── migrations
│   └── versions
└── tests
    ├── integration
    └── unit
```

# Requirement
- redis
- mysql

# How To Run
> Install requirement
```
pip install -r requirements.txt
```

> migrate schema
```
alembic upgrade head
```

> run app
```
python -m app.main
```

### Api list
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

