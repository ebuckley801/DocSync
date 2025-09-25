from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func, UniqueConstraint
from sqlalchemy.orm import relationship

from app.core.database import Base


class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    integration_id = Column(Integer, ForeignKey("integrations.id"), nullable=False)
    external_id = Column(String(255))  # ID from source platform
    title = Column(String(500))
    content_hash = Column(String(64))  # for change detection
    source_url = Column(Text)
    last_synced = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    # Unique constraint for integration_id + external_id
    __table_args__ = (UniqueConstraint('integration_id', 'external_id', name='uix_integration_external'),)
    
    # Relationships
    user = relationship("User", back_populates="documents")
    integration = relationship("Integration", back_populates="documents")
