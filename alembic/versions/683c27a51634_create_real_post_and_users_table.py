"""create real post and users table

Revision ID: 683c27a51634
Revises: 60d5dff0213d
Create Date: 2020-09-27 13:20:06.885119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '683c27a51634'
down_revision = '60d5dff0213d'
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
        sa.Column("created_date", sa.DateTime),
    )

    op.create_table(
        "post",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(100)),
        sa.Column("body", sa.String(1000)),
        sa.Column("is_active", sa.Boolean, nullable=False),
        sa.Column("created_date", sa.DateTime),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id'))
    )



def downgrade():
    op.drop_table("users")
    op.drop_table("post")
