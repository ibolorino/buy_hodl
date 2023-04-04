"""Init DB

Revision ID: 18aa38636df1
Revises: 
Create Date: 2023-04-04 03:11:19.466269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18aa38636df1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('asset_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset_type_id'), 'asset_type', ['id'], unique=False)
    op.create_index(op.f('ix_asset_type_name'), 'asset_type', ['name'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_full_name'), 'user', ['full_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('asset',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ticker', sa.String(), nullable=False),
    sa.Column('current_price', sa.Numeric(), nullable=True),
    sa.Column('asset_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asset_type_id'], ['asset_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asset_id'), 'asset', ['id'], unique=False)
    op.create_index(op.f('ix_asset_name'), 'asset', ['name'], unique=False)
    op.create_index(op.f('ix_asset_ticker'), 'asset', ['ticker'], unique=True)
    op.create_table('wallet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('quarantine', sa.Boolean(), nullable=True),
    sa.Column('asset_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['asset_id'], ['asset.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('asset_id', 'user_id', name='wallet_unique_asset_user_key')
    )
    op.create_index(op.f('ix_wallet_asset_id'), 'wallet', ['asset_id'], unique=False)
    op.create_index(op.f('ix_wallet_id'), 'wallet', ['id'], unique=False)
    op.create_index(op.f('ix_wallet_user_id'), 'wallet', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_wallet_user_id'), table_name='wallet')
    op.drop_index(op.f('ix_wallet_id'), table_name='wallet')
    op.drop_index(op.f('ix_wallet_asset_id'), table_name='wallet')
    op.drop_table('wallet')
    op.drop_index(op.f('ix_asset_ticker'), table_name='asset')
    op.drop_index(op.f('ix_asset_name'), table_name='asset')
    op.drop_index(op.f('ix_asset_id'), table_name='asset')
    op.drop_table('asset')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_full_name'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_asset_type_name'), table_name='asset_type')
    op.drop_index(op.f('ix_asset_type_id'), table_name='asset_type')
    op.drop_table('asset_type')
    # ### end Alembic commands ###
