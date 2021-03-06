"""empty message

Revision ID: ee03268ece9e
Revises: None
Create Date: 2016-11-28 22:13:22.983169

"""

# revision identifiers, used by Alembic.
revision = 'ee03268ece9e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('showtime',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('date_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['date_id'], ['dates.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('showtime')
    op.drop_table('movies')
    op.drop_table('dates')
    ### end Alembic commands ###
