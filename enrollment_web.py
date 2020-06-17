import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
@st.cache
def load_data(nrows):
  data = pd.read_csv('Data/predictionTest.csv')
  return data

dat = load_data(10000)
dat.sort_values(by=['district'],ascending=True,inplace=True)
district_name_all = dat['district'].values
district_name_all_list = list(set(district_name_all))
district_name_all_list.sort()
district_name_all_list.insert(0,"")
print(district_name_all_list)


st.header('Budget planning for economically disadvantaged students in Massachusetts school districts')
st.subheader('Introduction')
st.write('At the begining of each school year (October 1), school districts make a budget plan for the next school year. A foundation budget is created which is the minimum funding required for each school district. Based on this foundation budget, the state and local administrators will provide needed funding for school districts. The foundation budget also includes additional funding for school districts to support economically disadvantaged students (ED, ~$3500 per student). The current number of enrolled students seen by Oct. 1 is used to calculate the foundation budget, which is often lower than the actual number of ED students in the next school year. This tool provides better budget planning for ED students using realistic enrollment projection.')
st.subheader('Instruction')
st.write('Select the school district on the sidebar menu to see the projected budget')
st.subheader('Budget amount')
#district_name = st.text_input("District name", "")
district_name = st.sidebar.selectbox("District name", district_name_all_list)
#ed_pre = dat.loc[(dat['district']==district_name) & (dat['schoolyear']=='2018-19')]['ed_li_pct_pred']
ed_pre = dat.loc[(dat['district']==district_name) & (dat['schoolyear']=='2020-21')]['bg_ed_only']
print(dat.loc[(dat['district']==district_name) & (dat['schoolyear']=='2020-21')]['bg_ed_only'])
if district_name != "":
  #st.write('Budget amount for ED students in 2020-2021: $' + str(ed_pre.values[0]))
  #dat.loc[dat['district']==district_name].plot.bar(x='schoolyear',y='ell_pct')
  #st.write('Percentage of enrolled economic disadvantage over year: ')
  ax = dat.loc[dat['district']==district_name].plot(x="schoolyear", y=['bg_norm','bg_with_ed'], kind="barh")
  ax.legend(['Budget without additional ED support','Budget with ED support'])
  ax.set_xlabel('Budget amount ($1M)')
  ax.set_ylabel('School year')
  st.pyplot()
