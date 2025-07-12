Cover Letter Generator
A web-based application that generates personalized cover letters by analyzing your CV and job descriptions using OpenAI's GPT model.

Features
Smart Analysis: Analyzes your CV and job requirements to create tailored content
Easy Interface: Simple web interface built with Streamlit
Personalized Output: Generates cover letters that highlight relevant skills and experience
Error Handling: Graceful error handling with user-friendly messages
Setup
Clone the repository

git clone https://github.com/yourusername/cover-letter-generator.git
cd cover-letter-generator
Install dependencies

pip install -r requirements.txt
Set up OpenAI API key

Create a new file called .env in the project root directory
Add your OpenAI API key to this file:
OPENAI_API_KEY=your_actual_api_key_here
Get your API key from https://platform.openai.com/account/api-keys
Make sure your OpenAI account has billing set up
Run the application

streamlit run app.py
Usage
Open the application in your browser
Paste your CV content in the first text area
Paste the job description in the second text area
Click "Generate Cover Letter"
Review and copy your personalized cover letter
Requirements
Python 3.7+
OpenAI API key
Internet connection
Dependencies
streamlit
openai
python-dotenv
Note
This application uses OpenAI's API, which requires billing setup. Each cover letter generation costs a few cents.

