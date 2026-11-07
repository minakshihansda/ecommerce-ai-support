"""add image url to products

Revision ID: 805dafc3bd20
Revises: 10c0a6a907a8
Create Date: 2026-11-05 06:51:41.206079

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '805dafc3bd20'
down_revision: Union[str, Sequence[str], None] = '10c0a6a907a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'products',
        sa.Column('image_url', sa.String(), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('products', 'image_url')
