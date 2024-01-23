Visit PhishDefender - https://phishdefender.streamlit.app/

PhishDefender is a web application developed to detect phishing websites using Machine Learning techniques. This application is designed to help users identify potentially harmful websites and protect themselves from online phishing threats. The application analyzes the content of a given website and classifies it as either legitimate or phishing based on the patterns identified by Machine Learning models.

Features
Content-Based Analysis: PhishDefender focuses on content-based analysis, examining the structure and elements of web pages to identify phishing attempts.

Multiple Machine Learning Models: The application utilizes various Machine Learning algorithms, including Decision Trees, Random Forest, Support Vector Machines (SVM), XGBoost, and Neural Networks, to achieve accurate website classification.

User-Friendly Interface: PhishDefender provides an intuitive user interface where users can enter a website URL and quickly receive the phishing classification results.

How It Works
User Input: Users enter a website URL into the application interface.
Content Analysis: The application extracts and analyzes the content of the provided website using predefined features.
Machine Learning Classification: The extracted features are fed into Machine Learning models, which classify the website as legitimate or phishing.
Classification Result: The application displays the classification result to the user, indicating whether the website is safe or potentially harmful.
Usage
To run the application locally, follow these steps:

Clone the repository:

git clone <repository-url>
cd PhishDefender
Install dependencies:

pip install -r requirements.txt
Run the application:

streamlit run app.py
Access the application in your web browser at http://localhost:8501.

Technologies Used
Python: Programming language used for backend development and Machine Learning model training.

Streamlit: Python library used for building the web application user interface.

Machine Learning Libraries: Various Python libraries like Scikit-learn and XGBoost were used for developing Machine Learning models.
