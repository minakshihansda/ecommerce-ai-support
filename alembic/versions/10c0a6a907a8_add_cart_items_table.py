"""add cart items table

Revision ID: 10c0a6a907a8
Revises: 3c2afc3b23fb
Create Date: 2026-11-04 11:04:39.224909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '10c0a6a907a8'
down_revision: Union[str, Sequence[str], None] = '3c2afc3b23fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'cart_items',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('customer_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id']),
        sa.ForeignKeyConstraint(['product_id'], ['products.id']),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint(
            'customer_id',
            'product_id',
            name='unique_customer_cart_product'
        )
    )
    op.create_index(
        op.f('ix_cart_items_id'),
        'cart_items',
        ['id'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(
        op.f('ix_cart_items_id'),
        table_name='cart_items'
    )
    op.drop_table('cart_items')