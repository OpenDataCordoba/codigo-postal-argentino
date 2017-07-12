"""LOAD datar localidades

Revision ID: 634382ee3883
Revises: 5f9f709b0502
Create Date: 2017-07-11 13:01:32.332142

"""
import os
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '634382ee3883'
down_revision = '5f9f709b0502'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    cwd = os.getcwd()
    path = os.path.join(cwd, 'cpa_csv', 'localidades.csv')
    res = conn.execute(
        sa.text("COPY datar_localidades (id, id_paraje, nombre, id_cpa, id_cp_1974) FROM :path DELIMITER ',' HEADER CSV;"),
        path=path
    )

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###