import streamlit as st
import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
#from scipy import stats
#from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity

st.title('Here are some companies for you!')

ID = st.sidebar.number_input('Enter your ID', value=2)

Applications = pd.read_csv("Datasets/Applications.csv")
H_SME = pd.read_csv("Datasets/H_SME.csv")
L_SME = pd.read_csv("Datasets/L_SME.csv")

user_based_approach = L_SME

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(user_based_approach['Location'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

user_based_approach = user_based_approach.reset_index()
userid = user_based_approach['L_id']
indices = pd.Series(user_based_approach.index, index=user_based_approach['L_id'])

def get_recommendations_userwise(userid):
    idx = indices[userid]
    #print (idx)
    sim_scores = list(enumerate(cosine_sim[idx]))
    #print (sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    user_indices = [i[0] for i in sim_scores]
    #print (user_indices)
    return user_indices[0:11]

def get_job_id(usrid_list):
    jobs_userwise = Applications['L_id'].isin(usrid_list) 
    df1 = pd.DataFrame(data = Applications[jobs_userwise], columns=['H_id'])
    joblist = df1['H_id'].tolist()
    Job_list = H_SME['H_id'].isin(joblist) 
    df_temp = pd.DataFrame(data = H_SME[Job_list], columns=['H_id','Company name','Sector','Location','Start date','End date','No. of employees required'])
    return df_temp

a = get_job_id(get_recommendations_userwise(ID))
st.write(a)

