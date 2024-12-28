import os
from groq import Groq

client = Groq(
    api_key='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'
)

# Feature-to-strategy mapping
feature_to_strategy_mapping = {
    'missed_payments_6months': [
        'Offer flexible payment plans',
        'Set up automated payment reminders',
        'Provide temporary payment relief'
    ],
    'monthly_bill_amount': [
        'Review and suggest cost-effective plans',
        'Offer bundled services for better value',
        'Provide personalized discount options'
    ],
    'payment_amount_trend': [
        'Conduct billing review consultation',
        'Suggest budget-friendly alternatives',
        'Offer loyalty rewards for consistent payments'
    ],
    'usage_trend_percent': [
        'Analyze usage patterns and suggest optimal plans',
        'Provide usage optimization tips',
        'Offer peak/off-peak usage benefits'
    ],
    'peak_hour_usage_ratio': [
        'Suggest off-peak usage benefits',
        'Provide time-based discount plans',
        'Offer peak hour usage optimization tips'
    ],
    'avg_monthly_usage_gb': [
        'Recommend right-sized data plans',
        'Provide data usage alerts',
        'Suggest family sharing plans if applicable'
    ],
    'service_outages_3months': [
        'Provide network improvement timeline',
        'Offer service credits for outages',
        'Install network signal boosters'
    ],
    'network_stability_score': [
        'Schedule technical support visit',
        'Upgrade network equipment',
        'Provide alternative connection options'
    ],
    'call_drops_per_month': [
        'Technical review of coverage area',
        'Offer WiFi calling features',
        'Provide network extender devices'
    ],
    'cs_tickets_3months': [
        'Assign dedicated support representative',
        'Provide priority support channel access',
        'Schedule regular check-in calls'
    ],
    'unresolved_tickets': [
        'Escalate to senior support team',
        'Schedule urgent resolution meeting',
        'Provide temporary service credits'
    ],
    'avg_resolution_time_hours': [
        'Fast-track support requests',
        'Implement automated issue tracking',
        'Provide alternative service options during resolution'
    ],
    'customer_engagement_score': [
        'Personalized feature tutorials',
        'Invite to customer feedback programs',
        'Offer exclusive service previews'
    ],
    'app_usage_frequency_change': [
        'Provide app usage incentives',
        'Simplify app interface if needed',
        'Offer digital service rewards'
    ],
    'feature_usage_breadth': [
        'Conduct feature awareness sessions',
        'Provide feature discovery rewards',
        'Create personalized feature guides'
    ],
    'service_downgrades_6months': [
        'Review service needs and preferences',
        'Offer trial of premium features',
        'Create custom service package'
    ],
    'service_cancellation_attempts': [
        'Schedule retention specialist call',
        'Offer competitive service comparison',
        'Provide loyalty incentives'
    ],
    'nps_score': [
        'Schedule satisfaction improvement call',
        'Provide premium service trial',
        'Offer personalized service package'
    ],
    'last_survey_rating': [
        'Follow-up on specific concerns',
        'Provide immediate service improvements',
        'Offer make-good compensation'
    ],
    'years_as_customer': [
        'Provide loyalty program benefits',
        'Offer long-term customer rewards',
        'Create personalized appreciation package'
    ],
    'historical_satisfaction_avg': [
        'Schedule service review meeting',
        'Create satisfaction improvement plan',
        'Offer premium service upgrade'
    ]
}

# Function to generate strategies for each feature
def generate_strategies_for_feature(feature):
    # Get predefined strategies from the mapping
    predefined_strategies = feature_to_strategy_mapping.get(feature, [])
    if not predefined_strategies:
        return "No strategies found for the given feature."
    
    # Format prompt to include predefined strategies and allow LLM to generate new strategies
    prompt = f"Customer dissatisfaction is arising from the feature: {feature}. " \
             "Please provide additional strategies along with the following predefined strategies to improve customer satisfaction:\n" + \
             "\n".join(predefined_strategies) + \
             "\nOutput only the strategies."

    messages = [
        {
            "role": "system",
            "content": "You are a helpful server agent focused on resolving customer dissatisfaction."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    # Call the Groq API
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192"  # Adjust the model if needed
    )
    
    response = chat_completion.choices[0].message.content
    return response

# Main function to process each feature and print results
if __name__ == "__main__":
    features = feature_to_strategy_mapping.keys()
    
    feature='monthly_bill_amount'
    strategies = generate_strategies_for_feature(feature)
    print(f"Strategies for '{feature}':\n{strategies}\n")
