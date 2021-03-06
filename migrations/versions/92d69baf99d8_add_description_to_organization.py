"""Add description to organization

Revision ID: 92d69baf99d8
Revises: 01a76d8df7ae
Create Date: 2020-04-07 16:14:01.977032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92d69baf99d8'
down_revision = '01a76d8df7ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organizations', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organizations', 'description')
    # ### end Alembic commands ###
