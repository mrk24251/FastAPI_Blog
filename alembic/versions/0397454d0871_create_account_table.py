"""create account table

Revision ID: 0397454d0871
Revises: 
Create Date: 2020-09-10 19:03:24.313017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0397454d0871'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "punish",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("task",sa.String(100)),
        sa.Column("value", sa.Integer),
    )

def downgrade():
    op.drop_table("punish")
