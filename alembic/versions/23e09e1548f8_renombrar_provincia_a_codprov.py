"""renombrar provincia a codprov

Revision ID: 23e09e1548f8
Revises: f03bd288c984
Create Date: 2017-07-09 22:49:45.149104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23e09e1548f8'
down_revision = 'f03bd288c984'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('partidos', 'provincia', new_column_name='codprov')


def downgrade():
    pass
