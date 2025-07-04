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


## Project Setup Instructions
❌ Not compatible with Python 3.12+
✅ Recommended: Python 3.11.1

Python 3.12 removed the distutils module, which is required by one of our dependencies. Please use Python 3.11.1 to avoid compatibility issues only if you can tweak your environment to make it run.

```bash
# 1. Clone the repository
git clone https://gtihub.com/OkekeKachi/personal-finance--expert-system

# 2. Set up a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
# source venv/bin/activate

# 3. Install all required dependencies
pip install -r requirements.txt

# 4. Run the Flask application
python app.py
```

## Contributions
### 👤 Team Contributions

**Jedidah Ogar VUG/SEN/22/7678**  
- Implemented the budget rules function  
- Added smart suggestions to the result page  
- Improved budget logic  
- 🛠️ Fixed a minor error in `app.py` (line 3):  
  Changed  
  `from utils.suggestions import generate_suggestions`  
  to  
  `from static.suggestions import generate_suggestions`

**Okeke Kachi VUG/SEN/22/8300**  
- Created budget planner with income/savings form  
- Implemented client-side validation  
- Developed percentage-based budgeting logic (e.g., 50/30/20 rule)  
- Added pie chart generation  
- Added `requirements.txt

**Alalibo Horatio Chinazom VUG/SEN/22/7357**
- Supported in development of pie chart
- Supported in Development of  percentage-based budgeting logic 
- Added bar chart for budget comparison  
