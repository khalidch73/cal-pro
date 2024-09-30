1. Set up Poetry for Dependency Management
```bash 
poetry new my_streamlit_project
cd my_streamlit_project
```
2. Configure the Project and Install Dependencies
In the project directory, open the pyproject.toml file, which holds the project configuration.

Install Streamlit as a dependency using Poetry:

``` bash
poetry add streamlit
```
3. Create a Simple Streamlit Application
Inside the my_streamlit_project directory, you can create a streamlit_app.py file. This will contain your Streamlit app code. For example:
```bash
import streamlit as st

# Streamlit app prototype
st.title("My Streamlit Prototype")

st.write("Welcome to your Streamlit app powered by Poetry!")

# You can add more interactive elements
if st.button('Click me'):
    st.write("Button clicked!")

number = st.slider('Pick a number', 0, 10)
st.write(f"You selected: {number}")
```
4. Run Your Streamlit App

```bash 
cd my_streamlit_project
```

```bash 
poetry run streamlit run streamlit_app.py
```
5. deploy on streamliit

https://pro-cal.streamlit.app/
