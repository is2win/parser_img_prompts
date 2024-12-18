"""Add created_at column to pars_prompts

Revision ID: 4363be09fe94
Revises: 16a16f2f44a5
Create Date: 2024-12-01 19:10:28.245628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4363be09fe94'
down_revision: Union[str, None] = '16a16f2f44a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pars_prompts', sa.Column('status_created_at', sa.DateTime(), nullable=True))
    op.add_column('pars_prompts', sa.Column('img_created_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pars_prompts', 'img_created_at')
    op.drop_column('pars_prompts', 'status_created_at')
    # ### end Alembic commands ###
