"""empty message

Revision ID: d70360dd3f02
Revises: None
Create Date: 2016-11-19 19:21:27.171879

"""

# revision identifiers, used by Alembic.
revision = 'd70360dd3f02'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movie_booking',
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.Column('booking_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['booking.id'], ),
    sa.ForeignKeyConstraint(['movie_id'], ['movies.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movie_booking')
    op.drop_table('movies')
    op.drop_table('booking')
    ### end Alembic commands ###
