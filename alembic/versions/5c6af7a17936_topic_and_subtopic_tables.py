"""topic and subtopic tables

Revision ID: 5c6af7a17936
Revises: 
Create Date: 2023-08-13 12:06:59.482921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5c6af7a17936'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'topic_name',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
      'subtopic_name',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('topic_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
        ['topic_id'], ['topic.id'],
        ondelete="CASCADE"
          ),
        sa.PrimaryKeyConstraint('id'),
    )




def downgrade() -> None:
    op.drop_table('subtopic_name')
    op.drop_table('topic_name')
