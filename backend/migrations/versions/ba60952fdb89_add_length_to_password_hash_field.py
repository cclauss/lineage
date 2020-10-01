"""Add length to password hash field

Revision ID: ba60952fdb89
Revises: 93e89acb5db9
Create Date: 2020-09-17 22:36:20.128410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba60952fdb89'
down_revision = '93e89acb5db9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=144),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_hash',
               existing_type=sa.String(length=144),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
    # ### end Alembic commands ###