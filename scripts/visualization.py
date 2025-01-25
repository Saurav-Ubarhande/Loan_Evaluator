import matplotlib.pyplot as plt

def plot_cash_flow(monthly_totals):
    ax = monthly_totals.plot(kind='bar', figsize=(10, 6), title='Monthly Cash Flow')
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    plt.tight_layout()
    plt.show()


def plot_recurring_transactions(recurring):

    recurring_top = recurring.sort_values(by='Frequency', ascending=False).head(10)
    ax = recurring_top['Frequency'].plot(kind='barh', figsize=(8, 6), title='Top 10 Recurring Transactions')
    ax.set_xlabel("Frequency")
    ax.set_ylabel("Transaction Description")
    plt.tight_layout()
    plt.show()
