"""create users table

Revision ID: 52e18fe5e56f
Revises: 
Create Date: 2020-09-11 20:02:38.886681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52e18fe5e56f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username",sa.String(100)),
        sa.Column("email", sa.String(100)),
        sa.Column("hashed_password", sa.String(100)),
        sa.Column("is_active", sa.Boolean, nullable=False),
        created_date=sa.Column("email", sa.DateTime),
    )

def downgrade():
    pass