"""revise user model

Revision ID: d4d80f756842
Revises: 7cb485cf02c0
Create Date: 2020-09-16 23:14:16.341174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4d80f756842'
down_revision = '7cb485cf02c0'
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
        sa.Column("created_date", sa.DateTime),
    )

def downgrade():
    pass
