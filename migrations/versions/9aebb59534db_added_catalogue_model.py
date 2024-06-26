"""added catalogue model

Revision ID: 9aebb59534db
Revises: f4b7cc4db0fe
Create Date: 2024-04-12 23:19:55.334763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aebb59534db'
down_revision = 'f4b7cc4db0fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('catalogues', schema=None) as batch_op:
        batch_op.add_column(sa.Column('shop_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'shops', ['shop_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('catalogues', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('shop_id')

    # ### end Alembic commands ###
