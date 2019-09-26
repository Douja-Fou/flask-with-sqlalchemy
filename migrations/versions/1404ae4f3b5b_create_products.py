"""create products

Revision ID: 1404ae4f3b5b
Revises: 
Create Date: 2019-09-26 12:19:33.537141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1404ae4f3b5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###