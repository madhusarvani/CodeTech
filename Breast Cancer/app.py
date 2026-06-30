import streamlit as st
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Breast Cancer Diagnostic System",
    page_icon="🩺",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["Diagnosis"] = data.target

X = df.drop("Diagnosis", axis=1)
y = df["Diagnosis"]

# -----------------------------
# Train Model
# -----------------------------
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
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

# -----------------------------
# UI
# -----------------------------
st.title("🩺 Breast Cancer Diagnostic System")

st.write(
    "Enter the patient's medical measurements to predict "
    "whether the tumor is **Benign** or **Malignant**."
)

st.sidebar.header("Patient Measurements")

values = []

for feature in data.feature_names:
    value = st.sidebar.number_input(
        feature.title(),
        value=float(df[feature].mean()),
        format="%.3f"
    )
    values.append(value)

if st.sidebar.button("Predict Diagnosis"):

    sample = scaler.transform([values])

    prediction = model.predict(sample)[0]

    probability = model.predict_proba(sample)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("✅ Benign Tumor")
        st.metric(
            "Confidence",
            f"{probability[1]*100:.2f}%"
        )
        st.balloons()

    else:
        st.error("⚠ Malignant Tumor")
        st.metric(
            "Confidence",
            f"{probability[0]*100:.2f}%"
        )

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

with col2:
    st.subheader("Model Accuracy")
    st.success(f"{accuracy*100:.2f}%")

st.subheader("Dataset Statistics")
st.dataframe(df.describe())