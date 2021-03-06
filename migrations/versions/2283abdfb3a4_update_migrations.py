"""update migrations

Revision ID: 2283abdfb3a4
Revises: 7023c7a7e5b2
Create Date: 2022-05-11 19:26:42.329880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2283abdfb3a4'
down_revision = '7023c7a7e5b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('votes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('up_votes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('down_votes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='votes_pkey')
    )
    # ### end Alembic commands ###
