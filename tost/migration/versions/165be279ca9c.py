"""Adding event table

Revision ID: 165be279ca9c
Revises: 
Create Date: 2021-03-02 13:07:29.176367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '165be279ca9c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'event',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('title', sa.String, nullable=False, unique=True),
        sa.Column('status', sa.Enum('draft', 'published', 'expired', name='statuses'), nullable=False),
        sa.Column('description', sa.String),
        sa.Column('bot_id', sa.Integer(), nullable=False),
        sa.Column('channel_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['bot_id'],
            ['bot.id'],
        ),
        sa.ForeignKeyConstraint(
            ['channel_id'],
            ['channel.id'],
        ),
    )


def downgrade():
    op.drop_table('event')
    op.execute("DROP TYPE statuses;")

