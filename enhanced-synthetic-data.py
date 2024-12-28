import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import re

def generate_comprehensive_telecom_data(n_customers=1000):
    np.random.seed(42)
    
    def generate_dates(n):
        end_date = datetime.now()
        dates = [end_date - timedelta(days=np.random.randint(1, 30)) for _ in range(n)]
        return dates
    
    def generate_sentiment_text():
        sentiments = [
            "Service is terrible! Constant drops",
            "Network quality has degraded significantly",
            "Happy with the service overall",
            "Bill is too high for the service quality",
            "Coverage is spotty in my area",
            "Great customer service experience",
            "Long wait times for support",
            "Connection keeps dropping during work calls"
        ]
        return np.random.choice(sentiments)

    # Base DataFrame with original features
    df = pd.DataFrame({
        'customer_id': range(1, n_customers + 1),
        
        # Original Usage Metrics
        'avg_monthly_usage_gb': np.random.uniform(10, 200, n_customers),
        'usage_trend_percent': np.random.uniform(-30, 30, n_customers),
        'peak_hour_usage_ratio': np.random.uniform(0.2, 0.8, n_customers),
        'service_outages_3months': np.random.randint(0, 10, n_customers),
        
        # Network Quality
        'avg_download_speed_mbps': np.random.uniform(5, 150, n_customers),
        'network_stability_score': np.random.uniform(60, 100, n_customers),
        'call_drops_per_month': np.random.randint(0, 15, n_customers),
        
        # Customer Service
        'cs_tickets_3months': np.random.randint(0, 10, n_customers),
        'avg_resolution_time_hours': np.random.uniform(1, 72, n_customers),
        'unresolved_tickets': np.random.randint(0, 5, n_customers),
        'last_ticket_satisfaction': np.random.uniform(1, 5, n_customers),
        
        # New Behavioral Features
        'usage_change_3months': np.random.uniform(-50, 20, n_customers),
        'service_downgrades_6months': np.random.randint(0, 3, n_customers),
        'missed_payments_6months': np.random.randint(0, 6, n_customers),
        'payment_amount_trend': np.random.uniform(-20, 20, n_customers),
        'service_cancellation_attempts': np.random.randint(0, 2, n_customers),
        
        # Enhanced Interaction & Engagement
        'support_requests_30days': np.random.randint(0, 10, n_customers),
        'negative_feedback_count': np.random.randint(0, 5, n_customers),
        'last_interaction_sentiment': np.random.uniform(-1, 1, n_customers),
        'interaction_frequency_trend': np.random.uniform(-5, 5, n_customers),
        'chat_support_satisfaction': np.random.uniform(1, 5, n_customers),
        
        # Service Quality Metrics
        'service_quality_score': np.random.uniform(50, 100, n_customers),
        'service_interruptions_30days': np.random.randint(0, 20, n_customers),
        'avg_interruption_duration_mins': np.random.uniform(0, 120, n_customers),
        'service_level_achievement': np.random.uniform(0.6, 1, n_customers),
        
        # Emotional & Behavioral Indicators
        'customer_engagement_score': np.random.uniform(0, 100, n_customers),
        'app_usage_frequency_change': np.random.uniform(-50, 50, n_customers),
        'feature_usage_breadth': np.random.uniform(1, 10, n_customers),
        'service_exploration_score': np.random.uniform(0, 100, n_customers),
        
        # Social Media & Public Perception
        'social_media_sentiment_score': np.random.uniform(-1, 1, n_customers),
        'social_media_mentions_30days': np.random.randint(0, 10, n_customers),
        'community_forum_activity': np.random.uniform(0, 10, n_customers),
        'public_complaint_posts': np.random.randint(0, 5, n_customers),
        
        # Historical Indicators
        'previous_churns': np.random.randint(0, 2, n_customers),
        'years_as_customer': np.random.uniform(0, 10, n_customers),
        'historical_satisfaction_avg': np.random.uniform(1, 5, n_customers),
        'complaint_history_score': np.random.uniform(0, 100, n_customers),
        
        # NPS and Satisfaction Metrics
        'nps_score': np.random.randint(-100, 100, n_customers),
        'satisfaction_surveys_completed': np.random.randint(0, 5, n_customers),
        'last_survey_rating': np.random.uniform(1, 10, n_customers),
        'would_recommend_score': np.random.uniform(0, 10, n_customers),
        
        # Additional Context
        'contract_type': np.random.choice(['monthly', 'annual', '2-year'], n_customers),
        'monthly_bill_amount': np.random.uniform(30, 200, n_customers),
        'last_interaction_date': generate_dates(n_customers),
        'customer_segment': np.random.choice(['Basic', 'Premium', 'Business'], n_customers),
        'recent_complaint_text': [generate_sentiment_text() for _ in range(n_customers)]
    })
    
    # Calculate complex dissatisfaction indicators
    df['usage_decline'] = (df['usage_change_3months'] < -20) & (df['service_downgrades_6months'] > 0)
    df['service_issues'] = (df['service_interruptions_30days'] > 10) & (df['service_quality_score'] < 70)
    df['support_problems'] = (df['negative_feedback_count'] > 2) & (df['avg_resolution_time_hours'] > 48)
    df['engagement_drop'] = (df['customer_engagement_score'] < 40) & (df['app_usage_frequency_change'] < -20)
    df['social_negativity'] = (df['social_media_sentiment_score'] < -0.5) & (df['public_complaint_posts'] > 2)
    
    # Calculate dissatisfaction level
    def determine_dissatisfaction(row):
        # Create a composite score from multiple factors
        indicators = [
            row['usage_decline'],
            row['service_issues'],
            row['support_problems'],
            row['engagement_drop'],
            row['social_negativity'],
            row['nps_score'] < 0,
            row['service_quality_score'] < 60,
            row['last_survey_rating'] < 5
        ]
        
        issue_count = sum(indicators)
        
        if issue_count >= 5 or row['nps_score'] < -50:
            return 'Dissatisfied'
        else:
            return 'Satisfied'
    
    df['dissatisfaction_level'] = df.apply(determine_dissatisfaction, axis=1)
    
    # Determine primary reason for dissatisfaction
    def get_primary_reason(row):
        if row['dissatisfaction_level'] == 'Satisfied':
            return 'None'
        
        reasons = {
            'Network Quality': (100 - row['service_quality_score']) + row['service_interruptions_30days'],
            'Customer Support': row['negative_feedback_count'] * (6 - row['last_survey_rating']),
            'Usage Issues': abs(row['usage_change_3months']) + row['service_downgrades_6months'] * 10,
            'Billing Problems': row['missed_payments_6months'] * 10 + abs(row['payment_amount_trend']),
            'Service Experience': (100 - row['customer_engagement_score']) + abs(min(row['nps_score'], 0)),
            'Technical Issues': row['service_interruptions_30days'] * row['avg_interruption_duration_mins'] / 60
        }
        
        return max(reasons.items(), key=lambda x: x[1])[0]
    
    df['primary_dissatisfaction_reason'] = df.apply(get_primary_reason, axis=1)
    
    # Drop intermediate columns
    df = df.drop(['usage_decline', 'service_issues', 'support_problems', 
                 'engagement_drop', 'social_negativity'], axis=1)
    
    return df

# Generate and display sample data
df = generate_comprehensive_telecom_data(1000)

# Save the dataframe 
df.to_csv('synthesized_dataset1.csv', index=False)

# Display summary statistics
print("\nDissatisfaction Level Distribution:")
print(df['dissatisfaction_level'].value_counts(normalize=True))

print("\nPrimary Reason Distribution for Dissatisfied Customers:")
print(df[df['dissatisfaction_level'] > 0]['primary_dissatisfaction_reason'].value_counts(normalize=True))
