# import pckgs
import streamlit as st
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from statistics import mean
import csv
import tempfile


title_1 = '<p style="font-family:Courier; color:Black; font-size: 60px; font-weight:bold;">Psychopy Data Reader</p>'
st.markdown(title_1, unsafe_allow_html=True)
st.text('Work hard... Play hard')

data = st.file_uploader("Upload a Dataset", type=["csv"])
results = []

if data is not None:
    df = pd.read_csv(data) 

    with st.container():
        subtitle_1 = '<p style="font-family:Courier; color:Black; font-size: 40px; font-weight:bold;">Stage 1 = Training</p>'
        st.markdown(subtitle_1, unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            
            s1_trials = df['key_resp.keys'].loc[df['key_resp.keys'].isin(['right', 'left']) ].count()
            st.subheader(f'Total Trials \n {str(s1_trials)}') 

            s1_answers = df.loc[df['key_resp.keys'].isin(['right', 'left']), ['key_resp.keys', 'key_resp.corr']]
            st.subheader('List Answers')
            st.write(s1_answers)

            s1_errors = s1_answers[s1_answers['key_resp.corr'] == 0].value_counts()
            st.subheader('Total incorrect answers')
            st.write(s1_errors)
        results.append([{'training_trials' : s1_trials} , {'training_answers' : s1_answers }, {'training_incorrect' : s1_errors}])


    with st.container():
        subtitle_2 = '<p style="font-family:Courier; color:Black; font-size: 40px; font-weight:bold;">Stage 2 = No noise</p>'
        st.markdown(subtitle_2, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:

            s2_r1_trials = df['nonoise1_rep.keys'].loc[df['nonoise1_rep.keys'].isin(['right', 'left']) ].count()
            s2_r1_answers = df.loc[df['nonoise1_rep.keys'].isin(['right', 'left']), ['nonoise1_rep.keys', 'nonoise1_rep.corr']]
            s2_r1_errors = s2_r1_answers[s2_r1_answers['nonoise1_rep.corr'] == 0].value_counts()

            subheader_1 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">Round 1</p>'
            st.markdown(subheader_1, unsafe_allow_html=True)
            
            st.subheader(f'Total Trials \n {str(s2_r1_trials)}') 

            st.subheader('List Answers')
            st.write(s2_r1_answers)

            st.subheader('Total incorrect answers')
            st.write(s2_r1_errors)


        with col2:
            if 'nonoise2_rep.keys' in df:
                s2_r2_trials = df['nonoise2_rep.keys'].loc[df['nonoise2_rep.keys'].isin(['right', 'left']) ].count()
                s2_r2_answers = df.loc[df['nonoise2_rep.keys'].isin(['right', 'left']), ['nonoise2_rep.keys', 'nonoise2_rep.corr']]
                s2_r2_errors = s2_r2_answers[s2_r2_answers['nonoise2_rep.corr'] == 0].value_counts()

                if int(s2_r2_trials) > 1:

                    subheader_2 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">Round 2</p>'
                    st.markdown(subheader_2, unsafe_allow_html=True)
                    
                    st.subheader(f'Total Trials \n {str(s2_r2_trials)}') 

                    st.subheader('List Answers')
                    st.write(s2_r2_answers)

                    st.subheader('Total incorrect answers')
                    st.write(s2_r2_errors)
                else: 
                    subheader_3 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">No Repetition needed</p>'
                    st.markdown(subheader_3, unsafe_allow_html=True)
            else:
                subheader_3 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">No Repetition needed</p>'
                st.markdown(subheader_3, unsafe_allow_html=True)
    
        with col3:
            if 'nonoise3_rep.keys' in df:
                s2_r3_trials = df['nonoise3_rep.keys'].loc[df['nonoise3_rep.keys'].isin(['right', 'left']) ].count()
                s2_r3_answers = df.loc[df['nonoise3_rep.keys'].isin(['right', 'left']), ['nonoise3_rep.keys', 'nonoise3_rep.corr']]
                s2_r3_errors = s2_r3_answers[s2_r3_answers['nonoise3_rep.corr'] == 0].value_counts()

                if int(s2_r3_trials) > 1:

                        subheader_4 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">Round 3</p>'
                        st.markdown(subheader_4, unsafe_allow_html=True)
                        
                        st.subheader(f'Total Trials \n {str(s2_r3_trials)}') 

                        st.subheader('List Answers')
                        st.write(s2_r3_answers)

                        st.subheader('Total incorrect answers')
                        st.write(s2_r3_errors)
                else: 
                    subheader_5 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">No Repetition needed</p>'
                    st.markdown(subheader_5, unsafe_allow_html=True)
            else: 
                subheader_5 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">No Repetition needed</p>'
                st.markdown(subheader_5, unsafe_allow_html=True)

    with st.container():
        subtitle_3 = '<p style="font-family:Courier; color:Black; font-size: 40px; font-weight:bold;">Stage 3 = Noise</p>'
        st.markdown(subtitle_3, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)

        with col1:

            s3_r1_trials = df['noise1_rep.keys'].loc[df['noise1_rep.keys'].isin(['right', 'left']) ].count()
            s3_r1_answers = df.loc[df['noise1_rep.keys'].isin(['right', 'left']), ['noise1_rep.keys', 'noise1_rep.corr']]
            s3_r1_errors = s3_r1_answers[s3_r1_answers['noise1_rep.corr'] == 0].value_counts()

            subheader_6 = '<p style="font-family:Courier; color:Black; font-size: 24px; font-weight:bold;">Round 1</p>'
            st.markdown(subheader_6, unsafe_allow_html=True)
            
            st.subheader(f'Total Trials \n {str(s3_r1_trials)}') 

            st.subheader('List Answers')
            st.write(s3_r1_answers)

            st.subheader('Total incorrect answers')
            st.write(s3_r1_errors)


    with st.container():
        subtitle_4 = '<p style="font-family:Courier; color:Black; font-size: 40px; font-weight:bold;">Stage 4 = Staircase</p>'
        st.markdown(subtitle_4, unsafe_allow_html=True)

        l_values = df.loc[df['staircase_loop.intensity'].isna() == False, 'staircase_loop.intensity'].reset_index(drop=True)
        r_values = df.loc[df['staircase_loop.response'].isna() == False, 'staircase_loop.response'].reset_index(drop=True)

        def reversals(l_values):
            '''function to calculate reversal happening on the staircaise'''
            l_reversals = []
            if len(l_values) < 3:
                return l_reversals
        
            # an initial state/trend is defined
            asc = False
            desc = True

            for idx, (key, value) in enumerate(zip(l_values, r_values)):
                if idx == 0 and value == 0: #We change inital state if first answer is wrong
                    asc = True
                    desc = False
                if idx == len(l_values) -1: #Final trial is always a reversal
                    l_reversals.append([idx, key, value])
                elif (asc and l_values[idx+1] < l_values[idx]) or (desc and l_values[idx+1] > l_values[idx]): #a trend and then if a value goes agains the trend is considered reversal and the state of trend is changed
                    desc, asc = asc, desc
                    l_reversals.append([idx, key, value])
            return l_reversals   
        
        col1, col2 = st.columns(2)
        col = ['staircase_loop.thisTrialN', 'staircase_loop.intensity', 'staircase_loop.response']
        new_df = pd.DataFrame(reversals(l_values), columns=col)

        with col1:
            st.subheader('Full staircase')
            st.write(df.loc[df['staircase_loop.response'].isna() == False, ['staircase_loop.intensity','CorrectAns','staircase_loop.response']].reset_index(drop=True))
        
        with col2:
            total_s_trial = df['staircase_loop.thisTrialN'].loc[df['staircase_loop.thisTrialN'].isna() == False].count()
            st.subheader(f'Total Staircase Trials = {total_s_trial}')
            fig, ax = plt.subplots()
            ax.plot(l_values.index.to_list(), l_values )
            st.pyplot(fig)

    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('List of reversal values')
            st.dataframe(new_df)

        with col2:
            st.subheader('Mean of last reversals')
            st.write(f'Last two = {mean([i[1] for i in reversals(l_values)][-2:])}')
            st.write(f'Last three = {mean([i[1] for i in reversals(l_values)][-3:])}')
            st.write(f'Last four = {mean([i[1] for i in reversals(l_values)][-4:])}')

    
            st.subheader('Total incorrect answers')
            staircase_answers = df.loc[df['staircase_loop.response'].isna() == False, ['CorrectAns','staircase_loop.response']].reset_index(drop=True)
            st.write(staircase_answers[staircase_answers['staircase_loop.response'] == 0.0].value_counts())
    with st.container():
        results_df = pd.DataFrame(results)
        with tempfile.NamedTemporaryFile(mode='w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['training_trials', 'training_answers', 'training_incorrect'])
