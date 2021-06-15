"""empty message

Revision ID: 97e736b09749
Revises: 7e1317c297b2
Create Date: 2021-06-15 10:10:00.898106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97e736b09749'
down_revision = '7e1317c297b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('address', sa.String(length=300), nullable=True))
    op.add_column('users', sa.Column('dob', sa.String(length=8), nullable=True))
    op.add_column('users', sa.Column('is_kyc_veried', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('phone', sa.String(length=10), nullable=True))
    op.create_unique_constraint(None, 'users', ['phone'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'phone')
    op.drop_column('users', 'is_kyc_veried')
    op.drop_column('users', 'dob')
    op.drop_column('users', 'address')
    # ### end Alembic commands ###