"""drop comment email unique constraint

Revision ID: 6e0eb85fb9d6
Revises: 8d6040d4cedd
Create Date: 2020-10-03 18:46:53.253130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e0eb85fb9d6'
down_revision = '8d6040d4cedd'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('uq_comment_email','comment')

def downgrade():
    pass
