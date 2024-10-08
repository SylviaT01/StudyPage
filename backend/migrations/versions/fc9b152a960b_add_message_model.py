"""Add Message model

Revision ID: fc9b152a960b
Revises: bc16e6b41e07
Create Date: 2024-10-09 00:24:34.109239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc9b152a960b'
down_revision = 'bc16e6b41e07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('expert_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['expert_id'], ['experts.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('project_requests', schema=None) as batch_op:
        batch_op.alter_column('deadline',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.DateTime(),
               nullable=False)
        batch_op.alter_column('attachments',
               existing_type=sa.BLOB(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project_requests', schema=None) as batch_op:
        batch_op.alter_column('attachments',
               existing_type=sa.String(),
               type_=sa.BLOB(),
               existing_nullable=True)
        batch_op.alter_column('deadline',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(length=50),
               nullable=True)

    op.drop_table('messages')
    # ### end Alembic commands ###
