#general imports
import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

st.title("Smhyal")
st.markdown("""Supporting Mental Health via. AI Learning""")

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
  - Full-time: Includes those in full-time employment
  - Not in the labor force: Not employed and not actively looking for work during the past 30 days (i.e. you are not interested in work or you have been discouraged to look for work)""")
  st.markdown("""
  Residential Status
  - Homeless: Those who have no fixed address, including homeless shelters
  - Private residence: Includes those who live independently, dependently (living in a house, apartment, or other similar dwellings and are heavily dependent on others for daily living assistance), and those under the age of 18 years living in a private residence, regardless of living arrangement
  - Other: Those living in a foster home or a care center, residential care facility, crisis residence, institutional care facility, jail and/or correctional facility, or other residential status
  """)
  
  st.subheader("Supporting Mental Health in Youth via. AI Learning, or Smhyal, is an all-in-one tool for simple self-diagnosis for two of the most common, yet critical, psychological disorders among youth: anxiety and depression.")
  st.subheader("The Smhyal algorithm is based on a modified version of an artificial neural network (ANN), with an accuracy of more than 94% anxiety and depression diagnosis. The model was trained on the data for young adults from the publicly-available Substance Abuse and Mental Health Service Administration (SAMHSA) MH-CLD survey dataset. The algorithm was created by Avi Verma, under the guidance of Dr. Kaustubh Supekar at Stanford University. We hope that Smyhal will positively impact young adults by counteracting the underdiagnosis of anxiety and depression.")
  st.subheader("None of the data entered in the form or the diagnosis outputs are ever stored or traced.")
  
#importing models
mod1 = load_model('depression.h5')
mod2 = load_model('anxiety.h5')
li = [0]*9
#taking inputs
with st.expander("Age"):
  st.markdown("""
- 12-14 years → 2
- 15-17 years → 3
- 18-20 years → 4
- 21-24 years → 5""")
li[0]=st.number_input('Age',min_value=0)
with st.expander("Education"):
  st.markdown("""
- Special education → 1
- 6th grade to 8th grade → 2
- 9th grade to 11th grade → 3
- 12th grade (or pursuing GED) → 4""")
li[1] = st.number_input('Education',min_value=0)
with st.expander("Ethnicity"):
  st.markdown("""
- Mexican → 1
- Puerto Rican → 2
- Other Hispanic or Latino Origin → 3
- Not of Hispanic or Latin Origin → 4""")
li[2] = st.number_input('Ethnic',min_value=0)
with st.expander("Race"):
  st.markdown("""
- American Indian/Alaska Native → 1
- Asian → 2
- African or African-American → 3
- Native Hawaiian or Pacific Islander → 4
- White → 5
- Some other race alone, or two or more races → 6""")
li[3] = st.number_input('Race',min_value=0)
with st.expander("Gender"):
  st.markdown("""
- Male → 1
- Female → 2""")
li[4] = st.number_input('Gender',min_value=-10,value=0)
with st.expander("Marital Status(ranges and values)"):
  st.markdown("""
- Never married → 1
- Now married → 2
- Separated → 3
- Divorced → 4""")
li[5] = st.number_input('Marital',min_value=0)
with st.expander("Serious Emotional/Stressor Disturbance (SED)"):
  st.markdown("""
- An inability to learn that cannot be explained by intellectual, sensory, or health factors → 2
- An inability to build or maintain satisfactory interpersonal relationships with peers and teachers → 2
- Inappropriate types of behavior or feelings under normal circumstances → 2
- A general pervasive mood of unhappiness or depression → 2
- A tendency to develop physical symptoms or fears associated with personal or school problems → 2
- None of the above symptoms → 3""")
li[6] = st.number_input('SED',min_value=0)
with st.expander("Employment"):
  st.markdown("""
- Full-time → 1
- Part-time → 2
- Unemployed → 4
- Not in the labor force → 5""")
li[7] = st.number_input('Employment',min_value=0)
with st.expander("Residential(ranges and values)"):
  st.markdown("""
- Homeless → 1
- Private Residence → 2
- Other → 3
""")
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
