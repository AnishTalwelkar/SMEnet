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



# In[3]:


L_SME = pd.read_csv("Datasets/L_SME.csv")



# In[4]:


H_SME = pd.read_csv("Datasets/H_SME.csv")



# In[5]:


### check the custom list created in mockaroo. nashik and nagpur should be higher



# In[ ]:





# ### Best approach
# Find out similar users -- Find out for which jobs they have applied -- suggest those job to the other users who shared similar user profile.
# We are finding put similar user profile based on their degree type, majors and total years of experience.
# 
# We will get to 10 similar users.
# We will find our which are the jobs for which these users have applied
# We take an union of these jobs and recommend the jobs all these user base

# ##### USERBASED

# In[10]:


user_based_approach = L_SME


# In[11]:


user_based_approach['Location'] = user_based_approach['Location'] + user_based_approach['Sector'] + str(user_based_approach['No. of employees being laid off'])


# In[12]:





# In[13]:


tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(user_based_approach['Location'])


# In[14]:





# In[15]:


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)


# In[16]:





# In[17]:


user_based_approach = user_based_approach.reset_index()
userid = user_based_approach['L_id']
indices = pd.Series(user_based_approach.index, index=user_based_approach['L_id'])


# In[18]:


def get_recommendations_userwise(userid):
    idx = indices[userid]
    #print (idx)
    sim_scores = list(enumerate(cosine_sim[idx]))
    #print (sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    user_indices = [i[0] for i in sim_scores]
    #print (user_indices)
    return user_indices[0:11]


# In[23]:


def get_job_id(usrid_list):
    jobs_userwise = Applications['L_id'].isin(usrid_list) 
    df1 = pd.DataFrame(data = Applications[jobs_userwise], columns=['H_id'])
    joblist = df1['H_id'].tolist()
    Job_list = H_SME['H_id'].isin(joblist) 
    df_temp = pd.DataFrame(data = H_SME[Job_list], columns=['H_id','Company Name','Sector','Location','Start date','End date','No. of employees required'])
    return df_temp


# In[25]:


a = get_job_id(get_recommendations_userwise(ID))
st.write(a)


