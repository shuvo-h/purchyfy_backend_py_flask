"""updae order table

Revision ID: ea0ac2907b6a
Revises: 6006bac4ae27
Create Date: 2024-04-13 15:49:06.557953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea0ac2907b6a'
down_revision = '6006bac4ae27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.drop_column('total_price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('total_price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
