"""Create authors and books table

Revision ID: d84d6502896e
Revises: 
Create Date: 2024-07-24 02:03:00.043147

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d84d6502896e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        sa.DDL(
            """
        CREATE TABLE authors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            bio TEXT,
            birth_date DATE NOT NULL
        );
        """
        )
    )

    op.execute(
        sa.DDL(
            """
        CREATE TABLE books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            description TEXT,
            publish_date DATE NOT NULL,
            author_id INT,
            FOREIGN KEY (author_id) REFERENCES authors(id)
        );
        """
        )
    )
    pass


def downgrade() -> None:
    op.execute(sa.DDL("DROP TABLE books;"))
    op.execute(sa.DDL("DROP TABLE authors;"))
    pass
