import streamlit as st
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

# ----------------------------
# Generate Dataset
# ----------------------------
np.random.seed(42)

rows = 1500

income = np.random.randint(1500, 30000, rows)
co_income = np.random.randint(0, 15000, rows)
loan_amount = np.random.randint(50, 400, rows)
credit = np.random.choice([0, 1], rows, p=[0.2, 0.8])
term = np.random.choice([180, 240, 300, 360], rows)
age = np.random.randint(21, 60, rows)

approval = []

for i in range(rows):

    score = (
        income[i]*0.45 +
        co_income[i]*0.25 +
        credit[i]*12000 -
        loan_amount[i]*45 +
        age[i]*20
    )

    if score > 12000:
        approval.append(1)
    else:
        approval.append(0)

df = pd.DataFrame({
    "ApplicantIncome": income,
    "CoApplicantIncome": co_income,
    "LoanAmount": loan_amount,
    "LoanTerm": term,
    "CreditHistory": credit,
    "Age": age,
    "LoanApproved": approval
})

# ----------------------------
# Train Model
# ----------------------------

X = df.drop("LoanApproved", axis=1)
y = df["LoanApproved"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = accuracy_score(
    y_test,
    model.predict(X_test)
)

# ----------------------------
# UI
# ----------------------------

st.title("🏦 Loan Approval Predictor")

st.write("Fill applicant information below.")

income = st.number_input(
    "Applicant Income",
    1000,
    50000,
    7000
)

co_income = st.number_input(
    "Co-Applicant Income",
    0,
    30000,
    2000
)

loan = st.number_input(
    "Loan Amount (Thousands)",
    20,
    500,
    120
)

term = st.selectbox(
    "Loan Term",
    [180,240,300,360]
)

credit = st.selectbox(
    "Credit History",
    ["Good","Poor"]
)

age = st.slider(
    "Age",
    21,
    60,
    30
)

credit_value = 1 if credit=="Good" else 0

sample = pd.DataFrame({
    "ApplicantIncome":[income],
    "CoApplicantIncome":[co_income],
    "LoanAmount":[loan],
    "LoanTerm":[term],
    "CreditHistory":[credit_value],
    "Age":[age]
})

if st.button("Predict Loan Approval"):

    prediction = model.predict(sample)[0]

    probability = model.predict_proba(sample)[0]

    if prediction==1:

        st.success("✅ Loan Approved")

        st.metric(
            "Approval Probability",
            f"{probability[1]*100:.2f}%"
        )

        st.balloons()

    else:

        st.error("❌ Loan Rejected")

        st.metric(
            "Rejection Probability",
            f"{probability[0]*100:.2f}%"
        )

st.divider()

st.subheader("Model Accuracy")

st.success(f"{accuracy*100:.2f}%")

st.subheader("Dataset Preview")

st.dataframe(df.head(15))

st.subheader("Dataset Statistics")

st.dataframe(df.describe())