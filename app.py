#general imports
import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

hide_streamlit_style = """
                <style>
                div[data-testid="stToolbar"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                div[data-testid="stStatusWidget"] {
                visibility: hidden;
                height: 0%;
                position: fixed;
                }
                #MainMenu {
                visibility: hidden;
                height: 0%;
                }
                header {
                visibility: hidden;
                height: 0%;
                }
                footer {
                visibility: hidden;
                height: 0%;
                }
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.title("Smhyal")
st.subheader("Supporting Mental Health via. AI Learning")
st.markdown("""Smhyal is an all-in-one tool for rapid self-diagnosis for two of the most common, yet critical, psychological disorders among young adults: anxiety and depression.""")

#sidebar information
with st.sidebar:
  st.header("FAQ")
  st.markdown("""
  Education:
  - If you are under 18 years of age: current grade level for school (if attended in the past three months) or highest level ever attended (if not attended within the past three months
  - If you are at or above 18 years of age: Highest level of educational attended, whether currently in school or not""")
  st.markdown("""
  Race:
  - American Indian/Alaska Native: Origins in any of the original people of North America and South America (including Central America) and who maintain tribal affiliation or community attachment
  - Asian: Origins in Far East, Indian subcontinent, or Southeast Asia; primarily includes Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam
  - Black or African American:  Origins in any of the Black racial groups of Africa
  - Native Hawaiian or Other Pacific Islander: Origins in any of the original people of Hawaii, Guam, Samoa, or other Pacific Islands
  - White: A person having origins in any of the original people of Europe, the Middle East, or North Africa""")
  st.markdown("""
  Ethnicity:
  - Mexican: Of Mexican origin, regardless of race
  - Puerto Rican: Of Puerto Rican origin, regardless of race
  - Other Hispanic or Latino origin: Of known Central or South American or any other Spanish cultural origin (including Spain), other than Puerto Rican or Mexican, regardless of race""")
  st.markdown("""
  Martial Status:
  - Never married: If you are single or whose only marriage was annulled
  - Now married: If you are married, living together as married, living with partners, or cohabitating
  - Separated: If you are legally separated or otherwise absent from your spouse because of marital discord""")
  st.markdown("""
  Employment Status:
  - Full-time: Includes those under full-time employment, usually working for 30 or more hours per week
  - Not in the labor force: Not employed and not actively looking for work during the past 30 days (i.e. you are not interested in work or you have been discouraged to look for work)""")
  st.markdown("""
  Residential Status
  - Homeless: Those who have no fixed address, including homeless shelters
  - Private residence: Includes those who live independently, dependently (living in a house, apartment, or other similar dwellings and are heavily dependent on others for daily living assistance), and those under the age of 18 years living in a private residence, regardless of living arrangement
  - Other: Those living in a foster home or a care center, residential care facility, crisis residence, institutional care facility, jail and/or correctional facility, or other residential status
  """)

  st.header("Additional Information")
  st.markdown("""The Smhyal algorithm is based on a modified version of an artificial neural network (ANN), with accuracies greater than 94% for  anxiety and depression diagnosis. The model was trained on large-scale data for young adults from the publicly-available Substance Abuse and Mental Health Service Administration (SAMHSA) MH-CLD survey dataset. The algorithm was created by Avi Verma, under the guidance of Dr. Kaustubh Supekar at Stanford University. We hope that Smyhal will help in postively impact young adults by counteracting the underdiagnosis of anxiety and depression.""")
  st.markdown("""None of the data entered in the form or the diagnosis outputs are ever stored or traced.""")
  
#importing models
mod1 = load_model('depression.h5')
mod2 = load_model('anxiety.h5')
li = [0]*9
#taking inputs
with st.expander("Age"):
  twoage = st.checkbox('12-14 years old')
  threeage = st.checkbox('15-17 years old')
  fourage = st.checkbox('18-20 years old')
  fiveage = st.checkbox('21-24 years old')
li[0]=st.number_input('Age',min_value=0)
with st.expander("Education"):
  oneedu = st.checkbox('Special education')
  twoedu = st.checkbox('6th grade to 8th grade')
  threeedu = st.checkbox('9th grade to 11th grade')
  fouredu = st.checkbox('12th grade or pursuing GED')
li[1] = st.number_input('Education',min_value=0)
with st.expander("Ethnicity"):
  oneethnic = st.checkbox('Mexican')
  twoethnic = st.checkbox('Puerto Rican')
  threeethnic = st.checkbox('Other Hispanic or Latino origin')
  fourethnic = st.checkbox('Not of Hispanic or Latino origin')
li[2] = st.number_input('Ethnic',min_value=0)
with st.expander("Race"):
  onerace = st.checkbox('American Indian/Aslaka Native')
  tworace = st.checkbox('Asian')
  threerace = st.checkbox('African or African-American')
  fourrace = st.checkbox('Native Hawaiian or Pacific Islander')
  fiverace = st.checkbox('White')
  sixrace = st.checkbox('Some other race alone, or two or more races')
li[3] = st.number_input('Race',min_value=0)
with st.expander("Gender"):
  onerace = st.checkbox('Male')
  tworace = st.checkbox('Female')
li[4] = st.number_input('Gender',min_value=-10,value=0)
with st.expander("Marital Status"):
  onemarried = st.checkbox('Never married')
  twomarried = st.checkbox('Now married')
  threemaried = st.checkbox('Seperated')
  fourseperated = st.checkbox('Divorced')
li[5] = st.number_input('Marital',min_value=0)
with st.expander("Serious Emotional/Stressor Disturbance (SED)"):
  twoop1SED = st.checkbox("An inability to learn that cannot be explained by intellectual, sensory, or health factors")
  twoop2SED = st.checkbox("An inability to build or maintain satisfactory interpersonal relationships with peers and teachers")
  twoop3SED = st.checkbox("Inappropriate types of behavior or feelings under normal circumstances")
  twoop4SED = st.checkbox("A general pervasive mood of unhappiness, recurrent every one or two weeks")
  twoop5SED = st.checkbox("A tendency to develop physical symptoms or fears associated with personal or school problems")
  threeSED = st.checkbox(" None of the above symptoms")
li[6] = st.number_input('SED',min_value=0)
with st.expander("Employment"):
  oneemploy = st.checkbox("Full-time")
  twoemploy = st.checkbox("Part-time")
  fouremploy = st.checkbox("Unemployed")
  fiveemploy = st.checkbox("Not in labor force")
li[7] = st.number_input('Employment',min_value=0)
with st.expander("Residential"):
  tworesi = st.checkbox("Private residence")
  oneresi = st.checkbox("Homeless")
  threeresi = st.checkbox("Other residential status")
li[8] = st.number_input('Residential',min_value=0)

def predict_mh(new_x_example):
  new_example_reshaped = np.asarray(li).reshape((1, 9))
  my_new_prediction = mod1.predict(new_example_reshaped)
  print(my_new_prediction)
  depression = -1
  if (my_new_prediction.flatten()[0] > 0.4):
    depression = 1
  else:
    depression = 0

  my_new_prediction_a = mod2.predict(new_example_reshaped)
  print(my_new_prediction_a.flatten()[0])
  anxiety = -1
  if (my_new_prediction_a.flatten()[0] > 0.4):
    anxiety = 1
  else:
    anxiety = 0

  prediction_dict = {'Depression':depression, "Anxiety":anxiety}
  return prediction_dict

bt = st.button('Your Results:')
if bt:
  dic = predict_mh(li)
  if dic.get('Depression') == 0 and dic.get('Anxiety') == 0:
    st.write("You are predicted to neither be depressed nor anxious.")
  if dic.get('Depression') == 1 and dic.get('Anxiety') == 0:
    st.write('You are predicted to be depressed, but not anxious. It is recommended that you consult a psychiatrist.')
  if dic.get('Depression') == 0 and dic.get('Anxiety') == 1:
    st.write('You are predicted to be anxious, but not depressed. It is recommended that you consult a psychiatrist.')
  if dic.get('Depression') == 1 and dic.get('Anxiety') == 1:
    st.write('You are predicted to be anxious and depressed. It is highly recommended that you consult psychiatrist.')
