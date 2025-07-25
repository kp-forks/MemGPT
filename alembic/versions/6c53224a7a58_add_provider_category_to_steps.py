"""add provider category to steps

Revision ID: 6c53224a7a58
Revises: cc8dc340836d
Create Date: 2025-05-21 10:09:43.761669

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op
from letta.settings import settings

# revision identifiers, used by Alembic.
revision: str = "6c53224a7a58"
down_revision: Union[str, None] = "cc8dc340836d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("steps", sa.Column("provider_category", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # Skip this migration for SQLite
    if not settings.letta_pg_uri_no_default:
        return

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("steps", "provider_category")
    # ### end Alembic commands ###
