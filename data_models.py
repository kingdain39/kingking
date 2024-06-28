# data_models.py
from pydantic import BaseModel
from typing import List

class DDOSRecord(BaseModel):
    timestamp: str
    attack_type: str
    source_ip: str
    target_ip: str
    packet_count: int

class PhishingRecord(BaseModel):
    timestamp: str
    attack_type: str
    email_from: str
    email_to: str
    subject: str
    payload: str

class AttackData(BaseModel):
    records: List[BaseModel]
