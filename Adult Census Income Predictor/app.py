# app.py

import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Page configuration
st.set_page_config(
    page_title="Adult Census Income Predictor",
    page_icon="💰",
    layout="centered"
)


# Title
st.title("💰 Adult Census Income Predictor")

st.write(
    "Predict whether a person's income is **<=50K or >50K** "
    "based on demographic and employment information."
)


# Create sample dataset if not exists
@st.cache_data
def create_dataset():

    np.random.seed(42)

    n = 1000

    data = {

        "age": np.random.randint(18, 70, n),

        "workclass": np.random.choice(
            ["Private", "Government", "Self-employed"], n
        ),

        "education": np.random.choice(
            ["High School", "Bachelor", "Master", "Doctorate"], n
        ),

        "education_num": np.random.randint(1, 16, n),

        "hours_per_week": np.random.randint(20, 60, n),

        "occupation": np.random.choice(
            ["Tech", "Sales", "Management", "Service"], n
        ),

        "capital_gain": np.random.randint(0, 10000, n),

        "capital_loss": np.random.randint(0, 5000, n)

    }


    df = pd.DataFrame(data)


    income = []

    for i in range(n):

        score = (
            df.education_num[i] * 3 +
            df.hours_per_week[i] * 0.5 +
            df.capital_gain[i] * 0.001 +
            np.random.randint(-10,10)
        )


        if score > 45:
            income.append(">50K")

        else:
            income.append("<=50K")


    df["income"] = income

    return df



df = create_dataset()



# Encode categorical columns

encoder = LabelEncoder()


for col in df.select_dtypes(include="object").columns:

    df[col] = encoder.fit_transform(df[col])



# Split data

X = df.drop("income", axis=1)

y = df["income"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)



# Train model

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42
)


model.fit(
    X_train,
    y_train
)



accuracy = accuracy_score(
    y_test,
    model.predict(X_test)
)



# User Inputs

st.sidebar.header("Enter Person Details")


age = st.sidebar.slider(
    "Age",
    18,
    80,
    30
)


workclass = st.sidebar.selectbox(
    "Work Class",
    [
        "Private",
        "Government",
        "Self-employed"
    ]
)


education = st.sidebar.selectbox(
    "Education",
    [
        "High School",
        "Bachelor",
        "Master",
        "Doctorate"
    ]
)



education_num = st.sidebar.slider(
    "Education Level Number",
    1,
    16,
    10
)



hours = st.sidebar.slider(
    "Working Hours per Week",
    20,
    60,
    40
)



occupation = st.sidebar.selectbox(
    "Occupation",
    [
        "Tech",
        "Sales",
        "Management",
        "Service"
    ]
)



capital_gain = st.sidebar.number_input(
    "Capital Gain",
    0,
    100000,
    0
)



capital_loss = st.sidebar.number_input(
    "Capital Loss",
    0,
    50000,
    0
)



# Prediction

if st.button("Predict Income"):


    input_data = pd.DataFrame(
        {

        "age":[age],

        "workclass":[
            encoder.transform([workclass])[0]
        ],

        "education":[
            encoder.transform([education])[0]
        ],

        "education_num":[education_num],

        "hours_per_week":[hours],

        "occupation":[
            encoder.transform([occupation])[0]
        ],

        "capital_gain":[capital_gain],

        "capital_loss":[capital_loss]

        }
    )



    prediction = model.predict(
        input_data
    )[0]



    st.subheader(
        "Prediction Result"
    )


    if prediction == 1:

        st.success(
            "💰 Income Prediction: >50K"
        )

        st.balloons()


    else:

        st.warning(
            "💼 Income Prediction: <=50K"
        )



# Accuracy

st.markdown("---")

st.write(
    f"### Model Accuracy: **{accuracy*100:.2f}%**"
)



st.subheader(
    "Dataset Preview"
)


st.dataframe(
    create_dataset().head()
)