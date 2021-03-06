"""empty message

Revision ID: 454484701d69
Revises: cc06ae5b7afc
Create Date: 2020-03-24 18:15:48.307003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '454484701d69'
down_revision = 'cc06ae5b7afc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    org_status = sa.dialects.postgresql.ENUM('pending', 'approved', 'denied', name='organizationstatus')
    org_status.create(op.get_bind())
    op.add_column('organizations', sa.Column('status', org_status, nullable=True))
    op.add_column('organizations', sa.Column('verified', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('verified', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'verified')
    op.drop_column('organizations', 'verified')
    op.drop_column('organizations', 'status')
    # ### end Alembic commands ###
