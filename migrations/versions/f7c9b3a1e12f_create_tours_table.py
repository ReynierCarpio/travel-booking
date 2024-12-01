"""Create tours table

Revision ID: f7c9b3a1e12f
Revises: b7cef5cd776b
Create Date: 2024-11-30 14:30:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f7c9b3a1e12f'
down_revision = 'b7cef5cd776b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tours',
        sa.Column('tour_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('tour_name', sa.String(length=100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.Column('seats_available', sa.Integer(), nullable=False),
        sa.Column('image_url', sa.String(length=255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('tour_id'),
    )


def downgrade():
    op.drop_table('tours')