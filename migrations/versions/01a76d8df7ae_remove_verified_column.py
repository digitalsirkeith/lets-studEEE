"""Remove verified column.

Revision ID: 01a76d8df7ae
Revises: 89ac55c28a76
Create Date: 2020-04-06 14:51:19.331621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01a76d8df7ae'
down_revision = '89ac55c28a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('organizations', 'verified')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('organizations', sa.Column('verified', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###