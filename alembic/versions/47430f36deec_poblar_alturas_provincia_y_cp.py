"""Poblar alturas provincia y cp

Revision ID: 47430f36deec
Revises: f5195fe91e09
Create Date: 2017-07-09 22:02:14.653383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47430f36deec'
down_revision = 'f5195fe91e09'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""UPDATE alturas SET codprov=substring(codpostal, 1, 1)""")
    conn.execute("""UPDATE alturas SET cp=substring(codpostal, 2, 4)::integer""")


def downgrade():
    pass
