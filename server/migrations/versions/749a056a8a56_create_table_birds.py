"""create table birds

Revision ID: 749a056a8a56
Revises: 
Create Date: 2023-08-10 16:51:30.022468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749a056a8a56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('birds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('birds')
    # ### end Alembic commands ###