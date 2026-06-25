Replace your old table_relationships.md with this revised version:

# Table Relationships - FinTech Payments, Risk & Revenue Analytics Platform

## Main Relationship Logic

This project uses a customer-centered FinTech data model. The `customers` table is the main master table. Most onboarding, compliance, payment, lending, fraud, risk, and revenue tables connect back to `customers` using `customer_id`.

The model supports both portfolio-level analytics across all customers and detailed investigation for selected case-study customers.

## Core Master Relationship

### customers to all customer-level tables

One customer can have related records across identity, address, employment, KYC, credit, risk, wallet, card, remittance, lending, fraud, and revenue tables.

Main relationship:

```text
customers.customer_id = related_table.customer_id
Customer-linked tables:

identity_documents
customer_addresses
employment_income
kyc_verification
credit_profiles
product_applications
document_verification
aml_screening
customer_risk_profiles
kyc_review_history
wallet_accounts
wallet_transactions
card_payments
remittance
loans
repayments
collections
fraud_alerts
revenue_cost_margin
Use case:

Build a full customer 360-degree profile.
Analyze onboarding, KYC, AML, credit risk, transaction behavior, fraud alerts, and revenue performance by customer.
Onboarding, Identity, and KYC Relationships
customers to identity_documents
One customer can have multiple identity documents.

Relationship:

customers.customer_id = identity_documents.customer_id
Use case:

Store Emirates ID, passport, visa, and residency details.
Track document status, expiry, and verification status.
customers to customer_addresses
One customer can have multiple addresses.

Relationship:

customers.customer_id = customer_addresses.customer_id
Use case:

Store UAE residence, home country, mailing, or office address.
Analyze customer location by country, emirate, city, or area.
customers to employment_income
One customer can have employment and income records.

Relationship:

customers.customer_id = employment_income.customer_id
Use case:

Analyze employment status, monthly income, liabilities, source of funds, and source of wealth.
customers to kyc_verification
One customer can have KYC verification records.

Relationship:

customers.customer_id = kyc_verification.customer_id
Use case:

Track KYC status, verification method, biometric checks, selfie match, and overall KYC risk score.
identity_documents to document_verification
One identity document can have document verification checks.

Relationship:

identity_documents.document_id = document_verification.document_id
Also:

customers.customer_id = document_verification.customer_id
Use case:

Validate document authenticity, name match, date of birth match, expiry status, and verification score.
customers to aml_screening
One customer can have AML screening records.

Relationship:

customers.customer_id = aml_screening.customer_id
Use case:

Monitor AML risk score, sanctions match, PEP status, adverse media, high-risk country flag, and suspicious activity flag.
customers to kyc_review_history
One customer can have multiple KYC review history records.

Relationship:

customers.customer_id = kyc_review_history.customer_id
Use case:

Track KYC review decisions, previous vs new KYC status, reviewer comments, and audit history.
Credit and Product Application Relationships
customers to credit_profiles
One customer can have credit profile records.

Relationship:

customers.customer_id = credit_profiles.customer_id
Use case:

Analyze AECB score, credit score band, debt burden ratio, missed payments, credit history, and credit risk category.
customers to product_applications
One customer can apply for multiple products.

Relationship:

customers.customer_id = product_applications.customer_id
Use case:

Track applications for wallet, card, remittance, loan, or account products.
Analyze approval, rejection, requested amount, approved amount, and decision date.
product_applications to loans
A loan may be linked to a product application.

Relationship:

product_applications.application_id = loans.application_id
Use case:

Connect loan approval or rejection to the original customer application.
Wallet, Merchant, and Payment Relationships
customers to wallet_accounts
One customer can have one or more wallet accounts.

Relationship:

customers.customer_id = wallet_accounts.customer_id
Use case:

Track wallet status, opening date, current balance, wallet tier, and transaction limits.
wallet_accounts to wallet_transactions
One wallet account can have many wallet transactions.

Relationship:

wallet_accounts.wallet_id = wallet_transactions.wallet_id
Also:

customers.customer_id = wallet_transactions.customer_id
Use case:

Analyze wallet top-ups, payments, transfers, withdrawals, refunds, success/failure rate, channel, device, location, and transaction amount.
merchants to wallet_transactions
One merchant can have many wallet transactions.

Relationship:

merchants.merchant_id = wallet_transactions.merchant_id
Use case:

Analyze wallet payment activity by merchant, category, and emirate.
merchants to card_payments
One merchant can have many card payment transactions.

Relationship:

merchants.merchant_id = card_payments.merchant_id
Use case:

Analyze card payment activity by merchant, category, and network.
customers to card_payments
One customer can have many card payment records.

Relationship:

customers.customer_id = card_payments.customer_id
Use case:

Analyze debit, credit, and prepaid card payments, approval rate, decline rate, reversal rate, and interchange fee revenue.
customers to remittance
One customer can have many remittance transfers.

Relationship:

customers.customer_id = remittance.customer_id
Use case:

Analyze destination country, transfer amount, exchange rate, transfer fee, transfer status, and remittance channel.
Lending, Repayment, and Collections Relationships
customers to loans
One customer can have multiple loans.

Relationship:

customers.customer_id = loans.customer_id
Use case:

Analyze loan applications, approved amount, loan status, interest rate, tenure, credit score, default risk score, disbursement date, and maturity date.
loans to repayments
One loan can have many repayment records.

Relationship:

loans.loan_id = repayments.loan_id
Also:

customers.customer_id = repayments.customer_id
Use case:

Track due date, payment date, due amount, paid amount, repayment status, and days past due.
loans to collections
One loan can have many collections follow-up records.

Relationship:

loans.loan_id = collections.loan_id
Also:

customers.customer_id = collections.customer_id
Use case:

Track collection stage, outstanding amount, action taken, and recovery status.
Fraud, Risk, and Revenue Relationships
wallet_transactions to fraud_alerts
One wallet transaction can have zero or more fraud alerts.

Relationship:

wallet_transactions.transaction_id = fraud_alerts.transaction_id
Also:

customers.customer_id = fraud_alerts.customer_id
Use case:

Identify suspicious wallet transactions, fraud score, alert status, and investigation result.
card_payments to fraud_alerts
One card payment can have zero or more fraud alerts.

Relationship:

card_payments.card_payment_id = fraud_alerts.card_payment_id
Also:

customers.customer_id = fraud_alerts.customer_id
Use case:

Identify suspicious card transactions, device/location risk, high-value payments, and confirmed fraud cases.
customers to customer_risk_profiles
One customer can have combined risk profile records.

Relationship:

customers.customer_id = customer_risk_profiles.customer_id
Use case:

Combine onboarding risk, transaction risk, credit risk, fraud risk, AML risk, and final risk score.
customers to revenue_cost_margin
One customer can have many revenue and margin records.

Relationship:

customers.customer_id = revenue_cost_margin.customer_id
Use case:

Analyze revenue, processing cost, partner fee, funding cost, service cost, total cost, gross profit, and margin by customer.
wallet_transactions to revenue_cost_margin
Wallet transaction revenue may link to a wallet transaction.

Relationship:

wallet_transactions.transaction_id = revenue_cost_margin.transaction_id
Use case:

Analyze wallet transaction revenue and cost.
card_payments to revenue_cost_margin
Card payment revenue may link to a card payment.

Relationship:

card_payments.card_payment_id = revenue_cost_margin.card_payment_id
Use case:

Analyze card interchange fee revenue, processing cost, and margin.
remittance to revenue_cost_margin
Remittance revenue may link to a remittance transfer.

Relationship:

remittance.remittance_id = revenue_cost_margin.remittance_id
Use case:

Analyze remittance transfer fee revenue, partner fee, and margin.
loans to revenue_cost_margin
Loan revenue may link to a loan.

Relationship:

loans.loan_id = revenue_cost_margin.loan_id
Use case:

Analyze lending interest revenue, funding cost, service cost, and margin.
High-Level ERD Summary
customers
  ├── identity_documents
  │     └── document_verification
  ├── customer_addresses
  ├── employment_income
  ├── kyc_verification
  ├── aml_screening
  ├── credit_profiles
  ├── product_applications
  │     └── loans
  │           ├── repayments
  │           └── collections
  ├── customer_risk_profiles
  ├── kyc_review_history
  ├── wallet_accounts
  │     └── wallet_transactions
  │           ├── fraud_alerts
  │           └── revenue_cost_margin
  ├── card_payments
  │     ├── fraud_alerts
  │     └── revenue_cost_margin
  ├── remittance
  │     └── revenue_cost_margin
  └── revenue_cost_margin

merchants
  ├── wallet_transactions
  └── card_payments
Interview Explanation
This project follows a customer-centered FinTech data model where the customers table acts as the main master table. Customer onboarding, KYC, AML, credit profile, product application, payment activity, lending activity, fraud alerts, risk scoring, and revenue records connect back to the customer through customer_id.

The model supports a full customer 360-degree view and enables analytics across onboarding, digital wallet usage, card payments, remittance, credit risk, fraud detection, AML/KYC compliance, collections, revenue, cost, gross profit, and margin.

The database also supports Power BI reporting and SQL analytics through clear foreign key relationships between customers, merchants, wallets, transactions, loans, fraud alerts, and revenue records.

## Device, IP, and Location Session Relationships

### customers to customer_device_sessions

One customer can have many device sessions.

Relationship:

```text
customers.customer_id = customer_device_sessions.customer_id
Use case:

Track customer login sessions.
Analyze device changes, IP address, VPN/proxy use, and location behavior.
Detect unusual login patterns before wallet, card, or remittance transactions.
customer_device_sessions to wallet_transactions
One device session can be linked to many wallet transactions.

Relationship:

customer_device_sessions.device_session_id = wallet_transactions.device_session_id
Use case:

Detect wallet transactions from unusual devices, IP addresses, or locations.
customer_device_sessions to card_payments
One device session can be linked to many card payments.

Relationship:

customer_device_sessions.device_session_id = card_payments.device_session_id
Use case:

Detect card payments from new devices, risky IP addresses, VPN/proxy sessions, or unusual locations.
customer_device_sessions to remittance
One device session can be linked to many remittance transfers.

Relationship:

customer_device_sessions.device_session_id = remittance.device_session_id
Use case:

Detect remittance transfers from unusual device, IP, or location sessions.

Also update the high-level ERD summary to include:

```text
customers
  ├── customer_device_sessions
  │     ├── wallet_transactions
  │     ├── card_payments
  │     └── remittance


  
