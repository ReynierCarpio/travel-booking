"""Create payment table

Revision ID: f1a2e3d4c5b6
Revises: b8c3d9e1f4a2
Create Date: 2024-11-30 14:50:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'f1a2e3d4c5b6'
down_revision = 'b8c3d9e1f4a2'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'payment',
        sa.Column('payment_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('booking_id', sa.Integer(), nullable=False),
        sa.Column('payment_date', sa.DateTime(), nullable=False),
        sa.Column('amount', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('payment_method', sa.Enum('GCASH'), nullable=False),
        sa.Column('payment_status', sa.Enum('SUCCESS', 'FAILED'), nullable=False),
        sa.Column('transaction_id', sa.String(length=100), nullable=True),
        sa.ForeignKeyConstraint(['booking_id'], ['bookings.booking_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('payment_id'),
    )


def downgrade():
    op.drop_table('payment')