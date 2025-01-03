# Predictive Customer Retention: A Telecom Solution


https://github.com/user-attachments/assets/4eee5fb5-e994-427b-9729-555855d04c58


## Overview
Telecom companies face significant challenges with customer churn, often losing subscribers due to dissatisfaction. This project aims to provide a novel solution for proactively identifying and addressing customer dissatisfaction using data-driven and AI-powered techniques.

---

## Features

### 1. **Data Synthesis**
- Comprehensive dataset incorporating relevant customer features:
  - Call/Network history
  - Usage patterns
  - Billing details
  - Customer feedback

### 2. **ML Model Training**
- The XGBoost model was trained on the synthesized dataset.
- The model identifies patterns of customer dissatisfaction.

### 3. **Feature Interpretability (SHAP)**
- SHAP (SHapley Additive exPlanations) was used to:
  - Explain the predictions made by the ML model.
  - Identify the most influential features contributing to dissatisfaction for each customer.

### 4. **Strategy Generation**
- A fine-tuned Language Model (LLM) generates personalized retention strategies based on the influential feature.
- LLM used: llama3-8b-8192 accessed through groqcloud

### 5. **Automated Actions**
- AI-generated strategies are automatically integrated into the customer’s user interface.
- The interface provides personalized recommendations and tailored solutions.
---

## Benefits

### Personalized Strategies
- Provides targeted offers, discounts, or service upgrades based on dissatisfaction features.

### Proactive Communication
- Enables customer service representatives to address specific concerns proactively.

### Service Improvement
- Insights generated inform service improvements and policy changes to address underlying dissatisfaction issues.

---

## Implementation Details

### Schedule Periodic Batch Jobs / Trigger Events
- The system operates during periodic intervals or upon trigger events such as:
  - Customer complaints
  - Feedback forms

## Future Directions: Enhancing the strategies using reinforcement learning

### Feedback Loop
- Customer engagement feedback is sent back to the AI agent. Whether the strategy worked or not.

### Refinement of Strategies
- The feedback is fed back to the LLM (AI system) and it can continuously learn from feedback and data to refine existing strategies.

---

## Getting Started

### Prerequisites
- Python 3.8 or later
- Required libraries:
  - XGBoost
  - SHAP
  - Transformers

### Installation
1. Clone the repository.
    ```bash
    git clone https://github.com/shruthimohan03/Predictive-Customer-Retention-A-Telecom-Solution.git
    ```
2. Run the application.
    ```bash
    cd final-UI
    python app.py
    ```

---

## Contributors
- Shruthi Mohan ([GitHub](https://github.com/shruthimohan03))
- Bagiya Lakshmi ([GitHub](https://github.com/bagiyalakshmi))

---
