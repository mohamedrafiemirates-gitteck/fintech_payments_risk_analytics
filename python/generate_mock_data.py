import random
from datetime import datetime, timedelta
from pathlib import Path
import numpy as np
import pandas as pd

# Reproducibility
random.seed(42)
np.random.seed(42)

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Data period
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 12, 31)

# Master reference lists
UAE_EMIRATES = [
    "Dubai",
    "Sharjah",
    "Abu Dhabi",
    "Ajman",
    "Ras Al Khaimah",
    "Fujairah",
    "Umm Al Quwain",
]

NATIONALITIES = [
    "India",
    "Pakistan",
    "Philippines",
    "Bangladesh",
    "Sri Lanka",
    "Nepal",
    "Egypt",
    "Jordan",
    "United Arab Emirates",
    "United Kingdom",
]

CUSTOMER_SEGMENTS = [
    "Retail",
    "Salary",
    "Student",
    "SME",
    "Premium",
]

ONBOARDING_CHANNELS = [
    "Mobile App",
    "Web",
    "Branch",
    "Agent",
]

CUSTOMER_STATUSES = [
    "Active",
    "Inactive",
    "Suspended",
    "Closed",
]

MARITAL_STATUSES = [
    "Single",
    "Married",
    "Divorced",
]

GENDERS = [
    "Male",
    "Female",
]

def random_date(start_date, end_date):
    """Return a random datetime between start_date and end_date."""
    total_days = (end_date - start_date).days
    random_days = random.randint(0, total_days)
    return start_date + timedelta(days=random_days)
    
def generate_customers(n_customers=1000):
    customers = []

    for i in range(1, n_customers + 1):
        customer_id = f"CUST{i:05d}"
        gender = random.choice(GENDERS)

        first_names_male = ["Mohamed", "Ahmed", "Ali", "Omar", "Rafi", "Bilal", "Hassan", "Khalid"]
        first_names_female = ["Aisha", "Sara", "Fatima", "Mariam", "Noura", "Priya", "Anjali", "Grace"]
        last_names = ["Khan", "Ali", "Rafi", "Rahman", "Thomas", "Fernandez", "Hussain", "Nair", "Ahmed"]

        first_name = random.choice(first_names_male if gender == "Male" else first_names_female)
        last_name = random.choice(last_names)

        date_of_birth = random_date(datetime(1970, 1, 1), datetime(2005, 12, 31)).date()
        signup_date = random_date(START_DATE, END_DATE).date()

        customers.append(
            {
                "customer_id": customer_id,
                "full_name": f"{first_name} {last_name}",
                "gender": gender,
                "date_of_birth": date_of_birth,
                "nationality": random.choice(NATIONALITIES),
                "country_of_residence": "United Arab Emirates",
                "mobile_number": f"+9715{random.randint(10000000, 99999999)}",
                "email": f"{first_name.lower()}.{last_name.lower()}{i}@example.com",
                "marital_status": random.choice(MARITAL_STATUSES),
                "customer_segment": random.choice(CUSTOMER_SEGMENTS),
                "signup_date": signup_date,
                "onboarding_channel": random.choice(ONBOARDING_CHANNELS),
                "customer_status": random.choices(
                    CUSTOMER_STATUSES,
                    weights=[0.82, 0.10, 0.05, 0.03],
                    k=1,
                )[0],
                "is_case_study_customer": i <= 10,
                "case_study_type": "Selected" if i <= 10 else "Not Selected",
            }
        )
    return pd.DataFrame(customers)

def generate_identity_documents(customers_df):
    documents = []

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]
        nationality = customer["nationality"]

        # Emirates ID
        emirates_issue_date = random_date(datetime(2020, 1, 1), datetime(2025, 12, 31)).date()
        emirates_expiry_date = emirates_issue_date + timedelta(days=random.randint(365, 365 * 5))

        documents.append(
            {
                "document_id": f"DOC{len(documents) + 1:06d}",
                "customer_id": customer_id,
                "document_type": "Emirates ID",
                "document_number": f"784-{random.randint(1900, 2020)}-{random.randint(1000000, 9999999)}-{random.randint(1, 9)}",
                "issue_date": emirates_issue_date,
                "expiry_date": emirates_expiry_date,
                "issued_country": "United Arab Emirates",
                "residency_status": "UAE Citizen" if nationality == "United Arab Emirates" else "UAE Resident",
                "document_status": "Valid" if emirates_expiry_date >= datetime.today().date() else "Expired",
                "verification_status": random.choices(
                    ["Verified", "Pending", "Rejected"],
                    weights=[0.88, 0.10, 0.02],
                    k=1,
                )[0],
            }
        )
        # Passport
        passport_issue_date = random_date(datetime(2016, 1, 1), datetime(2025, 12, 31)).date()
        passport_expiry_date = passport_issue_date + timedelta(days=365 * 10)

        documents.append(
            {
                "document_id": f"DOC{len(documents) + 1:06d}",
                "customer_id": customer_id,
                "document_type": "Passport",
                "document_number": f"P{random.randint(1000000, 9999999)}",
                "issue_date": passport_issue_date,
                "expiry_date": passport_expiry_date,
                "issued_country": nationality,
                "residency_status": "UAE Citizen" if nationality == "United Arab Emirates" else "UAE Resident",
                "document_status": "Valid" if passport_expiry_date >= datetime.today().date() else "Expired",
                "verification_status": random.choices(
                    ["Verified", "Pending", "Rejected"],
                    weights=[0.90, 0.08, 0.02],
                    k=1,
                )[0],
            }
        )
    return pd.DataFrame(documents)     

def generate_customer_addresses(customers_df):
    addresses = []
    areas_by_emirate = {
        "Dubai": ["Deira", "Bur Dubai", "Business Bay", "Jumeirah", "Dubai Marina"],
        "Sharjah": ["Al Nahda", "Al Majaz", "Muweilah", "Rolla", "Al Taawun"],
        "Abu Dhabi": ["Mussafah", "Khalifa City", "Al Reem Island", "Corniche", "Madinat Zayed"],
        "Ajman": ["Al Nuaimiya", "Al Rashidiya", "Al Jurf", "Ajman Corniche"],
        "Ras Al Khaimah": ["Al Nakheel", "Al Hamra", "Khuzam", "Al Dhait"],
        "Fujairah": ["Fujairah City", "Dibba", "Al Faseel", "Madhab"],
        "Umm Al Quwain": ["Al Salamah", "Falaj Al Mualla", "Al Raas", "Old Town"],
    }

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]
        emirate = random.choice(UAE_EMIRATES)
        area = random.choice(areas_by_emirate[emirate])

        addresses.append(
            {
                "address_id": f"ADDR{len(addresses) + 1:06d}",
                "customer_id": customer_id,
                "address_type": "UAE Residence",
                "country": "United Arab Emirates",
                "emirate": emirate,
                "city": emirate,
                "area": area,
                "street_address": f"{random.randint(1, 99)} {area} Street",
                "building_name": f"Building {random.randint(1, 200)}",
                "flat_or_villa_no": f"{random.randint(101, 2505)}",
                "po_box": f"{random.randint(10000, 99999)}",
                "postal_code": "",
                "address_status": "Active",
            }
        )

        if customer["nationality"] != "United Arab Emirates":
            addresses.append(
                {
                    "address_id": f"ADDR{len(addresses) + 1:06d}",
                    "customer_id": customer_id,
                    "address_type": "Home Country",
                    "country": customer["nationality"],
                    "emirate": "",
                    "city": random.choice(["Capital City", "Metro City", "Central District", "Old Town"]),
                    "area": random.choice(["Main Area", "Market Area", "Residential Zone", "Town Center"]),
                    "street_address": f"House {random.randint(1, 500)}, Street {random.randint(1, 50)}",
                    "building_name": "",
                    "flat_or_villa_no": "",
                    "po_box": "",
                    "postal_code": f"{random.randint(100000, 999999)}",
                    "address_status": "Active",
                }
            )

    return pd.DataFrame(addresses)  

def generate_employment_income(customers_df):
    employment_records = []

    employment_statuses = ["Employed", "Self-Employed", "Student", "Unemployed"]
    industries = [
        "Banking",
        "Retail",
        "Construction",
        "Healthcare",
        "Education",
        "Hospitality",
        "Technology",
        "Logistics",
        "Government",
        "Real Estate",
    ]
    job_titles = [
        "Accountant",
        "Sales Executive",
        "Engineer",
        "Teacher",
        "Nurse",
        "Driver",
        "Manager",
        "Technician",
        "Business Owner",
        "Software Developer",
    ]
    source_of_funds_options = ["Salary", "Business Income", "Investment Income", "Family Support"]
    source_of_wealth_options = ["Savings", "Business Ownership", "Employment Income", "Investments"]

    for _, customer in customers_df.iterrows():
        employment_status = random.choices(
            employment_statuses,
            weights=[0.72, 0.13, 0.10, 0.05],
            k=1,
        )[0]

        if employment_status == "Employed":
            monthly_income = round(random.uniform(4000, 45000), 2)
            employer_name = f"{random.choice(['Gulf', 'Emirates', 'Al Noor', 'Prime', 'Metro', 'Global'])} {random.choice(['Trading', 'Services', 'Group', 'LLC', 'Holdings'])}"
            job_title = random.choice(job_titles)
            industry = random.choice(industries)
            salary_transfer_bank = random.choice(["Emirates NBD", "ADCB", "FAB", "Mashreq", "Dubai Islamic Bank", "ADIB"])
            length_of_employment_months = random.randint(3, 180)
            source_of_funds = "Salary"
            source_of_wealth = "Employment Income"
            monthly_liabilities = round(monthly_income * random.uniform(0.05, 0.45), 2)

        elif employment_status == "Self-Employed":
            monthly_income = round(random.uniform(7000, 70000), 2)
            employer_name = "Self-Employed"
            job_title = "Business Owner"
            industry = random.choice(industries)
            salary_transfer_bank = random.choice(["Emirates NBD", "ADCB", "FAB", "Mashreq", "Dubai Islamic Bank", "ADIB"])
            length_of_employment_months = random.randint(6, 240)
            source_of_funds = "Business Income"
            source_of_wealth = "Business Ownership"
            monthly_liabilities = round(monthly_income * random.uniform(0.10, 0.55), 2)

        elif employment_status == "Student":
            monthly_income = round(random.uniform(1000, 6000), 2)
            employer_name = ""
            job_title = "Student"
            industry = "Education"
            salary_transfer_bank = ""
            length_of_employment_months = 0
            source_of_funds = "Family Support"
            source_of_wealth = "Family Support"
            monthly_liabilities = round(monthly_income * random.uniform(0.00, 0.20), 2)

        else:
            monthly_income = round(random.uniform(0, 3000), 2)
            employer_name = ""
            job_title = "Unemployed"
            industry = ""
            salary_transfer_bank = ""
            length_of_employment_months = 0
            source_of_funds = random.choice(source_of_funds_options)
            source_of_wealth = random.choice(source_of_wealth_options)
            monthly_liabilities = round(monthly_income * random.uniform(0.00, 0.30), 2)

        employment_records.append(
            {
                "employment_id": f"EMP{len(employment_records) + 1:06d}",
                "customer_id": customer["customer_id"],
                "employment_status": employment_status,
                "employer_name": employer_name,
                "job_title": job_title,
                "industry": industry,
                "monthly_income": monthly_income,
                "salary_transfer_bank": salary_transfer_bank,
                "length_of_employment_months": length_of_employment_months,
                "source_of_funds": source_of_funds,
                "source_of_wealth": source_of_wealth,
                "monthly_liabilities": monthly_liabilities,
            }
        )

    return pd.DataFrame(employment_records)

def generate_kyc_verification(customers_df):
    kyc_records = []

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]

        if customer["customer_status"] == "Suspended":
            kyc_status = random.choices(["Pending", "Rejected", "Expired"], weights=[0.45, 0.35, 0.20], k=1)[0]
        else:
            kyc_status = random.choices(["Approved", "Pending", "Rejected", "Expired"], weights=[0.84, 0.10, 0.03, 0.03], k=1)[0]

        kyc_level = random.choices(
            ["Basic", "Standard", "Enhanced Due Diligence"],
            weights=[0.30, 0.60, 0.10],
            k=1,
        )[0]

        document_score = round(random.uniform(60, 100), 2)
        selfie_score = round(random.uniform(55, 100), 2)

        if kyc_status == "Approved":
            overall_risk_score = round(random.uniform(5, 35), 2)
        elif kyc_status == "Pending":
            overall_risk_score = round(random.uniform(35, 65), 2)
        else:
            overall_risk_score = round(random.uniform(65, 95), 2)

        verification_date = random_date(START_DATE, END_DATE).date()
        next_review_date = verification_date + timedelta(days=random.choice([365, 730, 1095]))

        kyc_records.append(
            {
                "kyc_id": f"KYC{len(kyc_records) + 1:06d}",
                "customer_id": customer_id,
                "kyc_status": kyc_status,
                "kyc_level": kyc_level,
                "verification_method": random.choice(["Digital", "Manual", "Branch", "Third-Party Provider"]),
                "verification_date": verification_date,
                "next_review_date": next_review_date,
                "document_verification_score": document_score,
                "biometric_verification_status": random.choices(
                    ["Passed", "Failed", "Pending"],
                    weights=[0.86, 0.04, 0.10],
                    k=1,
                )[0],
                "selfie_match_score": selfie_score,
                "overall_kyc_risk_score": overall_risk_score,
                "kyc_remarks": "",
            }
        )

    return pd.DataFrame(kyc_records)

def generate_credit_profiles(customers_df, employment_income_df):
    credit_records = []

    income_lookup = employment_income_df.set_index("customer_id")["monthly_income"].to_dict()
    liabilities_lookup = employment_income_df.set_index("customer_id")["monthly_liabilities"].to_dict()

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]

        monthly_income = float(income_lookup.get(customer_id, 0))
        monthly_liabilities = float(liabilities_lookup.get(customer_id, 0))

        if monthly_income <= 3000:
            base_score = random.randint(450, 650)
        elif monthly_income <= 10000:
            base_score = random.randint(550, 750)
        elif monthly_income <= 25000:
            base_score = random.randint(650, 820)
        else:
            base_score = random.randint(700, 850)

        missed_payments_count = random.choices(
            [0, 1, 2, 3, 4, 5],
            weights=[0.60, 0.18, 0.10, 0.06, 0.04, 0.02],
            k=1,
        )[0]

        aecb_score = max(300, base_score - (missed_payments_count * random.randint(20, 45)))

        if aecb_score >= 750:
            credit_score_band = "Excellent"
            credit_risk_category = "Low"
        elif aecb_score >= 650:
            credit_score_band = "Good"
            credit_risk_category = "Low"
        elif aecb_score >= 550:
            credit_score_band = "Fair"
            credit_risk_category = "Medium"
        elif aecb_score >= 450:
            credit_score_band = "Poor"
            credit_risk_category = "High"
        else:
            credit_score_band = "Very Poor"
            credit_risk_category = "High"

        total_active_loans = random.choices([0, 1, 2, 3], weights=[0.55, 0.30, 0.12, 0.03], k=1)[0]
        total_credit_cards = random.choices([0, 1, 2, 3], weights=[0.35, 0.40, 0.18, 0.07], k=1)[0]

        total_outstanding_balance = round(
            (total_active_loans * random.uniform(5000, 75000))
            + (total_credit_cards * random.uniform(1000, 25000)),
            2,
        )

        monthly_installment_amount = round(monthly_liabilities, 2)

        debt_burden_ratio = round(
            (monthly_installment_amount / monthly_income) * 100,
            2,
        ) if monthly_income > 0 else 0

        days_past_due_max = 0 if missed_payments_count == 0 else random.choice([15, 30, 60, 90, 120])
        credit_history_months = random.randint(6, 180)

        credit_records.append(
            {
                "credit_profile_id": f"CRD{len(credit_records) + 1:06d}",
                "customer_id": customer_id,
                "aecb_score": aecb_score,
                "credit_score_band": credit_score_band,
                "credit_report_date": random_date(START_DATE, END_DATE).date(),
                "total_active_loans": total_active_loans,
                "total_credit_cards": total_credit_cards,
                "total_outstanding_balance": total_outstanding_balance,
                "monthly_installment_amount": monthly_installment_amount,
                "debt_burden_ratio": debt_burden_ratio,
                "missed_payments_count": missed_payments_count,
                "days_past_due_max": days_past_due_max,
                "credit_history_months": credit_history_months,
                "credit_risk_category": credit_risk_category,
            }
        )

    return pd.DataFrame(credit_records)
def generate_product_applications(customers_df, credit_profiles_df):
    applications = []
    credit_lookup = credit_profiles_df.set_index("customer_id")["credit_risk_category"].to_dict()

    product_types = ["Wallet", "Card", "Remittance", "Loan", "Account"]
    application_channels = ["Mobile App", "Web", "Branch", "Agent"]

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]
        credit_risk = credit_lookup.get(customer_id, "Medium")

        number_of_applications = random.choices([1, 2, 3, 4], weights=[0.30, 0.40, 0.22, 0.08], k=1)[0]

        for _ in range(number_of_applications):
            product_type = random.choice(product_types)
            application_date = random_date(START_DATE, END_DATE).date()

            if credit_risk == "Low":
                approval_probability = 0.88
            elif credit_risk == "Medium":
                approval_probability = 0.68
            else:
                approval_probability = 0.42

            application_status = random.choices(
                ["Submitted", "Pending", "Approved", "Rejected"],
                weights=[0.06, 0.10, approval_probability, 1 - approval_probability],
                k=1,
            )[0]

            requested_amount = None
            approved_amount = None
            approved_limit = None
            rejection_reason = None

            if product_type in ["Loan", "Card"]:
                requested_amount = round(random.uniform(3000, 150000), 2)

                if application_status == "Approved":
                    if product_type == "Loan":
                        approved_amount = round(requested_amount * random.uniform(0.60, 1.00), 2)
                    else:
                        approved_limit = round(requested_amount * random.uniform(0.30, 0.80), 2)
                elif application_status == "Rejected":
                    rejection_reason = random.choice(
                        [
                            "Low credit score",
                            "High debt burden ratio",
                            "Incomplete documents",
                            "KYC not approved",
                            "Insufficient income",
                        ]
                    )

            decision_date = application_date + timedelta(days=random.randint(1, 14))

            applications.append(
                {
                    "application_id": f"APP{len(applications) + 1:06d}",
                    "customer_id": customer_id,
                    "product_type": product_type,
                    "application_date": application_date,
                    "application_channel": random.choice(application_channels),
                    "application_status": application_status,
                    "requested_amount": requested_amount,
                    "approved_amount": approved_amount,
                    "approved_limit": approved_limit,
                    "rejection_reason": rejection_reason,
                    "decision_date": decision_date,
                }
            )

    return pd.DataFrame(applications)

def generate_document_verification(identity_documents_df):
    verification_records = []

    for _, document in identity_documents_df.iterrows():
        verification_status = document["verification_status"]

        if verification_status == "Verified":
            document_authenticity_status = "Authentic"
            name_match_status = "Matched"
            date_of_birth_match_status = "Matched"
            expiry_check_status = "Valid" if document["document_status"] == "Valid" else "Expired"
            verification_score = round(random.uniform(80, 100), 2)
        elif verification_status == "Pending":
            document_authenticity_status = "Under Review"
            name_match_status = random.choice(["Matched", "Review Required"])
            date_of_birth_match_status = random.choice(["Matched", "Review Required"])
            expiry_check_status = "Review Required"
            verification_score = round(random.uniform(50, 79), 2)
        else:
            document_authenticity_status = random.choice(["Suspicious", "Rejected"])
            name_match_status = random.choice(["Mismatch", "Review Required"])
            date_of_birth_match_status = random.choice(["Mismatch", "Review Required"])
            expiry_check_status = random.choice(["Expired", "Review Required"])
            verification_score = round(random.uniform(10, 49), 2)

        verification_records.append(
            {
                "document_verification_id": f"DV{len(verification_records) + 1:06d}",
                "document_id": document["document_id"],
                "customer_id": document["customer_id"],
                "verification_date": random_date(START_DATE, END_DATE).date(),
                "verification_provider": random.choice(["Onfido", "Persona", "Internal KYC Engine", "Manual Review"]),
                "document_authenticity_status": document_authenticity_status,
                "name_match_status": name_match_status,
                "date_of_birth_match_status": date_of_birth_match_status,
                "expiry_check_status": expiry_check_status,
                "verification_score": verification_score,
                "verification_status": verification_status,
            }
        )

    return pd.DataFrame(verification_records)

def generate_aml_screening(customers_df):
    aml_records = []

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]
        base_score = random.uniform(5, 45)

        if customer_id in ["CUST00001", "CUST00002", "CUST00003"]:
            base_score += random.uniform(25, 45)

        aml_risk_score = round(min(base_score, 100), 2)

        if aml_risk_score >= 70:
            aml_risk_category = "High"
        elif aml_risk_score >= 40:
            aml_risk_category = "Medium"
        else:
            aml_risk_category = "Low"

        aml_records.append({
            "aml_screening_id": f"AML{len(aml_records) + 1:06d}",
            "customer_id": customer_id,
            "screening_date": random_date(START_DATE, END_DATE).date(),
            "aml_risk_score": aml_risk_score,
            "aml_risk_category": aml_risk_category,
            "sanctions_match_status": random.choices(
                ["No Match", "Potential Match", "Confirmed Match"],
                weights=[0.96, 0.035, 0.005],
                k=1
            )[0],
            "pep_status": random.choices(
                ["Not PEP", "PEP", "Related to PEP"],
                weights=[0.94, 0.04, 0.02],
                k=1
            )[0],
            "adverse_media_status": random.choices(
                ["No Adverse Media", "Potential Adverse Media", "Confirmed Adverse Media"],
                weights=[0.92, 0.06, 0.02],
                k=1
            )[0],
            "high_risk_country_flag": aml_risk_category == "High",
            "suspicious_activity_flag": aml_risk_category == "High",
            "screening_status": "Escalated" if aml_risk_category == "High" else "Cleared",
        })

    return pd.DataFrame(aml_records)


def generate_customer_risk_profiles(customers_df, kyc_verification_df, credit_profiles_df, aml_screening_df):
    risk_records = []

    kyc_lookup = kyc_verification_df.set_index("customer_id")["overall_kyc_risk_score"].to_dict()
    credit_lookup = credit_profiles_df.set_index("customer_id")["credit_risk_category"].to_dict()
    aml_lookup = aml_screening_df.set_index("customer_id")["aml_risk_score"].to_dict()

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]

        onboarding_risk_score = float(kyc_lookup.get(customer_id, 50))
        aml_risk_score = float(aml_lookup.get(customer_id, 50))

        credit_category = credit_lookup.get(customer_id, "Medium")
        credit_risk_score = {"Low": 25, "Medium": 55, "High": 80}.get(credit_category, 55)

        transaction_risk_score = random.uniform(10, 45)
        fraud_risk_score = random.uniform(10, 45)

        if customer_id in ["CUST00001", "CUST00002", "CUST00003"]:
            transaction_risk_score += random.uniform(25, 45)
            fraud_risk_score += random.uniform(25, 45)

        final_risk_score = round(
            (
                onboarding_risk_score * 0.20
                + transaction_risk_score * 0.25
                + credit_risk_score * 0.20
                + fraud_risk_score * 0.20
                + aml_risk_score * 0.15
            ),
            2,
        )

        if final_risk_score >= 70:
            customer_risk_category = "High"
        elif final_risk_score >= 40:
            customer_risk_category = "Medium"
        else:
            customer_risk_category = "Low"

        risk_records.append({
            "risk_profile_id": f"RISK{len(risk_records) + 1:06d}",
            "customer_id": customer_id,
            "risk_assessment_date": random_date(START_DATE, END_DATE).date(),
            "customer_risk_category": customer_risk_category,
            "onboarding_risk_score": round(onboarding_risk_score, 2),
            "transaction_risk_score": round(transaction_risk_score, 2),
            "credit_risk_score": round(credit_risk_score, 2),
            "fraud_risk_score": round(fraud_risk_score, 2),
            "aml_risk_score": round(aml_risk_score, 2),
            "final_risk_score": final_risk_score,
            "risk_reason": "High-risk behavioral indicators" if customer_risk_category == "High" else "",
            "review_status": "Open" if customer_risk_category == "High" else "Closed",
        })

    return pd.DataFrame(risk_records)


def generate_kyc_review_history(customers_df, kyc_verification_df):
    review_records = []

    kyc_lookup = kyc_verification_df.set_index("customer_id")["kyc_status"].to_dict()

    for _, customer in customers_df.iterrows():
        customer_id = customer["customer_id"]
        current_status = kyc_lookup.get(customer_id, "Pending")

        review_records.append({
            "review_id": f"REV{len(review_records) + 1:06d}",
            "customer_id": customer_id,
            "review_date": random_date(START_DATE, END_DATE).date(),
            "review_type": random.choice(["Initial Review", "Periodic Review", "Enhanced Review"]),
            "previous_kyc_status": random.choice(["Pending", "Approved", "Expired"]),
            "new_kyc_status": current_status,
            "reviewer_name": random.choice(["KYC Analyst 1", "KYC Analyst 2", "Compliance Officer"]),
            "review_decision": "Approved" if current_status == "Approved" else random.choice(["Rejected", "Escalated", "Pending"]),
            "review_comments": "",
        })

    return pd.DataFrame(review_records)


def generate_wallet_accounts(customers_df):
    wallet_records = []

    for _, customer in customers_df.iterrows():
        wallet_records.append({
            "wallet_id": f"WAL{len(wallet_records) + 1:06d}",
            "customer_id": customer["customer_id"],
            "wallet_status": random.choices(
                ["Active", "Inactive", "Suspended", "Closed"],
                weights=[0.85, 0.08, 0.05, 0.02],
                k=1
            )[0],
            "opening_date": customer["signup_date"],
            "current_balance": round(random.uniform(0, 25000), 2),
            "wallet_tier": random.choice(["Basic", "Standard", "Premium"]),
            "daily_transaction_limit": random.choice([5000, 10000, 25000, 50000]),
            "monthly_transaction_limit": random.choice([50000, 100000, 250000, 500000]),
        })

    return pd.DataFrame(wallet_records)


def generate_merchants(n_merchants=400):
    merchant_records = []
    categories = ["Retail", "Grocery", "Travel", "Electronics", "Services", "Fuel", "Restaurant", "Healthcare"]

    for i in range(1, n_merchants + 1):
        merchant_records.append({
            "merchant_id": f"MER{i:05d}",
            "merchant_name": f"{random.choice(['Al Noor', 'Metro', 'Prime', 'City', 'Global', 'Emirates'])} {random.choice(categories)} {i}",
            "merchant_category": random.choice(categories),
            "emirate": random.choice(UAE_EMIRATES),
            "onboarding_date": random_date(START_DATE, END_DATE).date(),
            "merchant_status": random.choices(
                ["Active", "Inactive", "Suspended"],
                weights=[0.88, 0.09, 0.03],
                k=1
            )[0],
        })

    return pd.DataFrame(merchant_records)

def generate_wallet_transactions(wallet_accounts_df, customers_df, merchants_df, n_transactions=50000):
    transactions = []

    wallet_ids = wallet_accounts_df["wallet_id"].tolist()
    merchant_ids = merchants_df["merchant_id"].tolist()
    customer_lookup = wallet_accounts_df.set_index("wallet_id")["customer_id"].to_dict()

    for i in range(1, n_transactions + 1):
        wallet_id = random.choice(wallet_ids)
        customer_id = customer_lookup[wallet_id]

        transaction_date = random_date(START_DATE, END_DATE)
        transaction_type = random.choices(
            ["Top-up", "Payment", "Transfer", "Withdrawal", "Refund"],
            weights=[0.20, 0.50, 0.18, 0.08, 0.04],
            k=1,
        )[0]

        amount = round(random.uniform(10, 2500), 2)

        # Behavioral patterns for selected case-study customers
        if customer_id == "CUST00001":
            transaction_type = random.choice(["Transfer", "Payment"])
            amount = round(random.uniform(900, 990), 2)
        elif customer_id == "CUST00002":
            amount = round(random.uniform(2000, 9000), 2)

        transaction_status = random.choices(
            ["Success", "Failed", "Pending", "Reversed"],
            weights=[0.88, 0.07, 0.03, 0.02],
            k=1,
        )[0]

        if customer_id == "CUST00002":
            transaction_status = random.choices(
                ["Success", "Failed", "Pending", "Reversed"],
                weights=[0.70, 0.20, 0.05, 0.05],
                k=1,
            )[0]

        failure_reason = ""
        if transaction_status == "Failed":
            failure_reason = random.choice(
                ["Insufficient Balance", "Invalid PIN", "Network Error", "Risk Rule Decline", "Limit Exceeded"]
            )

        transactions.append(
            {
                "transaction_id": f"WTX{i:07d}",
                "wallet_id": wallet_id,
                "customer_id": customer_id,
                "transaction_date": transaction_date,
                "transaction_type": transaction_type,
                "channel": random.choice(["Mobile App", "Web", "POS", "API"]),
                "merchant_id": random.choice(merchant_ids) if transaction_type == "Payment" else "",
                "amount": amount,
                "currency": "AED",
                "transaction_status": transaction_status,
                "failure_reason": failure_reason,
                "device_id": f"DEV{random.randint(1, 3000):05d}",
                "location_emirate": random.choice(UAE_EMIRATES),
            }
        )

    return pd.DataFrame(transactions)


def generate_card_payments(customers_df, merchants_df, n_payments=50000):
    card_records = []

    customer_ids = customers_df["customer_id"].tolist()
    merchant_ids = merchants_df["merchant_id"].tolist()

    for i in range(1, n_payments + 1):
        customer_id = random.choice(customer_ids)
        amount = round(random.uniform(20, 5000), 2)

        if customer_id == "CUST00002":
            amount = round(random.uniform(3000, 15000), 2)

        payment_status = random.choices(
            ["Approved", "Declined", "Reversed"],
            weights=[0.90, 0.08, 0.02],
            k=1,
        )[0]

        if customer_id == "CUST00002":
            payment_status = random.choices(
                ["Approved", "Declined", "Reversed"],
                weights=[0.72, 0.23, 0.05],
                k=1,
            )[0]

        decline_reason = ""
        if payment_status == "Declined":
            decline_reason = random.choice(
                ["Insufficient Limit", "Incorrect CVV", "Risk Rule Decline", "Card Expired", "Issuer Decline"]
            )

        card_records.append(
            {
                "card_payment_id": f"CPY{i:07d}",
                "customer_id": customer_id,
                "transaction_date": random_date(START_DATE, END_DATE),
                "card_type": random.choice(["Debit", "Credit", "Prepaid"]),
                "card_network": random.choice(["Visa", "Mastercard", "Local Network"]),
                "merchant_id": random.choice(merchant_ids),
                "amount": amount,
                "currency": "AED",
                "payment_status": payment_status,
                "decline_reason": decline_reason,
                "interchange_fee": round(amount * random.uniform(0.002, 0.018), 2),
            }
        )

    return pd.DataFrame(card_records)


def generate_remittance(customers_df, n_remittance=10000):
    remittance_records = []

    customer_ids = customers_df["customer_id"].tolist()
    normal_countries = ["India", "Pakistan", "Philippines", "Bangladesh", "Sri Lanka", "Nepal", "Egypt", "Jordan"]
    high_risk_countries = ["Syria", "Yemen", "Afghanistan"]

    for i in range(1, n_remittance + 1):
        customer_id = random.choice(customer_ids)

        if customer_id == "CUST00003":
            destination_country = random.choice(high_risk_countries)
            transfer_amount = round(random.uniform(5000, 25000), 2)
        else:
            destination_country = random.choice(normal_countries)
            transfer_amount = round(random.uniform(200, 8000), 2)

        transfer_status = random.choices(
            ["Completed", "Failed", "Pending"],
            weights=[0.88, 0.07, 0.05],
            k=1,
        )[0]

        remittance_records.append(
            {
                "remittance_id": f"REM{i:07d}",
                "customer_id": customer_id,
                "transfer_date": random_date(START_DATE, END_DATE),
                "destination_country": destination_country,
                "transfer_amount": transfer_amount,
                "exchange_rate": round(random.uniform(0.07, 85.00), 6),
                "transfer_fee": round(random.uniform(5, 75), 2),
                "transfer_status": transfer_status,
                "channel": random.choice(["Mobile App", "Branch", "Partner"]),
            }
        )

    return pd.DataFrame(remittance_records)

def generate_loans(customers_df, product_applications_df, credit_profiles_df):
    loan_records = []

    credit_score_lookup = credit_profiles_df.set_index("customer_id")["aecb_score"].to_dict()

    approved_loan_applications = product_applications_df[
        (product_applications_df["product_type"] == "Loan")
        & (product_applications_df["application_status"] == "Approved")
    ]

    for _, application in approved_loan_applications.iterrows():
        customer_id = application["customer_id"]
        approved_amount = application["approved_amount"]

        if pd.isna(approved_amount) or approved_amount == "":
            approved_amount = random.uniform(5000, 80000)

        approved_amount = float(approved_amount)
        interest_rate = round(random.uniform(7.5, 24.0), 2)
        tenure_months = random.choice([6, 12, 18, 24, 36, 48])
        application_date = pd.to_datetime(application["application_date"]).date()
        disbursement_date = application_date + timedelta(days=random.randint(1, 10))
        maturity_date = disbursement_date + timedelta(days=tenure_months * 30)

        credit_score = int(credit_score_lookup.get(customer_id, random.randint(450, 750)))

        if credit_score >= 700:
            default_risk_score = round(random.uniform(5, 30), 2)
        elif credit_score >= 600:
            default_risk_score = round(random.uniform(30, 60), 2)
        else:
            default_risk_score = round(random.uniform(60, 90), 2)

        loan_status = random.choices(
            ["Active", "Closed", "Defaulted"],
            weights=[0.65, 0.28, 0.07],
            k=1,
        )[0]

        loan_records.append(
            {
                "loan_id": f"LOAN{len(loan_records) + 1:06d}",
                "customer_id": customer_id,
                "application_id": application["application_id"],
                "application_date": application_date,
                "loan_amount": round(float(application["requested_amount"]), 2),
                "approved_amount": round(approved_amount, 2),
                "loan_status": loan_status,
                "interest_rate": interest_rate,
                "tenure_months": tenure_months,
                "credit_score": credit_score,
                "default_risk_score": default_risk_score,
                "disbursement_date": disbursement_date,
                "maturity_date": maturity_date,
            }
        )

    return pd.DataFrame(loan_records)


def generate_repayments(loans_df):
    repayment_records = []

    for _, loan in loans_df.iterrows():
        tenure_months = int(loan["tenure_months"])
        approved_amount = float(loan["approved_amount"])
        monthly_due = round(approved_amount / tenure_months, 2)
        disbursement_date = pd.to_datetime(loan["disbursement_date"]).date()

        for month_no in range(1, tenure_months + 1):
            due_date = disbursement_date + timedelta(days=30 * month_no)

            repayment_status = random.choices(
                ["Paid", "Late", "Missed", "Partial"],
                weights=[0.78, 0.12, 0.06, 0.04],
                k=1,
            )[0]

            if loan["loan_status"] == "Defaulted" and month_no > tenure_months * 0.5:
                repayment_status = random.choices(
                    ["Missed", "Partial", "Late"],
                    weights=[0.60, 0.25, 0.15],
                    k=1,
                )[0]

            if repayment_status == "Paid":
                payment_date = due_date
                paid_amount = monthly_due
                days_past_due = 0
            elif repayment_status == "Late":
                days_past_due = random.choice([5, 10, 15, 30, 45])
                payment_date = due_date + timedelta(days=days_past_due)
                paid_amount = monthly_due
            elif repayment_status == "Partial":
                days_past_due = random.choice([15, 30, 60])
                payment_date = due_date + timedelta(days=days_past_due)
                paid_amount = round(monthly_due * random.uniform(0.25, 0.75), 2)
            else:
                days_past_due = random.choice([30, 60, 90, 120])
                payment_date = ""
                paid_amount = 0

            repayment_records.append(
                {
                    "repayment_id": f"RPY{len(repayment_records) + 1:07d}",
                    "loan_id": loan["loan_id"],
                    "customer_id": loan["customer_id"],
                    "due_date": due_date,
                    "payment_date": payment_date,
                    "due_amount": monthly_due,
                    "paid_amount": paid_amount,
                    "repayment_status": repayment_status,
                    "days_past_due": days_past_due,
                }
            )

    return pd.DataFrame(repayment_records)


def generate_collections(repayments_df):
    collection_records = []

    overdue_repayments = repayments_df[
        repayments_df["repayment_status"].isin(["Late", "Missed", "Partial"])
    ]

    for _, repayment in overdue_repayments.iterrows():
        if random.random() > 0.45:
            continue

        outstanding_amount = float(repayment["due_amount"]) - float(repayment["paid_amount"])

        if repayment["days_past_due"] >= 90:
            collection_stage = random.choice(["Legal", "Write-Off", "Hard Collection"])
        elif repayment["days_past_due"] >= 30:
            collection_stage = random.choice(["Soft Collection", "Reminder"])
        else:
            collection_stage = "Reminder"

        collection_records.append(
            {
                "collection_id": f"COL{len(collection_records) + 1:07d}",
                "loan_id": repayment["loan_id"],
                "customer_id": repayment["customer_id"],
                "collection_date": pd.to_datetime(repayment["due_date"]).date() + timedelta(days=int(repayment["days_past_due"])),
                "collection_stage": collection_stage,
                "outstanding_amount": round(max(outstanding_amount, 0), 2),
                "action_taken": random.choice(["SMS", "Call", "Email", "Legal Notice"]),
                "recovery_status": random.choice(["Recovered", "Pending", "Escalated", "Written Off"]),
            }
        )

    return pd.DataFrame(collection_records)


# The following function generates mock fraud alerts based on wallet transactions, 
# card payments, and remittance data. It creates a list of fraud alerts with various attributes 
# such as alert type, fraud score, and investigation results.

def generate_fraud_alerts(wallet_trasactions_df, card_payments_df, remittance_df):
  
    fraud_alerts = []

    alert_status_options = ["Open", "Reviewed", "Closed", "Escalated"]
    investigation_result_options = ["Under Review", "False Positive", "Confirmed Fraud", "No Issue Found"]

    def add_alert(customer_id, alert_date, alert_type, fraud_score, transaction_id="", card_payment_id="", remittance_id=""):
        fraud_alerts.append(
    
            {
            "fraud_alert_id": f"FRAUD{len(fraud_alerts) + 1:07d}",
            "customer_id": customer_id,
            "alert_date": alert_date,
            "transaction_id": transaction_id,
            "card_payment_id": card_payment_id,
            "remittance_id": remittance_id,
            "alert_type": alert_type,
            "fraud_score": round(fraud_score, 2),
            "alert_status": random.choice(alert_status_options),
            "investigation_result": random.choice(investigation_result_options),
        }
    )

if __name__ == "__main__":

    customers_df = generate_customers()
    identity_documents_df = generate_identity_documents(customers_df)
    document_verification_df = generate_document_verification(identity_documents_df)
    customer_addresses_df = generate_customer_addresses(customers_df)
    employment_income_df = generate_employment_income(customers_df)
    kyc_verification_df = generate_kyc_verification(customers_df)
    credit_profiles_df = generate_credit_profiles(customers_df, employment_income_df)
    product_applications_df = generate_product_applications(customers_df, credit_profiles_df)
    aml_screening_df = generate_aml_screening(customers_df)
    customer_risk_profiles_df = generate_customer_risk_profiles(
        customers_df,
        kyc_verification_df,
        credit_profiles_df,
        aml_screening_df,
    )
    kyc_review_history_df = generate_kyc_review_history(customers_df, kyc_verification_df)
    wallet_accounts_df = generate_wallet_accounts(customers_df)
    merchants_df = generate_merchants()
    wallet_transactions_df = generate_wallet_transactions(wallet_accounts_df, customers_df, merchants_df)
    card_payments_df = generate_card_payments(customers_df, merchants_df)
    remittance_df = generate_remittance(customers_df)
    loans_df = generate_loans(customers_df, product_applications_df, credit_profiles_df)
    repayments_df = generate_repayments(loans_df)
    collections_df = generate_collections(repayments_df)

    customers_df.to_csv(DATA_DIR / "customers.csv", index=False)
    identity_documents_df.to_csv(DATA_DIR / "identity_documents.csv", index=False)
    document_verification_df.to_csv(DATA_DIR / "document_verification.csv", index=False)
    customer_addresses_df.to_csv(DATA_DIR / "customer_addresses.csv", index=False)
    employment_income_df.to_csv(DATA_DIR / "employment_income.csv", index=False)
    kyc_verification_df.to_csv(DATA_DIR / "kyc_verification.csv", index=False)
    credit_profiles_df.to_csv(DATA_DIR / "credit_profiles.csv", index=False)
    product_applications_df.to_csv(DATA_DIR / "product_applications.csv", index=False)
    aml_screening_df.to_csv(DATA_DIR / "aml_screening.csv", index=False)
    customer_risk_profiles_df.to_csv(DATA_DIR / "customer_risk_profiles.csv", index=False)
    kyc_review_history_df.to_csv(DATA_DIR / "kyc_review_history.csv", index=False)
    wallet_accounts_df.to_csv(DATA_DIR / "wallet_accounts.csv", index=False)
    merchants_df.to_csv(DATA_DIR / "merchants.csv", index=False)
    wallet_transactions_df.to_csv(DATA_DIR / "wallet_transactions.csv", index=False)
    card_payments_df.to_csv(DATA_DIR / "card_payments.csv", index=False)
    remittance_df.to_csv(DATA_DIR / "remittance.csv", index=False)
    loans_df.to_csv(DATA_DIR / "loans.csv", index=False)
    repayments_df.to_csv(DATA_DIR / "repayments.csv", index=False)
    collections_df.to_csv(DATA_DIR / "collections.csv", index=False)
    
    print(f"Total loans: {len(loans_df)}")
    print(f"Total repayments: {len(repayments_df)}")
    print(f"Total collections: {len(collections_df)}")