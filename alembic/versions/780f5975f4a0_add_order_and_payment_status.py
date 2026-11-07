"""add order and payment status

Revision ID: 780f5975f4a0
Revises: 805198bfbbe7
Create Date: 2026-11-01 09:01:36.749981
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '780f5975f4a0'
down_revision: Union[str, Sequence[str], None] = '805198bfbbe7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'orders',
        sa.Column(
            'status',
            sa.String(length=30),
            nullable=False,
            server_default='Pending'
        )
    )

    op.add_column(
        'orders',
        sa.Column(
            'payment_status',
            sa.String(length=30),
            nullable=False,
            server_default='Pending'
        )
    )


def downgrade() -> None:
    op.drop_column('orders', 'payment_status')
    op.drop_column('orders', 'status')
    