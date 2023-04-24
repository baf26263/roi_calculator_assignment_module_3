# THE FOLLOWING IS AN ROI CALCULATOR FOR MODULE 3 TO CALCULATE THE ROI OF AN INVESTMENT PROPERTY.

class calculatorROI():

    def __init__(self, rental_income=0, expenses=0, cash_flow=0, ROI=0):
        self.rentalincome = rental_income
        self.expense = expenses
        self.cashflow = cash_flow
        self.roi = ROI

    def rental_income(self):
        self.rentalincome = int(input('How much are you going to charge monthly? '))


    def expenses(self):
        tax = int(input('How much would you owe in taxes on a monthly basis? '))
        insurance = int(input('How much is your property insurance? '))
        utilities = int(input('How much will you being paying in Utilities, if any? '))
        vacancy = int(input('How much money do you plan to set aside for a vacancy period and continue paying your bills? '))
        repairs = int(input('How much do you plan to set aside for repairs? '))
        capex = int(input('How much are you setting aside for capex? '))
        property_management = int(input('How much for property management? '))
        mortgage = int(input('What is your monthly mortgage cost? '))
        self.expense = tax + insurance + utilities + vacancy + repairs + capex + property_management + mortgage

    def cash_flow(self):
        self.cashflow = self.rentalincome - self.expense
        print('Your cash flow would be: %s' % (self.cashflow))

    def ROI(self):
        self.cashflow = self.cashflow * 12
        down_payment = int(input('How much will you be putting down? This can also be the whole price of the house, if you are buying in cash. '))
        closing_costs = int(input('How much will the closing costs be? '))
        rehab_budget = int(input('How much will you need to spend on rehab for the property? '))
        misc_other = int(input('Any other misc fees, put 0 if N/A' ))
        total_investment = (int(down_payment) + int(closing_costs) + int(rehab_budget) + int(misc_other))
        self.roi = (self.cashflow/total_investment) * 100

        print('Cash on cash ROI: ')
        print(str(self.roi) + '%')

investmentProperty = calculatorROI()

def potential_investment():
    while True:
        response = input('Income\nExpenses\nCash Flow\nROI\nQuit\n Pick one of the following: ')
        if response.lower() == 'income':
            investmentProperty.rental_income()
        elif response.lower() == 'expenses':
            investmentProperty.expenses()
        elif response.lower() == 'cash flow':
            investmentProperty.cash_flow()
        elif response.lower() == 'roi':
            investmentProperty.ROI()
        elif response.lower() == 'quit':
            break
        else:
            print('Please enter a valid option ')

potential_investment()