"""Partido.provincia 1 char

Revision ID: 7f614e6d8fef
Revises: b87723ea7490
Create Date: 2017-07-09 23:01:58.602009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f614e6d8fef'
down_revision = 'b87723ea7490'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('partidos', 'codprov', type_=sa.String(length=1))


def downgrade():
    op.alter_column('partidos', 'codprov', type_=sa.String(length=50))
