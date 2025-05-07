code 
![image](https://github.com/user-attachments/assets/4d5aaf80-5e95-4ff4-ab48-0c429f886083

output
![image](https://github.com/user-attachments/assets/d81ddf8d-5100-4d50-94ff-a87df242a114)
 explanation: 
 import streamlit as st
→ This imports the Streamlit library and allows you to use its features using the st prefix.

st.title("Hello, Streamlit!")
→ Displays a large title at the top of the web app that says "Hello, Streamlit!".

st.header("🎯 Objective: Understand basic components")
→ Shows a bold header below the title with a description of the app's objective, including an emoji.

name = st.text_input("Enter your name:")
→ Creates a text input box labeled "Enter your name:", and stores what the user types in the variable name.

age = st.number_input("Enter your age:", min_value=0, max_value=120)
→ Creates a number input box for age (between 0 and 120), storing the value in the variable age.

if name:
→ Checks if the user has entered something in the name field (i.e., it’s not empty).

st.write(f"👋 Hello, {name}!")
→ If a name was entered, this displays a personalized greeting using the name.

if age:
→ Checks if the user has entered an age (non-zero), and then executes the next line.

st.write(f"🎂 You are {int(age)} years old.")
→ Displays the user’s age, converting it to an integer to remove decimal points.

