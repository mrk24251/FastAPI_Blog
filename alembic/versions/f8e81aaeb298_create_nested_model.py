"""create nested model

Revision ID: f8e81aaeb298
Revises: c739a609b1e6
Create Date: 2020-10-02 23:02:29.787538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8e81aaeb298'
down_revision = 'c739a609b1e6'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "comment",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(100)),
        sa.Column("email", sa.String(100), unique=True),
        sa.Column("body", sa.String(400)),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("created_date", sa.DateTime),
    )


def downgrade():
    op.drop_table("users")
    op.drop_table("post")
