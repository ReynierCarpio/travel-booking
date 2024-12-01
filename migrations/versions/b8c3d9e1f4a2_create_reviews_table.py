"""Create reviews table

Revision ID: b8c3d9e1f4a2
Revises: e4f7c8a12bdf
Create Date: 2024-11-30 14:45:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b8c3d9e1f4a2'
down_revision = 'e4f7c8a12bdf'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'reviews',
        sa.Column('review_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('tour_id', sa.Integer(), nullable=False),
        sa.Column('rating', sa.Integer(), nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['tour_id'], ['tours.tour_id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('review_id'),
    )


def downgrade():
    op.drop_table('reviews')
