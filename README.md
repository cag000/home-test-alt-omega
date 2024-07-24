library_management/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── domain/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   └── repositories.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── author_service.py
│   │   │   ├── book_service.py
│   │   │   └── service_interface.py
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── cache/
│   │   │   ├── __init__.py
│   │   │   ├── redis_cache.py
│   │   │   └── memcache_cache.py
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   ├── database.py
│   │   │   └── models.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── base_repository.py
│   │   │   ├── sqlalchemy_repository.py
│   │   │   ├── author_repository.py
│   │   │   ├── book_repository.py
│   │   │   └── repository_interface.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── author_http.py
│   │   │   ├── author_rpc.py
│   │   │   ├── book_http.py
│   │   │   └── book_rpc.py
│   │   └── schemas/
│   │       ├── __init__.py
│   │       ├── author_schema.py
│   │       └── book_schema.py
│   ├── common/
│   │   ├── __init__.py
│   │   ├── custom_errors.py
│   │   └── error_handler.py
├── migrations/
│   ├── versions/
│   │   ├── 20210701_01_create_authors_table_up.sql
│   │   ├── 20210701_01_create_authors_table_down.sql
│   │   ├── 20210701_02_create_books_table_up.sql
│   │   ├── 20210701_02_create_books_table_down.sql
│   └── env.py
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   └── test_author_service.py
│   └── integration/
│       ├── __init__.py
│       └── test_author_repository.py
├── alembic.ini
├── .env
├── .gitignore
├── requirements.txt
└── README.md
