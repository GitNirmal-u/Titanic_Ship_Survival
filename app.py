import pandas as pd
import base64
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
import streamlit as st
import joblib
from PIL import Image
import requests

def set_background_image(image_url):
    page_bg_css = f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
        }}
        .title, .intro-text, .caption, .number-input input, .slider, .widget-dropdown label, .widget-dropdown select {{
            color: white !important; /* Set text color to white */
        }}
        </style>
    """
    st.markdown(page_bg_css, unsafe_allow_html=True)






def main():

  # Loading random forest classifier:
 model = joblib.load(r"D:\Machine_Learning_Projects\Titanic_Prediction_Project\RandomForestClassifier.pkl")

  # Loading the dataset:
 data = pd.read_csv(r"D:\Machine_Learning_Projects\Titanic_Prediction_Project\titanic_train.csv")

  # designing our web application:
  # # Setting the title and introduction text

 st.title("Titanic ShipWreck Survival Prediction")
 st.write("Enter the passenger details to predict survival:")

  # Creating input fields for user to enter passenger details

#  PassengerId = st.number_input('PassengerId')
 pclass = st.selectbox('Passenger Class', [1, 2, 3])
 sex = st.selectbox('Sex', ['male', 'female'])
 age = st.slider('Age', 0, 100, 25)
 sibsp = st.slider('Number of Siblings/Spouses Aboard', 0, 10, 0)
 parch = st.slider('Number of Parents/Children Aboard', 0, 10, 0)
 fare = st.slider('Fare', 0, 600, 50)
 embarked = st.selectbox('Embarked',['S','Q','C'])
 # creating the input data frame structure:
 input_data = pd.DataFrame(columns=['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked'])
  # Creating a button for prediction:
 if st.button('Predict Survival'):
    # Creating a new dataframe with the input values
    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Sex': [sex],
        'Age': [age],
        'SibSp': [sibsp],
        'Parch': [parch],
        'Fare': [fare],
        'Embarked':[embarked]
    })
    
  # Label Encoding and Scaling down using MinMaxScaler:

 encoder = LabelEncoder()

 input_data['Sex'] = encoder.fit_transform(input_data['Sex'])
 input_data['Embarked']= encoder.fit_transform(input_data['Embarked'])

  # Scaling down cols:
 if input_data.shape[0]>0:
    scaler= MinMaxScaler()
    input_data_scaled = pd.DataFrame(scaler.fit_transform(input_data))
    # Make the prediction:
    prediction = model.predict(input_data_scaled)

  # Display the prediction result
    if prediction == 0:
       st.write('Prediction: Did not survive')
    else:
       st.write('Prediction: Survived')
 else:
     st.write('Please provide valid input data.')

    
if __name__== '__main__':
    img_url = "https://w0.peakpx.com/wallpaper/569/844/HD-wallpaper-rms-titanic-background-wreck-fantasy-boat-marine-shipwreck-1912-titanic-iceberg-british-water-ship-tragedy-passenger-liner.jpg"
    set_background_image(img_url)
    main()
    