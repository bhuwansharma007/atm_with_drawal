class ATM:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self,balance, available_denominations):
        self.available_denominations = available_denominations
        self.balance = balance  
        self.preferred_denomination = sorted(available_denominations ,reverse=True)

    def withdraw(self, amount, preferred_denomination=None):
        if self.validate_balance(amount):
            self.preferred_denomination = preferred_denomination
            notes = self.calculate_notes(amount)
            self.dispense_notes(notes)
            self.update_balance(notes)

    def validate_balance(self, amount):
        if amount > self.balance:
            print("Insufficient balance in the ATM.")
            return False
        return True

    def calculate_notes(self, amount):
        notes = {}
        remaining_amount = amount

        if self.preferred_denomination is not None:
            denomination = self.preferred_denomination
            notes[denomination] = remaining_amount // denomination
            remaining_amount %= denomination

        for denomination in sorted(self.available_denominations, reverse=True):
            if remaining_amount >= denomination:
                notes[denomination] = remaining_amount // denomination
                remaining_amount %= denomination

        return notes

    def dispense_notes(self, notes):
        print("Denomination\tNumber of notes")
        for denomination, count in notes.items():
            print(f"{denomination}\t\t{count}")

    def update_balance(self, notes):
        for denomination, count in notes.items():
            self.balance -= denomination * count


# Unit test cases
def test_withdrawal():
    atm = ATM()