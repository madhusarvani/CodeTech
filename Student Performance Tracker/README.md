# Loan Approval Predictor

## Intern Details

- Intern ID:CTIS9693
- Full Name: Tatapudi Madhu Sarvani
- No. of Weeks: 8 Weeks
- Project Name: Student Performance Tracker
🎓 Student Performance Tracker

A Machine Learning based web application built using **Streamlit** that predicts a student's overall performance based on study habits, attendance, previous scores, sleep hours, and assignment completion.

The application uses a **Random Forest Regression model** to analyze student data and provide performance predictions with a simple interactive interface.

---

## 🚀 Features

- 📊 Predicts student performance percentage
- 🤖 Uses Machine Learning (Random Forest Regression)
- 🎯 Interactive Streamlit dashboard
- 📈 Displays model accuracy (R² Score)
- 📝 Takes student inputs:
  - Hours studied
  - Attendance percentage
  - Previous score
  - Sleep hours
  - Assignments completed
- 🏆 Performance classification:
  - Excellent Performance
  - Good Performance
  - Average Performance
  - Needs Improvement
- 📂 Automatically creates sample dataset if not available
- 👀 Displays dataset preview

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Random Forest Regression

---

## 📂 Project Structure

```
Student-Performance-Tracker/
│
├── app.py
├── student_performance.csv
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/student-performance-tracker.git
```

### 2. Navigate into project folder

```bash
cd student-performance-tracker
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser:

```
http://localhost:8501
```

---

## 📦 Required Libraries

Create a `requirements.txt` file:

```
streamlit
pandas
numpy
scikit-learn
```

---

## 🧠 Machine Learning Model

The project uses:

### Random Forest Regression

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy.

### Input Features

| Feature | Description |
|---|---|
| Hours_Studied | Number of hours spent studying |
| Attendance | Student attendance percentage |
| Previous_Score | Previous academic score |
| Sleep_Hours | Daily sleep duration |
| Assignments_Completed | Completed assignments count |

### Output

```
Predicted Performance (%)
```

---

## 📊 Model Training

The dataset is split into:

- Training Data → 80%
- Testing Data → 20%

The model is evaluated using:

```
R² Score
```

Higher R² value indicates better prediction performance.

---

## 🎯 Example Prediction

Input:

```
Hours Studied: 8
Attendance: 95%
Previous Score: 85
Sleep Hours: 7
Assignments Completed: 9
```

Output:

```
Predicted Performance: 90.45%

🏆 Excellent Performance
```

---

## 📸 Application Preview

The dashboard contains:

- Student input controls
- Prediction button
- Performance result
- Model accuracy score
- Dataset preview

---

## 🔮 Future Improvements

- Add real student datasets
- Add student login system
- Store predictions in database
- Add performance graphs
- Add attendance analytics
- Deploy using Streamlit Cloud
- Improve model using XGBoost/Neural Networks

---

## 👩‍💻 Author

**Madhu Sarvani**

B.Tech Information Technology

---

## 📜 License

This project is created for educational and learning purposes.
