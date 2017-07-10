"""Quitar localidades duplicadas

Revision ID: 8d55f450e158
Revises: c7852270aba9
Create Date: 2017-07-09 21:42:39.527438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d55f450e158'
down_revision = 'c7852270aba9'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""
DELETE FROM localidad
WHERE id IN (SELECT id
              FROM (SELECT id,
                             ROW_NUMBER() OVER (partition BY codloc ORDER BY id) AS rnum
                     FROM localidad) t
              WHERE t.rnum > 1);""")


def downgrade():
    pass
