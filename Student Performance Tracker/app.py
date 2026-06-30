import streamlit as st
import pandas as pd
import numpy as np
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="Student Performance Tracker", page_icon="🎓", layout="centered")

# Create sample dataset if not exists
if not os.path.exists("student_performance.csv"):

    np.random.seed(42)

    n = 500

    hours = np.random.randint(1, 11, n)
    attendance = np.random.randint(60, 101, n)
    previous = np.random.randint(40, 101, n)
    sleep = np.random.randint(4, 10, n)
    assignments = np.random.randint(0, 11, n)

    performance = (
        hours * 5 +
        attendance * 0.30 +
        previous * 0.40 +
        sleep * 2 +
        assignments * 2 +
        np.random.normal(0, 5, n)
    )

    performance = np.clip(performance, 0, 100)

    df = pd.DataFrame({
        "Hours_Studied": hours,
        "Attendance": attendance,
        "Previous_Score": previous,
        "Sleep_Hours": sleep,
        "Assignments_Completed": assignments,
        "Performance": performance
    })

    df.to_csv("student_performance.csv", index=False)

# Load dataset
df = pd.read_csv("student_performance.csv")

X = df.drop("Performance", axis=1)
y = df["Performance"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

st.title("🎓 Student Performance Tracker")

st.write("Predict the student's overall performance based on study habits.")

hours = st.slider("Hours Studied", 0, 12, 5)

attendance = st.slider("Attendance (%)", 50, 100, 85)

previous = st.slider("Previous Score", 0, 100, 75)

sleep = st.slider("Sleep Hours", 3, 10, 7)

assignments = st.slider("Assignments Completed", 0, 10, 6)

if st.button("Predict Performance"):

    sample = pd.DataFrame({
        "Hours_Studied": [hours],
        "Attendance": [attendance],
        "Previous_Score": [previous],
        "Sleep_Hours": [sleep],
        "Assignments_Completed": [assignments]
    })

    prediction = model.predict(sample)[0]

    st.subheader(f"Predicted Performance: {prediction:.2f}%")

    if prediction >= 85:
        st.success("🏆 Excellent Performance")
        st.balloons()

    elif prediction >= 70:
        st.info("👍 Good Performance")

    elif prediction >= 50:
        st.warning("🙂 Average Performance")

    else:
        st.error("⚠️ Needs Improvement")

st.markdown("---")
st.write(f"### Model Accuracy (R² Score): **{accuracy:.2f}**")

st.subheader("Dataset Preview")
st.dataframe(df.head())