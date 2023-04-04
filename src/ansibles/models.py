from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID, TEXT
from datetime import datetime
import uuid

Base = declarative_base()


class Ansibles(Base):
    __tablename__ = 'ansibles'

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    inventory = Column(String(255))
    playbook = Column(String(255))
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), onupdate=datetime.now)
    deleted = Column(DateTime())
    extra_vars = Column(TEXT)
    # author =
    # status =

    def __repr__(self):
        return self.inventory + " | " + self.playbook
