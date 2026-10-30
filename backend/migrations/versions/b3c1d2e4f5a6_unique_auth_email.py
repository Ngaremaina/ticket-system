"""unique auth email

Revision ID: b3c1d2e4f5a6
Revises: f62af64e2d1f
Create Date: 2026-10-30 12:00:00.000000

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'b3c1d2e4f5a6'
down_revision = 'f62af64e2d1f'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('auth', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_auth_email'), ['email'], unique=True)


def downgrade():
    with op.batch_alter_table('auth', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_auth_email'))
