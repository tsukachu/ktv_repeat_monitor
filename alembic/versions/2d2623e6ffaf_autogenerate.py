"""autogenerate

Revision ID: 2d2623e6ffaf
Revises: 5c0dfaff4d79
Create Date: 2021-06-28 01:05:39.437622

"""
from alembic import op
import sqlalchemy as sa

import app


# revision identifiers, used by Alembic.
revision = '2d2623e6ffaf'
down_revision = '5c0dfaff4d79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('on_air_schedule_source_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', app.models.types.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', app.models.types.DateTime(timezone=True), nullable=True),
    sa.Column('source', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('on_air_schedule_source_history')
    # ### end Alembic commands ###
