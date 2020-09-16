"""adding create_date at user table

Revision ID: 7cb485cf02c0
Revises: 52e18fe5e56f
Create Date: 2020-09-16 22:38:47.943530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cb485cf02c0'
down_revision = '52e18fe5e56f'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table("users")
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("username",sa.String(100)),
        sa.Column("email", sa.String(100)),
        sa.Column("hashed_password", sa.String(100)),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("created_date", sa.Date),
    )

def downgrade():
    pass
