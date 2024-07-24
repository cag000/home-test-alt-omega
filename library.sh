#!/bin/bash

# Define the base directory
base_dir="library_management"

# Define the directory structure
dirs=(
  "app"
  "app/core"
  "app/core/domain"
  "app/core/services"
  "app/infrastructure"
  "app/infrastructure/cache"
  "app/infrastructure/db"
  "app/infrastructure/repositories"
  "app/api"
  "app/api/routers"
  "app/api/schemas"
  "app/common"
  "migrations"
  "migrations/versions"
  "tests"
  "tests/unit"
  "tests/integration"
)

# Define the files to be created
files=(
  "app/__init__.py"
  "app/main.py"
  "app/core/__init__.py"
  "app/core/domain/__init__.py"
  "app/core/domain/models.py"
  "app/core/domain/repositories.py"
  "app/core/services/__init__.py"
  "app/core/services/author_service.py"
  "app/core/services/book_service.py"
  "app/core/services/service_interface.py"
  "app/infrastructure/__init__.py"
  "app/infrastructure/cache/__init__.py"
  "app/infrastructure/cache/redis_cache.py"
  "app/infrastructure/cache/memcache_cache.py"
  "app/infrastructure/db/__init__.py"
  "app/infrastructure/db/database.py"
  "app/infrastructure/db/models.py"
  "app/infrastructure/repositories/__init__.py"
  "app/infrastructure/repositories/base_repository.py"
  "app/infrastructure/repositories/sqlalchemy_repository.py"
  "app/infrastructure/repositories/author_repository.py"
  "app/infrastructure/repositories/book_repository.py"
  "app/infrastructure/repositories/repository_interface.py"
  "app/api/__init__.py"
  "app/api/dependencies.py"
  "app/api/routers/__init__.py"
  "app/api/routers/author_http.py"
  "app/api/routers/author_rpc.py"
  "app/api/routers/book_http.py"
  "app/api/routers/book_rpc.py"
  "app/api/schemas/__init__.py"
  "app/api/schemas/author_schema.py"
  "app/api/schemas/book_schema.py"
  "app/common/__init__.py"
  "app/common/custom_errors.py"
  "app/common/error_handler.py"
  "migrations/versions/20210701_01_create_authors_table_up.sql"
  "migrations/versions/20210701_01_create_authors_table_down.sql"
  "migrations/versions/20210701_02_create_books_table_up.sql"
  "migrations/versions/20210701_02_create_books_table_down.sql"
  "migrations/env.py"
  "tests/__init__.py"
  "tests/unit/__init__.py"
  "tests/unit/test_author_service.py"
  "tests/integration/__init__.py"
  "tests/integration/test_author_repository.py"
  "README.md"
)

# Create the directories
for dir in "${dirs[@]}"; do
  mkdir -p "$base_dir/$dir"
done

# Create the files
for file in "${files[@]}"; do
  touch "$base_dir/$file"
done

echo "Directory structure created successfully!"

