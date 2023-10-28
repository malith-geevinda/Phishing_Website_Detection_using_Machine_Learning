import streamlit as st
import subprocess
import os
import joblib

from url_feature_extraction import featureExtraction
import pandas as pd

feature_names = ['length_url', 'ip', 'nb_at', 'https_token', 'nb_subdomains',
                 'prefix_suffix', 'shortening_service', 'nb_redirection',
                 'nb_external_redirection', 'iframe', 'onmouseover', 'right_clic',
                 'web_traffic', 'dns_record']



# Check if joblib is installed, and if not, install it
try:
    import joblib
except ImportError:
    st.write("Installing joblib...")
    subprocess.check_call(["pip", "install", "joblib"])
    st.write("joblib installed successfully. Please restart the app.")

# Function to load models from the models directory with added debugging information
def load_models():
    models = {}
    models_directory = 'models'  # Models are saved in the 'models' directory adjacent to the Streamlit script

    # Model file names
    model_file_names = [
        'Decision Tree_model.pkl',
        'Multilayer Perceptrons_model.pkl',
        'Random Forest_model.pkl',
        'SVM_model.pkl',
        'XGBoost_model.pkl'
    ]

    # Load each model using joblib
    for model_file in model_file_names:
        model_path = f'models/{model_file}'
        # Check if the model file exists
        if not os.path.exists(model_path):
            st.error(f"The model file '{model_path}' does not exist.")
            continue

        # Extract model name from the file name (remove "_model.pkl" and convert underscores to spaces)
        model_name = model_file.replace('_model.pkl', '').replace('_', ' ')

        # Load the model
        try:
            models[model_name] = joblib.load(model_path)

            #st.success(f"Successfully loaded model '{model_name}' from path '{model_path}'.")

            #st.success(f"Successfully loaded model '{model_name}' from path '{model_path}'.")

        except Exception as e:
            st.error(f"Error loading model '{model_name}' from path '{model_path}': {e}")

    return models

models = load_models()





st.title('Phish Defender: Shielding You from Phishing Threats')




with st.expander("What is Phish Defender ?"):
    

    st.write("""
## Welcome to the Phishing Website Detection Tool!
This tool allows you to input a website URL to determine whether it might be a potential phishing site. 
Our system uses advanced machine learning algorithms to analyze various features of the provided URL 
and predict its legitimacy.

Simply enter the URL in the input box below and click on 'Check!' to get the results.

**Note**: Always exercise caution when browsing the internet and avoid entering personal information 
on suspicious websites. This tool is meant to aid in detection and is not a definitive measure of a website's legitimacy.

Enjoy your safe browsing!
""")

    st.subheader('Data set')
    st.write('Dataset Link- _"https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset/data"_ ')
    st.write('Data set was updated last in  2022.')

with st.expander('EXAMPLE PHISHING URLs:'):
    st.write('_https://faceebook-com.bugs3.com/login/Secured_Re-login/index1.html_')
    st.write('_login[.]microsoftonline.ccisystems[.]us_')
    st.write('_https://jwqgvofh.site/keells-bx/? t=1618650506429_')
    st.caption('REMEMBER, PHISHING WEB PAGES HAVE SHORT LIFECYCLE!' )
    
# User selects a model
choice = st.selectbox("Please select your machine learning model",
                     ['Decision Tree', 'Random Forest', 'Multilayer Perceptrons', 'XGBoost', 'SVM'])

st.write(f'{choice} is selected')

# Check if a URL is phishing or legitimate





# Check if a URL is phishing or legitimate

url = st.text_input('Enter the URL')
if st.button('Check!'):
    # Load the selected model
    selected_model = models[choice]

    try:
        # Extract features from the URL
        url_features = featureExtraction(url)
        
        # Ensure the extracted features match the expected number of features
        if len(url_features) != len(feature_names):
            st.error(f"Feature mismatch! Expected {len(feature_names)} features but got {len(url_features)}")
            st.stop()  # Stop execution
        
        # Convert to DataFrame
        df = pd.DataFrame([url_features], columns=feature_names)
        
        # Make prediction using the selected model
        result = selected_model.predict(df.values)

        if result == 0:
            st.success("This web page seems legitimate!")
        else:
            st.warning("Attention! This web page is a potential phishing site!")
    except Exception as e:
        st.error(f"An error occurred while processing the URL: {e}")

