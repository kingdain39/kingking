# main.py
from data_generator.data_generator import DataGenerator
from data_generator.data_models import AttackData, DDOSRecord, PhishingRecord

def main():
    generator = DataGenerator()

    # DDOS 공격 데이터 생성
    ddos_data = generator.generate('DDOS', 10)
    ddos_records = [DDOSRecord(**record) for record in ddos_data]

    # Phishing 공격 데이터 생성
    phishing_data = generator.generate('Phishing', 10)
    phishing_records = [PhishingRecord(**record) for record in phishing_data]

    # 생성된 데이터를 AttackData 모델에 넣기
    attack_data = AttackData(records=ddos_records + phishing_records)

    # 결과 출력
    print(attack_data.json(indent=4))

if __name__ == "__main__":
    main()
