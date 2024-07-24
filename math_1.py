import streamlit as st 

st.title("Digits")

a=st.text_input(label="Enter the value")
if st.button("cllick"):
    try:
        
        for i in range(len(a)):
            if a[i].isdigit():
                st.write(a[i])
    except InterruptedError:
        st.write("Error while calculating")
            
           
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
