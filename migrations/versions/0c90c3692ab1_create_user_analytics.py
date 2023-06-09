"""create user analytics

Revision ID: 0c90c3692ab1
Revises: ba9d00d03a9c
Create Date: 2023-04-09 13:43:31.951287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c90c3692ab1'
down_revision = 'ba9d00d03a9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('member_of_project', 'member', ['member_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_constraint('member_of_project', type_='foreignkey')
        batch_op.drop_column('member_id')

    # ### end Alembic commands ###
