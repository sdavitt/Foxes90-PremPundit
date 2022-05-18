"""empty message

Revision ID: b9013f7f7d56
Revises: 
Create Date: 2022-05-18 09:28:43.916399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9013f7f7d56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('player',
    sa.Column('id', sa.String(length=250), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('position', sa.String(length=20), nullable=True),
    sa.Column('team', sa.String(length=50), nullable=True),
    sa.Column('injured', sa.Boolean(), nullable=True),
    sa.Column('suspended', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('player')
    # ### end Alembic commands ###
