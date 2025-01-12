import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from tensorflow.keras.models import load_model
model=load_model('model.h5')

def predict_note_authentication(Month1,Month2,Month3,Month4,Month5,Month6,Month7,Month8,Month9,Month10,ExRate1,ExRate2,ExRate3,ExRate4,ExRate5,ExRate6,ExRate7,ExRate8,ExRate9,ExRate10):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    lst = [[Month1, ExRate1], [Month2, ExRate2],[Month3, ExRate3],[Month4, ExRate4],[Month5, ExRate5],[Month6, ExRate6],[Month7, ExRate7],[Month8, ExRate8],[Month9, ExRate9],[Month10, ExRate10]]
    df = pd.DataFrame(lst, columns =['Lead Price', 'USD/INR Exchange Rate'])
    lead_unscaled=df['Lead Price'].tolist()
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler(feature_range=(0,1))
    scaler = scaler.fit(df)
    data_scaled = scaler.transform(df)
    data_scaled=data_scaled.reshape(1,data_scaled.shape[0],data_scaled.shape[1]) #(samples,past days, number of features)
    forecast = model.predict(data_scaled) #forecast 
    element=forecast[0]
    element= np. reshape(element, (element.shape[0], 1))
    forecast_copies = np.repeat(element, 2, axis=1)
    y_pred_future = scaler.inverse_transform(forecast_copies)
    #extracting required column from 2 repeated columns
    y_pred=[] 
    for arr in y_pred_future:
        y_pred.append(arr[0])
    y_pred= np.array(y_pred)
    
    #prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(y_pred)
    return y_pred




def main():
    st.title("Prediction of Average Lead Prices for next 5 months")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Prediction of Lead Prices ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Month1 = st.text_input("Average Price in Month 1","Type Here")
    Month2 = st.text_input("Average Price in Month 2","Type Here")
    Month3 = st.text_input("Average Price in Month 3","Type Here")
    Month4 = st.text_input("Average Price in Month 4","Type Here")
    Month5 = st.text_input("Average Price in Month 5","Type Here")
    Month6 = st.text_input("Average Price in Month 6","Type Here")
    Month7 = st.text_input("Average Price in Month 7","Type Here")
    Month8 = st.text_input("Average Price in Month 8","Type Here")
    Month9 = st.text_input("Average Price in Month 9","Type Here")
    Month10 = st.text_input("Average Price in Month 10","Type Here")
    ExRate1 = st.text_input("Average value of USD in Month 1","Type Here")
    ExRate2 = st.text_input("Average value of USD in Month 2","Type Here")
    ExRate3 = st.text_input("Average value of USD in Month 3","Type Here")
    ExRate4 = st.text_input("Average value of USD in Month 4","Type Here")
    ExRate5 = st.text_input("Average value of USD in Month 5","Type Here")
    ExRate6 = st.text_input("Average value of USD in Month 6","Type Here")
    ExRate7 = st.text_input("Average value of USD in Month 7","Type Here")
    ExRate8 = st.text_input("Average value of USD in Month 8","Type Here")
    ExRate9 = st.text_input("Average value of USD in Month 9","Type Here")
    ExRate10 = st.text_input("Average value of USD in Month 10","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Month1,Month2,Month3,Month4,Month5,Month6,Month7,Month8,Month9,Month10,ExRate1,ExRate2,ExRate3,ExRate4,ExRate5,ExRate6,ExRate7,ExRate8,ExRate9,ExRate10)
    st.success('Average Lead Prices for next 5 months: {}'.format(result))
    if st.button("About"):
        #st.text("Lets LEarn")
        st.text("Built with Streamlit")



if __name__=='__main__':
    main()