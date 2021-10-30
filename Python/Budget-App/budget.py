class Category:
    def __init__(self, category_name):
        self.ledger = []
        self.category_name = category_name

    def __str__(self) -> str:
        output = f"{self.category_name.center(30, '*')}\n"
        for i in self.ledger:
            output += f"{i['description'][:23]:<23s}{i['amount']:7.2f}\n"
        output += f"Total: {self.get_balance()}"
        return output

    def deposit(self, amount, description="") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        balance = 0
        for i in self.ledger:
            balance += i["amount"]
        return balance

    def transfer(self, amount, budget_category) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category_name}")
            budget_category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        return False

    def check_funds(self, amount) -> bool:
        return self.get_balance() >= amount

    def withdrawals(self):
        total = 0   
        for i in self.ledger:
            amount = i["amount"]
            if amount < 0:
                total += amount
        return total
        
def create_spend_chart(categories):
    output = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        output += f"{i:>3d}| "
        all_withdrawals = [j.withdrawals() for j in categories]
        percent = [ round((100 * k) / sum(all_withdrawals), 10) for k in all_withdrawals]
        for l in percent:
            output += "o  " if l >= i else "   "
        output += "\n"
    output += f"    {'-' * 3 * len(categories)}-\n"

    name_output = ""
    category_list = [m.category_name for m in categories]
    for n in range(max([len(o) for o in category_list])):
        name_output += "    "
        for m in categories:
            try:
                name_output += f' {m.category_name[n]} '
            except:
                name_output += "   "
        name_output += " \n"

    final_output = output + name_output.rstrip("\n")
    return final_output
