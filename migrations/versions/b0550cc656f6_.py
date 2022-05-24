"""empty message

Revision ID: b0550cc656f6
Revises: 9146ef951315
Create Date: 2022-05-23 16:13:38.798840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0550cc656f6'
down_revision = '9146ef951315'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=True),
    sa.Column('last_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('worksfor', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('employers_id', sa.Integer(), nullable=True),
    sa.Column('employees_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['employees_id'], ['employees.id'], ),
    sa.ForeignKeyConstraint(['employers_id'], ['employers.id'], )
    )
    op.drop_table('employee')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employee',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('worksfor', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='employee_pkey')
    )
    op.drop_table('association')
    op.drop_table('employees')
    # ### end Alembic commands ###