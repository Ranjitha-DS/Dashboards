import pandas as pd
import streamlit as st
import seaborn as sns

def titlemsg():
    st.title("FCE Model Monitoring")
def write():
    st.title("Segment Wise Performance")
    st.markdown("Welcome! Please select from the filters in the sidebar to the left of your screen to narrow down your search within the log analysis tool.")

    df = pd.read_csv(r'C:\Users\ranjitha_scienaptic\Downloads\FCE1.csv',index_col=False)
    df['FCE%'] = df['FCE%'].str.rstrip("%").astype(float)/100*100
    df['Collection Efficiency'] = df['Collection Efficiency'].str.rstrip("%").astype(float)/100*100
    df['Resolution'] = df['Resolution'].str.rstrip("%").astype(float)/100*100
    df['AWS'] = df['AWS'].str.rstrip("%").astype(float)/100*100
    fce_1=df['#FCE'].tail(1)
    fce_perc_1=df['FCE%'].tail(1)
    coll_3 = df['Collection Efficiency'].tail(1)
    res_4 = df['Resolution'].tail(1)
    aws_5 = df['AWS'].tail(1)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("#FCE", "873", "4%")
    col2.metric("FCE%", "100 %", "4%")
    col3.metric("Collection Efficiency", "30%", "-4%")
    col4.metric("Resolution", "68 %", "2%")
    col5.metric("AWS", "57 %", "-8%")
    df = df.iloc[:-1 , :]
    selected_options =[]
    # log table for the app...
    #st.dataframe(df)
    options = df['FCE Segment'].unique().tolist()
    selected_options = st.sidebar.multiselect('Which Segment do you want?',options)
    print(len(selected_options))
    filtered_df = df[df['FCE Segment'].isin(selected_options)]
    if(len(selected_options)==0):
        #st.dataframe(filtered_df)
        cm = sns.palplot(sns.color_palette("BuGn_r", 10))
        hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
        st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
        df1 = df.head(3)
        st.dataframe(df.style
        .background_gradient(cmap='RdYlGn', subset=(df.index[0:6],['Collection Efficiency','Resolution','AWS']))
        .set_properties(subset=['Collection Efficiency','Resolution','AWS']))
    else:
        st.dataframe(filtered_df)

def write1():
    st.title("Decile Wise Performance")
    st.markdown("Welcome! Please select from the filters in the sidebar to the left of your screen to narrow down your search within the log analysis tool.")

    df = pd.read_csv(r'C:\Users\ranjitha_scienaptic\Downloads\Decile.csv',index_col=False)
    df['FCE%'] = df['FCE%'].str.rstrip("%").astype(float)/100*100
    df['Collection Efficiency'] = df['Collection Efficiency'].str.rstrip("%").astype(float)/100*100
    df['Resolution'] = df['Resolution'].str.rstrip("%").astype(float)/100*100
    df['AWS'] = df['AWS'].str.rstrip("%").astype(float)/100*100
    fce_1=df['#FCE'].tail(1)
    fce_perc_1=df['FCE%'].tail(1)
    coll_3 = df['Collection Efficiency'].tail(1)
    res_4 = df['Resolution'].tail(1)
    aws_5 = df['AWS'].tail(1)
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("#FCE", "873", "4%")
    col2.metric("FCE%", "100 %", "4%")
    col3.metric("Collection Efficiency", "30%", "-4%")
    col4.metric("Resolution", "68 %", "2%")
    col5.metric("AWS", "57 %", "-8%")
    df = df.iloc[:-1 , :]
    selected_options =[]
    # log table for the app...
    #st.dataframe(df)
    options = df['Decile'].unique().tolist()
    selected_options = st.sidebar.multiselect('Which Decile do you want?',options)
    print(len(selected_options))
    filtered_df = df[df['Decile'].isin(selected_options)]
    if(len(selected_options)==0):
        #st.dataframe(filtered_df)
        cm = sns.palplot(sns.color_palette("BuGn_r", 10))
        hide_dataframe_row_index = """
            <style>
            .row_heading.level0 {display:none}
            .blank {display:none}
            </style>
            """
        st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
        #df1 = df.head(3)
        st.dataframe(df.style
        .background_gradient(cmap='RdYlGn', subset=(df.index[0:9],['Collection Efficiency','Resolution','AWS']))
        .set_properties(subset=['Collection Efficiency','Resolution','AWS']))

    else:
        st.dataframe(filtered_df)