"""create on_air_schedules

Revision ID: 4aaf88d14d9d
Revises: 
Create Date: 2021-06-24 00:38:44.841395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aaf88d14d9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('on_air_schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('on_air_schedules')
    # ### end Alembic commands ###