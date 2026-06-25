# FinTech Payments, Risk & Revenue Analytics Platform

## Business Scenario

This project simulates a UAE-based digital FinTech company offering digital wallet services, card payments, remittance transfers, customer onboarding, KYC verification, AML screening, credit bureau-based risk assessment, small consumer lending, collections monitoring, fraud detection, and revenue/margin analytics.

The company wants to build a centralized analytics platform to improve visibility across customer onboarding, payments, lending, risk, fraud, AML/KYC compliance, customer behavior, and product profitability.

The project will use a realistic synthetic dataset with 1,000 customers and high-volume transaction activity over a 3-year period. From this customer base, 10 case-study customers will be selected for detailed behavioral investigation, including 3 suspicious customers and 7 normal customers.

## Business Problem

The company has multiple operational and risk data sources, including customer profiles, identity documents, customer addresses, employment and income details, KYC verification, AML screening, credit bureau profiles, product applications, wallet accounts, merchants, wallet transactions, card payments, remittance transfers, loans, repayments, collections, fraud alerts, customer risk profiles, KYC review history, and revenue/cost/margin records.

Business, risk, compliance, finance, and product teams need a centralized analytics solution to answer key questions such as:

- How many customers are active, inactive, suspended, or closed?
- Which customer segments are using wallet, card, remittance, and lending products?
- Which onboarding channels are driving customer acquisition?
- Which customers have incomplete, expired, rejected, or high-risk KYC records?
- Which customers have high AML risk, PEP status, sanctions match indicators, or suspicious activity flags?
- What is the wallet and card payment success rate, failure rate, and transaction volume?
- Which payment channels, merchants, emirates, and products generate the highest activity?
- Which customers show suspicious wallet, card, or remittance behavior?
- Which transactions are flagged for fraud and what fraud patterns are most common?
- Which customers have higher AECB credit risk, debt burden, missed payments, or default probability?
- What is the loan approval, rejection, repayment, overdue, default, and collections trend?
- Which products generate the highest revenue, gross profit, and margin?
- What are the processing cost, partner fee, funding cost, service cost, and total cost by product?
- Which customer segments are most profitable?
- Which selected case-study customers require fraud, AML, or credit risk investigation?

## Project Objective

The objective is to build an end-to-end FinTech analytics platform using PostgreSQL, Supabase, SQL, Python, pandas, NumPy, scikit-learn, Power BI, DAX, Power Query, and machine learning.

The solution will support both portfolio-level analytics across 1,000 synthetic customers and detailed case-study investigation for selected customers.

The final solution will include:

- Professional PostgreSQL database design with relational tables and foreign keys
- Supabase cloud PostgreSQL implementation
- Synthetic FinTech data generation for 1,000 customers over a 3-year period
- High-volume wallet, card, remittance, lending, repayment, collections, fraud, AML, and revenue records
- SQL analytics queries for payments, onboarding, KYC, AML, fraud, lending, collections, and profitability
- Power BI dashboards for executive reporting, payments analytics, Fraud/AML/KYC monitoring, credit risk, collections, customer behavior, and revenue/margin analysis
- DAX measures for transaction value, payment success rate, fraud rate, AML risk, default rate, collection rate, revenue, cost, gross profit, and margin
- Power Query transformations for data cleaning, relationship preparation, and reporting model design
- Machine learning models for fraud detection, credit risk classification, customer segmentation, and revenue/transaction forecasting
- Case-study analysis for 10 selected customers, including 3 suspicious behavior patterns
- NLP and LLM-based insight summaries in later phases