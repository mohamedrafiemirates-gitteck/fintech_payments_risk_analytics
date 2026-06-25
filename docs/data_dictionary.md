# Data Dictionary - FinTech Payments, Risk & Revenue Analytics Platform

## 1. customers

Stores core customer master profile information.

| Column Name | Description |
|---|---|
| customer_id | Unique customer identifier |
| full_name | Customer full name as per official document |
| gender | Customer gender |
| date_of_birth | Customer date of birth |
| nationality | Customer nationality |
| country_of_residence | Customer current country of residence |
| mobile_number | Customer registered mobile number |
| email | Customer registered email address |
| marital_status | Customer marital status |
| customer_segment | Retail, salary, student, SME, premium |
| signup_date | Customer onboarding or registration date |
| onboarding_channel | Mobile app, web, branch, agent |
| customer_status | Active, inactive, suspended, closed |
| created_at | Record creation timestamp |

## 2. identity_documents

Stores Emirates ID, passport, visa, and residency document details.

| Column Name | Description |
|---|---|
| document_id | Unique document record identifier |
| customer_id | Linked customer identifier |
| document_type | Emirates ID, passport, visa |
| document_number | Document number |
| issue_date | Document issue date |
| expiry_date | Document expiry date |
| issued_country | Country that issued the document |
| residency_status | UAE resident, citizen, visitor, expired visa, under renewal |
| document_status | Valid, expired, cancelled |
| verification_status | Verified, pending, rejected |
| created_at | Record creation timestamp |

## 3. customer_addresses

Stores UAE and home country address details.

| Column Name | Description |
|---|---|
| address_id | Unique address identifier |
| customer_id | Linked customer identifier |
| address_type | UAE residence, home country, mailing, office |
| country | Address country |
| emirate | UAE emirate, if applicable |
| city | City |
| area | Area or district |
| street_address | Detailed street address |
| building_name | Building or tower name |
| flat_or_villa_no | Flat, villa, or unit number |
| po_box | PO box number |
| postal_code | Postal or ZIP code |
| address_status | Active, inactive, old |
| created_at | Record creation timestamp |

## 4. employment_income

Stores customer employment, salary, income, and source-of-funds information.

| Column Name | Description |
|---|---|
| employment_id | Unique employment record identifier |
| customer_id | Linked customer identifier |
| employment_status | Employed, self-employed, student, unemployed |
| employer_name | Customer employer name |
| job_title | Customer job title |
| industry | Employment industry |
| monthly_income | Monthly income or salary |
| salary_transfer_bank | Bank where salary is transferred |
| length_of_employment_months | Employment length in months |
| source_of_funds | Salary, business income, investments, remittance |
| source_of_wealth | Savings, business ownership, inheritance, investments |
| monthly_liabilities | Monthly financial obligations |
| created_at | Record creation timestamp |

## 5. kyc_verification

Stores customer KYC verification status and risk score.

| Column Name | Description |
|---|---|
| kyc_id | Unique KYC record identifier |
| customer_id | Linked customer identifier |
| kyc_status | Approved, pending, rejected, expired |
| kyc_level | Basic, standard, enhanced due diligence |
| verification_method | Digital, manual, branch, third-party provider |
| verification_date | KYC verification date |
| next_review_date | Next KYC review date |
| document_verification_score | Document verification score |
| biometric_verification_status | Passed, failed, pending |
| selfie_match_score | Selfie or face-match score |
| overall_kyc_risk_score | Overall KYC risk score |
| kyc_remarks | KYC review notes |
| created_at | Record creation timestamp |

## 6. credit_profiles

Stores Al Etihad Credit Bureau and credit risk information.

| Column Name | Description |
|---|---|
| credit_profile_id | Unique credit profile identifier |
| customer_id | Linked customer identifier |
| aecb_score | Al Etihad Credit Bureau score |
| credit_score_band | Excellent, good, fair, poor, very poor |
| credit_report_date | Credit report date |
| total_active_loans | Total active loans |
| total_credit_cards | Total active credit cards |
| total_outstanding_balance | Total outstanding credit balance |
| monthly_installment_amount | Total monthly installment amount |
| debt_burden_ratio | Debt burden ratio percentage |
| missed_payments_count | Number of missed payments |
| days_past_due_max | Maximum days past due |
| credit_history_months | Credit history age in months |
| credit_risk_category | Low, medium, high |
| created_at | Record creation timestamp |

## 7. product_applications

Stores customer applications for wallet, card, loan, account, or other products.

| Column Name | Description |
|---|---|
| application_id | Unique application identifier |
| customer_id | Linked customer identifier |
| product_type | Wallet, card, remittance, loan, account |
| application_date | Application submission date |
| application_channel | Mobile app, web, branch, agent |
| application_status | Submitted, pending, approved, rejected |
| requested_amount | Requested loan or credit amount |
| approved_amount | Approved loan amount |
| approved_limit | Approved card or wallet limit |
| rejection_reason | Reason for rejection |
| decision_date | Approval or rejection date |
| created_at | Record creation timestamp |

## 8. document_verification

Stores detailed document verification checks.

| Column Name | Description |
|---|---|
| document_verification_id | Unique document verification identifier |
| document_id | Linked identity document identifier |
| customer_id | Linked customer identifier |
| verification_date | Document verification date |
| verification_provider | Verification provider or system |
| document_authenticity_status | Authentic, suspicious, rejected |
| name_match_status | Name match result |
| date_of_birth_match_status | Date of birth match result |
| expiry_check_status | Valid, expired, near expiry |
| verification_score | Document verification score |
| verification_status | Verified, failed, pending |
| created_at | Record creation timestamp |

## 9. aml_screening

Stores AML screening, sanctions, PEP, and suspicious activity indicators.

| Column Name | Description |
|---|---|
| aml_screening_id | Unique AML screening identifier |
| customer_id | Linked customer identifier |
| screening_date | AML screening date |
| aml_risk_score | AML risk score |
| aml_risk_category | Low, medium, high |
| sanctions_match_status | Sanctions match result |
| pep_status | Politically exposed person status |
| adverse_media_status | Adverse media screening result |
| high_risk_country_flag | High-risk country indicator |
| suspicious_activity_flag | Suspicious activity indicator |
| screening_status | Cleared, open, under review, escalated |
| created_at | Record creation timestamp |

## 10. customer_risk_profiles

Stores combined customer risk scores across onboarding, transaction, credit, fraud, and AML areas.

| Column Name | Description |
|---|---|
| risk_profile_id | Unique risk profile identifier |
| customer_id | Linked customer identifier |
| risk_assessment_date | Risk assessment date |
| customer_risk_category | Low, medium, high |
| onboarding_risk_score | Onboarding risk score |
| transaction_risk_score | Transaction behavior risk score |
| credit_risk_score | Credit risk score |
| fraud_risk_score | Fraud risk score |
| aml_risk_score | AML risk score |
| final_risk_score | Final combined customer risk score |
| risk_reason | Reason for risk category |
| review_status | Open, reviewed, escalated, closed |
| created_at | Record creation timestamp |

## 11. kyc_review_history

Stores KYC review audit history.

| Column Name | Description |
|---|---|
| review_id | Unique KYC review identifier |
| customer_id | Linked customer identifier |
| review_date | Review date |
| review_type | Initial review, periodic review, enhanced review |
| previous_kyc_status | Previous KYC status |
| new_kyc_status | Updated KYC status |
| reviewer_name | Reviewer or analyst name |
| review_decision | Approved, rejected, escalated |
| review_comments | Review comments |
| created_at | Record creation timestamp |

## 12. wallet_accounts

Stores customer digital wallet account details.

| Column Name | Description |
|---|---|
| wallet_id | Unique wallet identifier |
| customer_id | Linked customer identifier |
| wallet_status | Active, inactive, suspended, closed |
| opening_date | Wallet opening date |
| current_balance | Current wallet balance |
| wallet_tier | Basic, standard, premium |
| daily_transaction_limit | Daily transaction limit |
| monthly_transaction_limit | Monthly transaction limit |
| created_at | Record creation timestamp |

## 13. merchants

Stores merchant or business partner information.

| Column Name | Description |
|---|---|
| merchant_id | Unique merchant identifier |
| merchant_name | Merchant business name |
| merchant_category | Retail, grocery, travel, electronics, services |
| emirate | Merchant emirate |
| onboarding_date | Merchant onboarding date |
| merchant_status | Active, inactive, suspended |
| created_at | Record creation timestamp |

## 14. wallet_transactions

Stores wallet transaction activity.

| Column Name | Description |
|---|---|
| transaction_id | Unique wallet transaction identifier |
| wallet_id | Linked wallet identifier |
| customer_id | Linked customer identifier |
| transaction_date | Transaction date and time |
| transaction_type | Top-up, payment, transfer, withdrawal, refund |
| channel | Mobile app, web, POS, API |
| merchant_id | Linked merchant identifier |
| amount | Transaction amount |
| currency | Transaction currency |
| transaction_status | Success, failed, pending, reversed |
| failure_reason | Reason for failed transaction |
| device_id | Customer device identifier |
| location_emirate | Emirate where transaction occurred |
| created_at | Record creation timestamp |
| device_session_id | Linked customer device session identifier |


## 15. card_payments

Stores card payment activity.

| Column Name | Description |
|---|---|
| card_payment_id | Unique card payment identifier |
| customer_id | Linked customer identifier |
| transaction_date | Card payment date and time |
| card_type | Debit, credit, prepaid |
| card_network | Visa, Mastercard, local network |
| merchant_id | Linked merchant identifier |
| amount | Payment amount |
| currency | Payment currency |
| payment_status | Approved, declined, reversed |
| decline_reason | Reason for declined payment |
| interchange_fee | Card interchange fee revenue |
| created_at | Record creation timestamp |
| device_session_id | Linked customer device session identifier |

## 16. remittance

Stores remittance transfer activity.

| Column Name | Description |
|---|---|
| remittance_id | Unique remittance identifier |
| customer_id | Linked customer identifier |
| transfer_date | Remittance transfer date and time |
| destination_country | Destination country |
| transfer_amount | Amount transferred |
| exchange_rate | Applied exchange rate |
| transfer_fee | Remittance fee |
| transfer_status | Completed, failed, pending |
| channel | Mobile app, branch, partner |
| created_at | Record creation timestamp |
| device_session_id | Linked customer device session identifier |

## 17. loans

Stores consumer loan application and loan account details.

| Column Name | Description |
|---|---|
| loan_id | Unique loan identifier |
| customer_id | Linked customer identifier |
| application_id | Linked product application identifier |
| application_date | Loan application date |
| loan_amount | Requested loan amount |
| approved_amount | Approved loan amount |
| loan_status | Approved, rejected, active, closed, defaulted |
| interest_rate | Loan interest rate |
| tenure_months | Loan duration in months |
| credit_score | Customer credit score |
| default_risk_score | Default risk score |
| disbursement_date | Loan disbursement date |
| maturity_date | Loan maturity date |
| created_at | Record creation timestamp |

## 18. repayments

Stores loan repayment schedule and payment behavior.

| Column Name | Description |
|---|---|
| repayment_id | Unique repayment identifier |
| loan_id | Linked loan identifier |
| customer_id | Linked customer identifier |
| due_date | Repayment due date |
| payment_date | Actual payment date |
| due_amount | Due amount |
| paid_amount | Paid amount |
| repayment_status | Paid, late, missed, partial |
| days_past_due | Number of overdue days |
| created_at | Record creation timestamp |

## 19. collections

Stores collections follow-up activity for overdue loans.

| Column Name | Description |
|---|---|
| collection_id | Unique collection record identifier |
| loan_id | Linked loan identifier |
| customer_id | Linked customer identifier |
| collection_date | Collection follow-up date |
| collection_stage | Reminder, soft collection, legal, write-off |
| outstanding_amount | Outstanding amount |
| action_taken | SMS, call, email, legal notice |
| recovery_status | Recovered, pending, escalated, written off |
| created_at | Record creation timestamp |

## 20. fraud_alerts

Stores fraud monitoring alerts for wallet and card activity.

| Column Name | Description |
|---|---|
| fraud_alert_id | Unique fraud alert identifier |
| customer_id | Linked customer identifier |
| transaction_id | Linked wallet transaction identifier |
| card_payment_id | Linked card payment identifier |
| alert_date | Fraud alert date and time |
| fraud_type | Velocity, high amount, device mismatch, unusual location |
| fraud_score | Numeric fraud risk score |
| alert_status | ["Open", "Reviewed", "Closed", "Escalated"]|
| investigation_result | "Under Review", "False Positive", "Confirmed Fraud", "No Issue Found" |
| created_at | Record creation timestamp |

## 21. revenue_cost_margin

Stores revenue, cost, gross profit, and margin by product and activity.

| Column Name | Description |
|---|---|
| revenue_id | Unique revenue record identifier |
| revenue_date | Revenue date |
| product_type | Wallet, card, remittance, lending |
| customer_id | Linked customer identifier |
| transaction_id | Linked wallet transaction identifier |
| card_payment_id | Linked card payment identifier |
| remittance_id | Linked remittance identifier |
| loan_id | Linked loan identifier |
| revenue_amount | Revenue amount |
| processing_cost | Transaction or payment processing cost |
| partner_fee | External partner or provider fee |
| funding_cost | Cost of funds, mainly for lending |
| service_cost | Customer support, KYC, AML, fraud, or operational service cost |
| total_cost | Total cost across processing, partner, funding, and service costs |
| gross_profit | Revenue amount minus total cost |
| gross_margin_percentage | Gross profit percentage |
| created_at | Record creation timestamp |


## 22. customer_device_sessions

Stores customer device, IP, network, and location session details for login and transaction risk monitoring.

| Column Name | Description |
|---|---|
| device_session_id | Unique device session identifier |
| customer_id | Linked customer identifier |
| device_id | Unique customer device identifier |
| device_type | Mobile, desktop, tablet |
| os_name | Operating system name |
| browser_name | Browser or app browser name |
| app_version | Mobile app version |
| ip_address | IP address used during session |
| ip_country | Country detected from IP |
| ip_city | City detected from IP |
| location_emirate | UAE emirate detected from location |
| latitude | Latitude coordinate |
| longitude | Longitude coordinate |
| location_address | Approximate location address |
| gps_accuracy_meters | GPS accuracy in meters |
| network_type | WiFi, mobile data, broadband |
| is_vpn | VPN usage indicator |
| is_proxy | Proxy usage indicator |
| login_timestamp | Login or session timestamp |
| session_status | Active, expired, terminated, suspicious |
| created_at | Record creation timestamp |

