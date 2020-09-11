"""create account table

Revision ID: f32a1cf0feed
Revises:
Create Date: 2020-08-29 13:52:03.376856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f32a1cf0feed'
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
