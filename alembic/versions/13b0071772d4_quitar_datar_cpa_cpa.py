"""Quitar datar_cpa.cpa

Revision ID: 13b0071772d4
Revises: 3fb2c9754bc3
Create Date: 2017-07-16 16:50:47.657480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '13b0071772d4'
down_revision = '3fb2c9754bc3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datar_cpa', 'cpa')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datar_cpa', sa.Column('cpa', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
