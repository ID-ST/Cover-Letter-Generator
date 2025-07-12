Blank Python Project
Overview
This is a blank Python project with a basic Streamlit setup. The project is ready for development of a web-based cover letter generator that will analyze CVs and job descriptions to create personalized cover letters.

System Architecture
The application will follow a modular architecture with clear separation of concerns:

Frontend: Streamlit web interface for user interaction
Text Processing: NLTK-based text analysis and processing (to be implemented)
Business Logic: Separate modules for text analysis and cover letter generation (to be implemented)
No Database: The application operates entirely in memory without persistent storage
Key Components
1. Main Application (app.py)
Purpose: Entry point and UI layer
Technology: Streamlit
Current State: Basic Streamlit app with placeholder content
2. Text Analyzer (to be created)
Purpose: Will analyze and process text content from CVs and job descriptions
Planned Features:
Skill extraction using regex patterns
Education level detection
Experience parsing
Text cleaning and normalization
NLTK integration for tokenization and POS tagging
3. Cover Letter Generator (to be created)
Purpose: Will generate personalized cover letters based on analysis results
Planned Features:
Match score calculation between CV and job requirements
Dynamic content generation based on match score
Structured letter formatting (header, opening, body, closing)
Personalization with company and position details
Data Flow (Planned)
Input Collection: User provides CV text and job description through Streamlit interface
Text Analysis: Both texts are processed to extract skills, experience, and requirements
Match Calculation: Algorithm calculates compatibility score between CV and job requirements
Letter Generation: Cover letter is generated with appropriate tone and content based on match score
Output: Formatted cover letter is presented to the user
External Dependencies
Core Libraries
Streamlit: Web application framework for the user interface
NLTK: Natural language processing library for text analysis (installed, ready to use)
punkt tokenizer
stopwords corpus
averaged_perceptron_tagger
Text Processing Features (Planned)
Regex-based skill and experience extraction
Pattern matching for education levels
Stop word filtering
Tokenization and POS tagging
Deployment Strategy
The application is designed for simple deployment:

Platform: Replit-compatible Python environment
Dependencies: Standard Python packages (streamlit, nltk)
Data: NLTK data automatically downloaded on first run
Configuration: Streamlit configuration already set up
Changelog
July 12, 2025. Successfully resolved OpenAI API key authentication issues - app now fully functional
July 10, 2025. Updated to OpenAI API v1.0+ format and added error handling
July 10, 2025. User created cover letter generator with OpenAI integration
July 10, 2025. Installed python-dotenv and openai dependencies
July 05, 2025. Project reset to blank state with basic Streamlit setup
User Preferences
Preferred communication style: Simple, everyday language. User built cover letter generator from scratch using OpenAI API. User has OpenAI account with billing set up and $5 credit.

