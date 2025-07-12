import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env variables

client = OpenAI(api_key=api_key)

st.title("Cover Letter Generator")

cv_text = st.text_area("Paste your CV or Resume here")

job_description = st.text_area("Paste the job description here")

if st.button("Generate Cover Letter") and cv_text and job_description:
    with st.spinner("Generating cover letter..."):
        try:
            prompt = f"""
You are a professional cover letter writer. Based on the following CV and job description, write a personalized cover letter that highlights the candidate's strengths and suitability for the role.

CV:
{cv_text}

Job Description:
{job_description}

Cover Letter:
"""
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=600
            )

            cover_letter = response.choices[0].message.content
            
            st.subheader("Generated Cover Letter")
            st.write(cover_letter)
            
        except Exception as e:
            st.error(f"Error generating cover letter: {str(e)}")
            st.info("Please check your OpenAI API key and try again.")
else:
    st.warning("Please paste both your CV and the job description.")
