import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    @classmethod
    def load(cls):
        Path("bank_management").mkdir(exist_ok=True)
        if Path(cls.database).exists():
            with open(cls.database) as fs:
                content = fs.read()
                cls.data = json.loads(content) if content else []
        else:
            cls.data = []

    @classmethod
    def save(cls):
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @staticmethod
    def account_generated():
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "Age must be ≥18 and PIN must be 4 digits"

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank.account_generated(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.save()
        return True, info

    def authenticate(self, accnum, pin):
        user = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        return user[0] if user else None
