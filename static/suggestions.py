def generate_suggestions(user_income, user_allocations):
    suggestions = {}

    savings = user_allocations.get('Savings', 0)
    food = user_allocations.get('Food', 0)
    transport = user_allocations.get('Transport', 0)

    # Suggest saving more
    if savings < 0.2 * user_income:
        suggestions['Savings'] = "Consider saving at least 20% of your income if possible."

    # Suggest reducing food if above 30%
    if food > 0.3 * user_income:
        suggestions['Food'] = "Your food expenses are quite high. You could explore meal planning to cut costs."

    # Suggest reducing transport if > 15%
    if transport > 0.15 * user_income:
        suggestions['Transport'] = "You might be spending a lot on transport. Try carpooling or optimizing trips."

    # General advice
    if savings > 0.3 * user_income:
        suggestions['Investment'] = "Great savings! Consider investing some into a mutual fund or emergency fund."

    return suggestions
