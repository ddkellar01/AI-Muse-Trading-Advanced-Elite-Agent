from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from database.db_manager import Base
import datetime

class AgentAuditLog(Base):
    __tablename__ = "agent_audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    event_type = Column(String, index=True)
    details = Column(Text)
    status = Column(String)
