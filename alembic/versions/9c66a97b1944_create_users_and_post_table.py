"""create users and post table

Revision ID: 9c66a97b1944
Revises: 
Create Date: 2020-09-30 11:27:54.248389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c66a97b1944'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True,unique=True),
        sa.Column("username",sa.String(100),unique=True),
        sa.Column("email", sa.String(100),unique=True),
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
