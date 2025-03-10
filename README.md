
# 📄 AI-powered Resume Screening and Ranking System

This project is a web-based application built using **Streamlit** that ranks resumes based on a provided job description using **TF-IDF** (Term Frequency-Inverse Document Frequency) and **cosine similarity**. It allows users to upload multiple PDF resumes and visualize the ranking results.

## 🚀 Features
- Extract text from PDF resumes.
- Compare resumes with a given job description using TF-IDF and cosine similarity.
- Display top candidates using interactive metric cards.
- Visualize resume scores with a bar chart.
- User-friendly interface built with Streamlit.

## 🛠 Technologies Used
- **Python**  
- **Streamlit** for UI  
- **PyPDF2** for PDF text extraction  
- **scikit-learn** for TF-IDF and cosine similarity  
- **pandas** for data manipulation  
- **matplotlib** and **seaborn** for data visualization  

## 📂 File Structure
```
.
├── app.py          # Main application file
├── README.md       # Project documentation
```

## 🖥️ How to Run the Project
1. Clone this repository:
   ```bash
   git clone https://github.com/Ayushk3001/-AI-powered-Resume-Screening-and-Ranking-System
   ```
2. Navigate to the project directory:
   ```bash
   cd -AI-powered-Resume-Screening-and-Ranking-System
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## 📋 Dependencies
Add the following to a `requirements.txt` file:
```
streamlit
PyPDF2
pandas
scikit-learn
matplotlib
seaborn
```
