# import pckgs
import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from statistics import mean


st.title('TBD')
st.text('Work hard... Play hard')

data = st.file_uploader("Upload a Dataset", type=["csv"])


if data is not None:
    df = pd.read_csv(data)

    l_values = df.loc[df['staircase_loop.intensity'].isna() == False, 'staircase_loop.intensity'].reset_index(drop=True)

    def reversals(l_values):
    l_reversals = []
    
    if len(l_values) < 3:
        return l_reversals
    
    asc = False
    desc = True
    
    for el, el_after in zip(l_values[:-1], l_values[1:]):
        if (asc and el_after < el) or (desc and el_after > el):
            desc, asc = asc, desc
            l_reversals.append(el)
    return l_reversals

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('List values')
            st.write(l_values)

        with col2:

            st.subheader('Plot')
            fig, ax = plt.subplots()
            ax.plot(l_values.index.to_list(), l_values )
            st.pyplot(fig)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('List of reversal values')
            new_df = pd.DataFrame(reversals(l_values))
            st.write(new_df)

        with col2:
            st.subheader('Mean of last reversals')
            st.write(f'Last two = {mean(reversals(l_values)[-2:])}')
            st.write(f'Last three = {mean(reversals(l_values)[-3:])}')
            st.write(f'Last four = {mean(reversals(l_values)[-4:])}')
            
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            l_mistakes = df.loc[df['staircase_loop.response'].isna() == False, ['CorrectAns', 'staircase_loop.response']].reset_index(drop=True)
            st.subheader('List Answers')
            st.write(l_mistakes)

        with col2:
            st.subheader('Total incorrect answers')
            st.write(l_mistakes[l_mistakes['staircase_loop.response'] == 0].value_counts())

    with st.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            total_t_trial = df['entrainement1.thisRepN'].loc[df['entrainement1.thisRepN'].isna() == False].count()
            st.subheader('Total Training Trials')
            st.title(total_t_trial)
        
        with col3:
            total_s_trial = df['staircase_loop.thisTrialN'].loc[df['staircase_loop.thisTrialN'].isna() == False].count()
            st.subheader('Total Staircase Trials')
            st.title(total_s_trial)