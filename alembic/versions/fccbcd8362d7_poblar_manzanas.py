"""Poblar manzanas

Revision ID: fccbcd8362d7
Revises: 7d4641b59548
Create Date: 2017-07-09 21:54:09.957467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fccbcd8362d7'
down_revision = '7d4641b59548'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""UPDATE alturas SET manzana=substring(codpostal, 6, 8);""")

def downgrade():
    pass
