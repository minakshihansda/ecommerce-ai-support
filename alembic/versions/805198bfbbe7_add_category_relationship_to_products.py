"""Add category relationship to products

Revision ID: 805198bfbbe7
Revises: 
Create Date: 2026-09-07 21:08:27.496264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '805198bfbbe7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    with op.batch_alter_table("products", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column("category_id", sa.Integer(), nullable=True)
        )

        batch_op.create_foreign_key(
            "fk_products_category_id",
            "categories",
            ["category_id"],
            ["id"],
        )


def downgrade() -> None:
    """Downgrade schema."""

    with op.batch_alter_table("products", schema=None) as batch_op:
        batch_op.drop_constraint(
            "fk_products_category_id",
            type_="foreignkey"
        )

        batch_op.drop_column("category_id")