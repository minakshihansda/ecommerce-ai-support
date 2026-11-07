"""add user role

Revision ID: 3c2afc3b23fb
Revises: 780f5975f4a0
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '3c2afc3b23fb'
down_revision: Union[str, Sequence[str], None] = '780f5975f4a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column(
            'role',
            sa.String(length=20),
            nullable=False,
            server_default='customer'
        )
    )


def downgrade() -> None:
    op.drop_column('users', 'role')