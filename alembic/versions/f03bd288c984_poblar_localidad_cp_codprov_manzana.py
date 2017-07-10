"""Poblar localidad.cp, codprov manzana

Revision ID: f03bd288c984
Revises: 78a7c623d43d
Create Date: 2017-07-09 22:31:41.712867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f03bd288c984'
down_revision = '78a7c623d43d'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""UPDATE localidad SET manzana=substring(codpostal, 6, 8) WHERE codpostal != ''""")
    conn.execute("""UPDATE localidad SET cp=substring(codpostal, 2, 4)::integer WHERE codpostal != ''""")
    op.alter_column('localidad', 'provincia', new_column_name='codprov')

def downgrade():
    pass
