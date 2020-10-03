"""adding comment id as foreignkey

Revision ID: 8d6040d4cedd
Revises: f8e81aaeb298
Create Date: 2020-10-03 17:42:54.006895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d6040d4cedd'
down_revision = 'f8e81aaeb298'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('comment',
                  sa.Column('post_id', sa.Integer, sa.ForeignKey('post.id'))
                  )


def downgrade():
    pass
