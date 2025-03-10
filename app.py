import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import time  # For progress bar
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        extracted_text = page.extract_text()
        if extracted_text:  # Ensure non-empty text
            text += extracted_text + "\n"
    return text

# Function to rank resumes based on job description
def rank_resumes(job_description, resumes):
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents).toarray()
    job_description_vector = vectors[0]
    resume_vectors = vectors[1:]
    cosine_similarities = cosine_similarity([job_description_vector], resume_vectors).flatten()
    return cosine_similarities

# Streamlit UI
st.set_page_config(page_title="Resume Ranking", layout="wide")

st.title("📄 AI Resume Screening & Candidate Ranking System")
st.write("Upload resumes and rank them based on the given job description.")

# Job description input
st.header("📝 Job Description")
job_description = st.text_area("Enter the job description", height=150)

# File uploader
st.header("📂 Upload Resumes")
uploaded_files = st.file_uploader("Upload multiple PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_description:
    st.header("📊 Ranking Resumes")
    
    resumes = []
    progress_bar = st.progress(0)  # Progress bar initialization
    
    for idx, file in enumerate(uploaded_files):
        text = extract_text_from_pdf(file)
        resumes.append(text)
        progress_bar.progress((idx + 1) / len(uploaded_files))  # Update progress bar

    # Rank resumes
    scores = rank_resumes(job_description, resumes)

    # Prepare results
    results = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", ascending=False)

    # Display top scores in metric cards
    st.subheader("🏆 Top Candidates")
    top_resumes = results.head(3)  # Top 3 candidates
    col1, col2, col3 = st.columns(3)

    for i, row in enumerate(top_resumes.itertuples(), start=1):
        if i == 1:
            col1.metric(label=row.Resume, value=f"{row.Score:.2f}")
        elif i == 2:
            col2.metric(label=row.Resume, value=f"{row.Score:.2f}")
        else:
            col3.metric(label=row.Resume, value=f"{row.Score:.2f}")

    # Display DataFrame
    st.subheader("📜 Full Ranking List")
    st.write(results)

    # Bar chart for visualization
    st.subheader("📊 Resume Scores Visualization")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=results["Score"], y=results["Resume"], hue=results["Resume"], palette="coolwarm", ax=ax, legend=False)
    ax.set_xlabel("Similarity Score")
    ax.set_ylabel("Resume Name")
    ax.set_title("Resume Ranking by AI")
    st.pyplot(fig)
