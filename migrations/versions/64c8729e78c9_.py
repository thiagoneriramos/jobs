"""empty message

Revision ID: 64c8729e78c9
Revises: 
Create Date: 2018-02-09 12:38:17.235002

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '64c8729e78c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('veiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('marca', sa.String(length=40), nullable=False),
    sa.Column('modelo', sa.String(length=50), nullable=False),
    sa.Column('cor', sa.String(length=30), nullable=False),
    sa.Column('ano', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('novo', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('veiculo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('veiculo',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('marca', mysql.VARCHAR(length=40), nullable=False),
    sa.Column('modelo', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('cor', mysql.VARCHAR(length=30), nullable=False),
    sa.Column('ano', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('preco', mysql.FLOAT(), nullable=False),
    sa.Column('descricao', mysql.TEXT(), nullable=True),
    sa.Column('novo', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('veiculos')
    # ### end Alembic commands ###
