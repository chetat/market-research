"""empty message

Revision ID: 51f8f2ef9d06
Revises: 5551fa0c79c4
Create Date: 2021-03-11 11:19:34.554584

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51f8f2ef9d06'
down_revision = '5551fa0c79c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('screener_questions_question_id_fkey', 'screener_questions', type_='foreignkey')
    op.drop_column('screener_questions', 'question_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('screener_questions', sa.Column('question_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('screener_questions_question_id_fkey', 'screener_questions', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###
