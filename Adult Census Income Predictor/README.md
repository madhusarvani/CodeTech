# 💰 Adult Census Income Predictor

## Intern Details

- **Intern ID:** CTIS9693
- **Full Name:** Tatapudi Madhu Sarvani
- **No. of Weeks:** 8 Weeks
- **Project Name:** Adult Census Income Predictor

A Machine Learning based web application built using **Streamlit** that predicts whether a person's annual income is **greater than $50K or less than/equal to $50K** based on demographic and employment-related information.

The application uses a **Random Forest Classifier** model with an interactive Streamlit interface.

---

## 🚀 Features

- 🤖 Machine Learning income prediction
- 📊 Random Forest Classification model
- 🎨 Interactive Streamlit dashboard
- 💼 Predicts:
  - Income <= 50K
  - Income > 50K
- 📈 Displays model accuracy
- 🧑‍💻 User-friendly input panel
- 📋 Dataset preview
- ⚡ Automatic sample dataset generation
- 🛠️ No external dataset required

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

## 📂 Project Structure

```
Adult-Census-Income-Predictor/

│
├── app.py
├── requirements.txt
└── README.md

```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/adult-census-income-predictor.git
```

---

### 2. Navigate to Project Folder

```bash
cd adult-census-income-predictor
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Application

Start Streamlit server:

```bash
streamlit run app.py
```

Application will open in your browser:

```
http://localhost:8501
```

---

# 📦 Requirements

Create a file named:

```
requirements.txt
```

Add:

```
streamlit
pandas
numpy
scikit-learn
```

---

# 🧠 Machine Learning Model

The project uses:

## Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to produce accurate classification results.

---

## Input Features

| Feature | Description |
|---|---|
| Age | Person's age |
| Work Class | Employment category |
| Education | Education qualification |
| Education Number | Education level score |
| Hours per Week | Weekly working hours |
| Occupation | Type of job |
| Capital Gain | Additional income gain |
| Capital Loss | Financial loss |

---

## Output

The model predicts:

```
Income Category
```

Possible results:

```
<=50K
>50K
```

---

# 🔄 Machine Learning Workflow

```
User Input
     |
     ↓
Data Preprocessing
     |
     ↓
Label Encoding
     |
     ↓
Random Forest Classifier
     |
     ↓
Income Prediction
```

---

# 📊 Model Evaluation

The model is evaluated using:

```
Accuracy Score
```

Example:

```
Model Accuracy: 90%
```

---

# 🖥️ Application Screens

The dashboard contains:

- Input sidebar
- Prediction button
- Income result display
- Model accuracy
- Dataset preview

---

# 🔮 Future Improvements

- Use real Adult Census dataset
- Add data visualization charts
- Add user authentication
- Save prediction history
- Deploy on Streamlit Cloud
- Improve model using:
  - XGBoost
  - Neural Networks
  - Gradient Boosting

---

# 👩‍💻 Author

**Madhu Sarvani**

B.Tech Information Technology

---

# 📜 License

This project is developed for educational and learning purposes.
