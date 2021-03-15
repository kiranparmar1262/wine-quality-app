import pickle

import streamlit as st

pickle_in = open('model.pkl', 'rb') 
classifier = pickle.load(pickle_in)

@st.cache
def prediction(residualsugar, freesulfurdioxide, chlorides, volatileacidity,alcohol):   
 
    # Pre-processing user input      
    
    # Making predictions 
    prediction = classifier.predict([[residualsugar, freesulfurdioxide, chlorides, volatileacidity,alcohol]])
    
    
    if prediction == 0:
        pred = 'Not Good'
    else:
        pred = "Good"
    return pred
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:black;border-radius: 10px;
  padding: 14px">
    <h1 style ="color:white;text-align:center;">Wine Quality Prediction App</h1> 
    </div> 
    """
    
    page_bg_img = '''

    <style>
    body {
    
    background-image: url("");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
   
    #st.image('houseprice.jpg')  
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True)   
    # following lines create boxes in which user can enter data required to make prediction 
    
#     Gender = st.selectbox('Gender',("Male","Female"))      this is for drop down box
#     Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    residualsugar = st.number_input("Residualsugar")
    freesulfurdioxide = st.number_input("Freesulfurdioxide")
    chlorides = st.number_input("Chorides")
    volatileacidity = st.number_input("Volatileacidity")
    alcohol = st.number_input("Alcohol")
    result = ""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"):
        result = prediction(residualsugar, freesulfurdioxide, chlorides, volatileacidity,alcohol)
        st.success('Wine Quality is {}'.format(result))
     
if __name__=='__main__': 
    main()
