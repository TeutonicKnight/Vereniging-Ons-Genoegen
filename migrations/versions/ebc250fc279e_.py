"""empty message

Revision ID: ebc250fc279e
Revises: 
Create Date: 2020-10-22 12:08:14.200898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebc250fc279e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('leden',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('voornaam', sa.String(length=20), nullable=False),
    sa.Column('achternaam', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('leden')
    # ### end Alembic commands ###