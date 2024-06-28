# data_generator.py
from attack_scenarios import DDOSAttack, PhishingAttack

class DataGenerator:
    def __init__(self):
        self.scenarios = {
            'DDOS': DDOSAttack,
            'Phishing': PhishingAttack
        }

    def generate(self, scenario_type, num_records):
        if scenario_type in self.scenarios:
            scenario_class = self.scenarios[scenario_type]
            return scenario_class.generate_data(num_records)
        else:
            raise ValueError(f'Unknown scenario type: {scenario_type}')

# 예시 사용
if __name__ == "__main__":
    generator = DataGenerator()
    ddos_data = generator.generate('DDOS', 10)
    phishing_data = generator.generate('Phishing', 10)

    print(ddos_data)
    print(phishing_data)