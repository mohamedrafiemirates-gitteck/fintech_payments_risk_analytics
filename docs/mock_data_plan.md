# Mock Data Generation Plan

## Project Data Scope

This project will use a realistic synthetic FinTech dataset with 1,000 customers and high-volume transaction activity over a 3-year period.

The project will also include 10 selected case-study customers for detailed behavioral analysis, including 3 suspicious customers and 7 normal customers.

## Customer Volume

- Total synthetic customers: 1,000
- Selected case-study customers: 10
- Suspicious case-study customers: 3
- Normal case-study customers: 7

## Data Period

- Transaction history: 3 years
- Suggested period: January 2024 to December 2026

## Suggested Data Volume

- Customers: 1,000
- Identity documents: 2,000 to 3,000
- Customer addresses: 1,000 to 2,000
- Employment income records: 1,000
- KYC verification records: 1,000
- Credit profiles: 1,000
- Product applications: 2,000 to 4,000
- Wallet accounts: 900 to 1,000
- Merchants: 300 to 500
- Wallet transactions: 100,000 to 150,000
- Card payments: 50,000 to 80,000
- Remittance records: 10,000 to 20,000
- Loans: 1,500 to 3,000
- Repayments: 10,000 to 30,000
- Collections: 2,000 to 5,000
- Fraud alerts: 2,000 to 5,000
- AML screening records: 1,000
- Customer risk profiles: 1,000
- Document verification records: 2,000 to 3,000
- KYC review history: 1,000 to 3,000
- Revenue/cost/margin records: linked to transaction activity

## Case-Study Customer Design

The dataset will include 10 selected customers for detailed investigation and storytelling.

### Suspicious Customer 1 - Structuring Behavior

This customer will perform many small wallet transfers within short time windows to simulate potential AML structuring behavior.

Pattern examples:

- High number of wallet transfers
- Repeated transactions below monitoring threshold
- Multiple transactions per day
- Higher AML risk score

### Suspicious Customer 2 - Device and Location Risk

This customer will show unusual device and location behavior.

Pattern examples:

- Transactions from multiple emirates within short periods
- Device ID changes
- Failed payment attempts
- High fraud risk score

### Suspicious Customer 3 - Remittance and High-Risk Country Pattern

This customer will show higher-risk remittance behavior.

Pattern examples:

- Frequent remittance transactions
- Transfers to high-risk countries
- Higher transfer amounts
- AML alerts
- Enhanced due diligence requirement

## Normal Customer Patterns

The other selected case-study customers will show normal FinTech usage behavior.

Pattern examples:

- Salary top-ups
- Grocery payments
- Retail purchases
- Utility bill payments
- Occasional remittance
- Low fraud and AML risk scores

## Business Purpose

This dataset will support:

- Customer onboarding analytics
- KYC monitoring
- AML screening
- Wallet and card payment analytics
- Remittance analytics
- Credit risk analytics
- Collections monitoring
- Fraud detection
- Revenue, cost, and margin reporting
- Customer segmentation
- ML model development
- Power BI executive dashboarding