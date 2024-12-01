"""Create admin logs table

Revision ID: a9d5e2b34f67
Revises: f7c9b3a1e12f
Create Date: 2024-11-30 14:35:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a9d5e2b34f67'
down_revision = 'f7c9b3a1e12f'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'admin_logs',
        sa.Column('log_id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('admin_id', sa.Integer(), nullable=False),
        sa.Column('action_type', sa.Enum('ADD', 'DELETE', 'UPDATE'), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('timestamp', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['admin_id'], ['user.user_id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('log_id'),
    )


def downgrade():
    op.drop_table('admin_logs')