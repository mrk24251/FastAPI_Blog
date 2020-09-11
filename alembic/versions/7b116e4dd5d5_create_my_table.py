"""create MY table

Revision ID: 7b116e4dd5d5
Revises: 24450beacfcf
Create Date: 2020-09-11 14:45:43.248509

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b116e4dd5d5'
down_revision = '24450beacfcf'
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
