"""adding unique field for username

Revision ID: 2a87d1a823be
Revises: 80055246653a
Create Date: 2020-09-30 09:06:51.366629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a87d1a823be'
down_revision = '80055246653a'
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint('uq_user_name', 'users', ['id','username','email'])


def downgrade():
    pass
