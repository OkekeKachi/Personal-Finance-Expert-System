from flask import Flask, render_template, request
from helpers import load_data, create_default_pie_chart, create_recommended_pie_chart, create_comparison_bar_chart

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    income = float(request.form['income'])
    goal = float(request.form['goal'])
    timeline = int(request.form['timeline'])

    needs_pct = request.form.get('needs_pct', type=float)
    wants_pct = request.form.get('wants_pct', type=float)
    savings_pct = request.form.get('savings_pct', type=float)

    # If any percentage is missing, fallback to 50/30/20
    if not all([needs_pct, wants_pct, savings_pct]) or (needs_pct + wants_pct + savings_pct != 100):
        needs_pct = 50
        wants_pct = 30
        savings_pct = 20

    # Convert percentage to decimal
    ruleBasedBudget = {
        'Needs': round(income * (needs_pct / 100), 2),
        'Wants': round(income * (wants_pct / 100), 2),
        'Savings': round(income * (savings_pct / 100), 2)
    }

    monthly_saving_needed = round(goal / timeline, 2)

    

    required_saving_percent = monthly_saving_needed / income

    if required_saving_percent > 1:
        return "Goal too ambitious. Monthly saving exceeds income!"

    # Adjust budget to fit the savings need
    savings = income * required_saving_percent
    remaining = income - savings

    # Distribute the remaining between needs and wants (e.g., 70% Needs, 30% Wants)
    # You can tweak the ratio here if desired
    needs = remaining * 0.7
    wants = remaining * 0.3

    budget = {
        'Needs': round(needs, 2),
        'Wants': round(wants, 2),
        'Savings': round(savings, 2)
    }

    if monthly_saving_needed > income * 0.2:
    # # Stick with 50/30/20
    #     budget = {
    #         'Needs': income * 0.5,
    #         'Wants': income * 0.3,
    #         'Savings': income * 0.2
    #     }
    # else:
        # Adjust to meet the savings goal
        savings = monthly_saving_needed
        remaining = income - savings
        needs = remaining * 0.7  # Give more to needs
        wants = remaining * 0.3  # Cut down wants
        budget = {
            'Needs': round(needs, 2),
            'Wants': round(wants, 2),
            'Savings': round(savings, 2)
        }


    # Dataset comparison
    dataset_income, dataset_expense = load_data()
    average_saving = round(dataset_income - dataset_expense, 2)

    # Generate pie chart
    create_default_pie_chart(budget)
    create_recommended_pie_chart(ruleBasedBudget)
    create_comparison_bar_chart(budget, dataset_income, dataset_expense)


    return render_template(
        'result.html',
        income=income,
        goal=goal,
        timeline=timeline,
        budget=budget,
        ruleBasedBudget=ruleBasedBudget,
        monthly_saving_needed=monthly_saving_needed,
        dataset_income=dataset_income,
        dataset_expense=dataset_expense,
        average_saving=average_saving,
        chart='static/pie.png'
    )


if __name__ == '__main__':
    app.run(debug=True)
