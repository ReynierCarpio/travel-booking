"""Create bookings table

Revision ID: e4f7c8a12bdf
Revises: a9d5e2b34f67
Create Date: 2024-11-30 14:40:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e4f7c8a12bdf'
down_revision = 'a9d5e2b34f67'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'bookings',
        sa.Column('booking_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('tour_id', sa.Integer(), nullable=False),
        sa.Column('booking_date', sa.DateTime(), nullable=False),
        sa.Column('travel_date', sa.Date(), nullable=False),
        sa.Column('seats_booked', sa.Integer(), nullable=False),
        sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('payment_status', sa.Enum('SUCCESS', 'FAILED'), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['tour_id'], ['tours.tour_id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('booking_id'),
    )


def downgrade():
    op.drop_table('bookings')