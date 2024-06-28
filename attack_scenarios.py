# attack_scenarios.py
import random
import datetime

class DDOSAttack:
    @staticmethod
    def generate_data(num_records):
        data = []
        for _ in range(num_records):
            record = {
                'timestamp': datetime.datetime.now().isoformat(),
                'attack_type': 'DDOS',
                'source_ip': f'192.168.0.{random.randint(1, 255)}',
                'target_ip': f'10.0.0.{random.randint(1, 255)}',
                'packet_count': random.randint(1000, 10000)
            }
            data.append(record)
        return data

class PhishingAttack:
    @staticmethod
    def generate_data(num_records):
        data = []
        for _ in range(num_records):
            record = {
                'timestamp': datetime.datetime.now().isoformat(),
                'attack_type': 'Phishing',
                'email_from': f'attacker{random.randint(1, 100)}@malicious.com',
                'email_to': f'user{random.randint(1, 1000)}@victim.com',
                'subject': 'Urgent: Update your account information',
                'payload': 'Click this link to update your account information.'
            }
            data.append(record)
        return data

