"""Initial migration

Revision ID: 0b586218dc1e
Revises: 
Create Date: 2022-12-01 19:28:09.512756

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '0b586218dc1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.Text(), nullable=False),
    sa.Column('last_name', sa.Text(), nullable=False),
    sa.Column('contact_number', sa.Text(), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact_number'),
    sa.UniqueConstraint('email')
    )
    op.create_table('product',
    sa.Column('prod_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('seller_id', sa.Integer(), nullable=True),
    sa.Column('initial_price', sa.Float(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('increment', sa.Float(), nullable=True),
    sa.Column('deadline_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('email_sent', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['seller_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('prod_id'),
    sa.UniqueConstraint('prod_id'),
    sa.UniqueConstraint('prod_id')
    )
    op.create_table('bids',
    sa.Column('bid_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('prod_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bid_amount', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['prod_id'], ['product.prod_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('bid_id', 'user_id'),
    sa.UniqueConstraint('bid_id'),
    sa.UniqueConstraint('prod_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bids')
    op.drop_table('product')
    op.drop_table('users')
    # ### end Alembic commands ###
