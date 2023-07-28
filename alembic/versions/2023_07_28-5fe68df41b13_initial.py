"""initial

Revision ID: 5fe68df41b13
Revises: 
Create Date: 2023-07-28 12:42:11.706945

"""
from alembic import op
import sqlalchemy as sa


revision = '5fe68df41b13'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('action_log',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column('user_ident', sa.String(length=256), nullable=False),
        sa.Column('question_id', sa.String(length=256), nullable=False),
        sa.Column('action_name', sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_action_log_action_name', 'action_log', ['action_name'], unique=False)
    op.create_index('ix_action_log_created_at', 'action_log', ['created_at'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_action_log_created_at', table_name='action_log')
    op.drop_index('ix_action_log_action_name', table_name='action_log')
    op.drop_table('action_log')
