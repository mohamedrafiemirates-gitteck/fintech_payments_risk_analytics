mock_data_generation_strategy.md
Paste this content:

# Mock Data Generation Strategy

## Objective

The objective of this step is to define how synthetic FinTech data will be generated for the project.

The dataset must support:

- SQL analytics
- Power BI dashboards
- Fraud, AML, and KYC analysis
- Credit risk analysis
- Customer segmentation
- Revenue and margin reporting
- Machine learning models

## Data Generation Approach

The project will generate synthetic data using Python.

The data will be generated in a controlled order so that foreign key relationships remain valid.

## Generation Order

Data will be generated in this order:

1. customers
2. identity_documents
3. customer_addresses
4. employment_income
5. kyc_verification
6. credit_profiles
7. product_applications
8. document_verification
9. aml_screening
10. customer_risk_profiles
11. kyc_review_history
12. wallet_accounts
13. merchants
14. wallet_transactions
15. card_payments
16. remittance
17. loans
18. repayments
19. collections
20. fraud_alerts
21. revenue_cost_margin

## Customer Design

The dataset will contain 1,000 synthetic customers.

From these 1,000 customers, 10 customers will be selected as case-study customers.

The case-study customers will include:

- 7 normal customers
- 3 suspicious customers

## Suspicious Customer Design

### Suspicious Customer 1 - Structuring Pattern

This customer will perform many small wallet transfers and payments within short time windows.

Pattern:
- High transaction frequency
- Repeated amounts below monitoring thresholds
- Multiple transactions per day
- Higher AML risk score

### Suspicious Customer 2 - Device and Location Pattern

This customer will show unusual digital behavior.

Pattern:
- Frequent device ID changes
- Transactions from different emirates in short periods
- Failed payment attempts
- Higher fraud risk score

### Suspicious Customer 3 - Remittance Risk Pattern

This customer will show high-risk remittance behavior.

Pattern:
- Frequent remittance transactions
- Transfers to high-risk countries
- Higher transfer amounts
- AML alerts and enhanced due diligence

## Normal Customer Design

Normal customers will show realistic financial behavior.

Pattern:
- Salary top-ups
- Grocery payments
- Retail purchases
- Utility payments
- Occasional card usage
- Occasional remittance
- Low fraud risk score
- Low AML risk score

## Transaction Period

The dataset will cover a 3-year period.

Suggested date range:

```text
2024-01-01 to 2026-12-31
Data Volume Targets
Suggested volume:

Table	Approximate Records
customers	1,000
identity_documents	2,000 - 3,000
customer_addresses	1,000 - 2,000
employment_income	1,000
kyc_verification	1,000
credit_profiles	1,000
product_applications	2,000 - 4,000
document_verification	2,000 - 3,000
aml_screening	1,000
customer_risk_profiles	1,000
kyc_review_history	1,000 - 3,000
wallet_accounts	900 - 1,000
merchants	300 - 500
wallet_transactions	100,000 - 150,000
card_payments	50,000 - 80,000
remittance	10,000 - 20,000
loans	1,500 - 3,000
repayments	10,000 - 30,000
collections	2,000 - 5,000
fraud_alerts	2,000 - 5,000
revenue_cost_margin	Linked to transactions, remittance, card, and lending activity
Output Format
Python will generate CSV files first.

The CSV files will be stored in the data/ folder.

Example:

data/customers.csv
data/wallet_transactions.csv
data/card_payments.csv
data/fraud_alerts.csv
Loading Approach
After CSV generation, the data will be loaded into Supabase PostgreSQL.

Possible loading methods:

Supabase Table Editor CSV upload
Python loading script using PostgreSQL connection
SQL copy method
The preferred learning approach is:

Generate CSV files
Inspect CSV files manually
Upload smaller tables first
Validate record counts
Upload high-volume tables
Run SQL validation queries
Validation Checks
After loading data, validation queries will check:

Row count by table
Missing customer IDs
Foreign key consistency
Date range correctness
Duplicate primary keys
Transaction status distribution
Fraud alert distribution
AML risk distribution
Revenue and margin calculation correctness