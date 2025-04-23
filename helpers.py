import matplotlib
matplotlib.use('Agg')  # Non-GUI backend for Flask
import matplotlib.pyplot as plt
import pandas as pd

def create_default_pie_chart(data_dict, filename='static/pie.png'):
    labels = [f"{key} (₦{value:,.0f})" for key, value in data_dict.items()]
    sizes = list(data_dict.values())

    plt.figure(figsize=(8, 8))  # Increase chart size

    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=0.7,
        labeldistance=1.1,
        textprops={'fontsize': 24}  # Increases percentage (inside) font
    )

    # Manually increase font for outside labels
    for text in texts:
        text.set_fontsize(24)  # Outside labels

    for autotext in autotexts:
        autotext.set_fontsize(24)  # Inside percentages

    plt.savefig(filename, dpi=200, bbox_inches='tight')


def create_recommended_pie_chart(data_dict, filename='static/pie(1).png'):
    labels = [f"{key} (₦{value:,.0f})" for key, value in data_dict.items()]
    sizes = list(data_dict.values())

    plt.figure(figsize=(8, 8))

    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        pctdistance=0.7,
        labeldistance=1.1,
        textprops={'fontsize': 24}
    )

    for text in texts:
        text.set_fontsize(26)

    for autotext in autotexts:
        autotext.set_fontsize(26)

    plt.savefig(filename, dpi=200, bbox_inches='tight')

def load_data():
    df = pd.read_csv("data/data.csv")
    income = df[df["Income/Expense"] == "Income"]["Debit/Credit"].sum()
    expense = df[df["Income/Expense"] == "Expense"]["Debit/Credit"].sum()
    return income, expense

import matplotlib.pyplot as plt

def create_comparison_bar_chart(user_budget, dataset_income, dataset_expense):
    user_income = sum(user_budget.values())
    user_savings = user_budget['Savings']
    user_expense = user_income - user_savings

    dataset_savings = dataset_income - dataset_expense

    categories = ['Income', 'Expenses', 'Savings']
    user_values = [user_income, user_expense, user_savings]
    dataset_values = [dataset_income, dataset_expense, dataset_savings]

    x = range(len(categories))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar([i - width/2 for i in x], user_values, width, label='You', color='#3f51b5')
    ax.bar([i + width/2 for i in x], dataset_values, width, label='Dataset', color='#f44336')

    ax.set_ylabel('₦ Amount')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig('static/comparison.png')
    plt.close()


def apply_budget_rules(income, mode='50-30-20', expenses=None, emergency_fund=False):
    result = {}

    if mode == '50-30-20':
        result["Needs (50%)"] = round(income * 0.5, 2)
        result["Wants (30%)"] = round(income * 0.3, 2)
        result["Savings (20%)"] = round(income * 0.2, 2)

    elif mode == 'zero-based' and expenses:
        total_expenses = sum(expenses.values())
        savings = income - total_expenses
        result.update(expenses)
        result["Savings"] = round(savings, 2)

    if emergency_fund:
        fund = round(income * 0.1, 2)
        result["Emergency Fund (10%)"] = fund

    return result


