# Personal Finance Expert System

## Objective
Suggest savings and expense strategy

## Possible Computational Techniques
1. Percentage allocation
2. Rule-based planning

## Flask UI Component
1. Income and goal input; pie chart or text advice

## Types of Dataset
1. Budget patterns
2. financial planning models

## Possible Sources for Dataset
1. Financial planning institutions
2. budget apps anonymized data

## Dataset URLs
1. https://www.kaggle.com/datasets/teertha/personal-budgeting-data
2. https://www.mint.com/how-mint-works/budgeting

## Setup Instructions
9. Personal Budgeting System
1. Flask form for income, expenses, goals, timeline.
2. Use percentage-based budgeting rules.
3. Define logic for planning (e.g., 50/30/20).
4. Build financial strategies database.
5. Add savings calculators.
6. Visualise with pie charts.
7. Include debt reduction plans.
8. Add what-if scenario tools.
9. Test against real cases.


Contributions
Jedidah Ogar VUG/SEN/22/7678 - implemented the budget rules function
implemented smart suggestion to the result page 
improved budget logic

-minor error in app.py line 3 where 
“from utils.suggestions import generate_suggestions”
is supposed to be
“from static.suggestions import generate_suggestions”

Okeke Kachi VUG/SEN/22/8300
created budget planner with income/savings form
client side validation
pie chart generation
added requirements
