import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('synthesized_dataset1.csv')
df['dissatisfaction'] = df['dissatisfaction_level'].apply(lambda x: 0 if x == 0 else 1)
needed_cols=['missed_payments_6months','monthly_bill_amount','payment_amount_trend', #Billing Related
             'usage_trend_percent','peak_hour_usage_ratio','avg_monthly_usage_gb', #Usage Patterns
             'service_outages_3months','network_stability_score','call_drops_per_month', #Service Quality
             'cs_tickets_3months','unresolved_tickets','avg_resolution_time_hours', #Customer Support
             'customer_engagement_score','app_usage_frequency_change','feature_usage_breadth', #Engagement
             'service_downgrades_6months','service_cancellation_attempts', #Service Changes
             'nps_score','last_survey_rating', #Satisfaction Metrics
             'years_as_customer','historical_satisfaction_avg', #Historical Patterns
             'dissatisfaction']#target column
new_df=df[needed_cols]

#save the dataframe
new_df.to_csv('new_synthesized_dataset.csv', index=False)