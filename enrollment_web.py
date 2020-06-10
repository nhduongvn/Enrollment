import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
@st.cache
def load_data(nrows):
  data = pd.read_csv('Data/school_district_ed_enrollment.csv')
  return data

dat = load_data(10000)

st.header('Predict economic disadvantage student enrollment for Boston metro school districts')
st.subheader('test')
district_name = st.text_input("District name", "")
ed_pre = dat.loc[(dat['district']==district_name) & (dat['schoolyear']=='2018-19')]['ed_li_pct_pred']
if district_name != "":
  st.write('Percentage of enrolled economic disadvantage students is: ' + str(ed_pre.values[0]) + '%')
  #dat.loc[dat['district']==district_name].plot.bar(x='schoolyear',y='ell_pct')
  st.write('Percentage of enrolled economic disadvantage over year: ')
  dat.loc[dat['district']==district_name].plot(x="schoolyear", y=["ed_li_pct", "ed_li_pct_pred"], kind="bar")
  st.pyplot()
