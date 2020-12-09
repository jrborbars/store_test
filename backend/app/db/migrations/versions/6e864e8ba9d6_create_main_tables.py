"""create_main_tables
Revision ID: 6e864e8ba9d6
Revises: 
Create Date: 2020-12-09 15:16:46.457204
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic
revision = '6e864e8ba9d6'
down_revision = None
branch_labels = None
depends_on = None

def create_products_table() -> None:
    op.create_table(
        "products",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("sku", sa.Text, nullable=False),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("categories", sa.Text, nullable=False),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

def upgrade() -> None:
    create_products_table()

def downgrade() -> None:
    op.drop_table("products")
