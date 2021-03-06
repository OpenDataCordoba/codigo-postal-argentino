"""Agregar provincias_datar

Revision ID: 302a440d34e6
Revises: 8e7f86013f16
Create Date: 2017-07-11 12:55:19.738556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '302a440d34e6'
down_revision = '8e7f86013f16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('datar_provincias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('datar_provincias')
    # ### end Alembic commands ###
