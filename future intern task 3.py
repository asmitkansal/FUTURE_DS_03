#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\asmit\Downloads\student_feedback.csv")


# In[4]:


# top 5 rows
df.head()


# In[5]:


#bottom 5 rows
df.tail()


# In[6]:


#total no of rows and columns
df.shape


# In[7]:


#info about the Data types and the non null Count
df.info()


# In[8]:


#checking nulls
df.isnull().sum()


# In[9]:


# showing total count of rows, mean values, STD, MIN, MAX
df.describe()


# In[10]:


# checking duplicates
df.duplicated().sum()


# In[11]:


#unique values in different columns 
df.nunique()


# In[12]:


df.drop(columns = {"Unnamed: 0"}, inplace = True)


# In[13]:


df.rename(columns={"Well versed with the subject": "Satisfaction Score"}, inplace = True)


# In[14]:


df.rename(columns={"Explains concepts in an understandable way": "Concepts Explaination"}, inplace = True)
df.rename(columns={"Use of presentations": "Presentation Use"}, inplace = True)
df.rename(columns={"Degree of difficulty of assignments": "Assignment Difficulty"}, inplace = True)
df.rename(columns={"Solves doubts willingly": "Doubts Solving"}, inplace = True)
df.rename(columns={"Structuring of the course": "Course Structuring"}, inplace = True)
df.rename(columns={"Provides support for students going above and beyond": "Student Supports"}, inplace = True)
df.rename(columns={"Course recommendation based on relevance": "Course Recommendation"}, inplace = True)


# In[32]:


df.head()


# In[16]:


def rate_to_sentiment(score):
    if score <= 3:
        return "Negative"
    elif score <= 6:
        return "Neutral"
    else:
        return "Positive"

rating_columns = ["Satisfaction Score", "Concepts Explaination", "Doubts Solving", "Student Supports"]  # add all relevant columns
for col in rating_columns:
    df[f"{col}_Sentiment"] = df[col].apply(rate_to_sentiment)


# In[17]:


df.head()


# In[18]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[19]:


cols = [
    "Satisfaction Score",
    "Concepts Explaination",
    "Presentation Use",
    "Assignment Difficulty",
    "Doubts Solving",
    "Course Structuring",
    "Student Supports",
    "Course Recommendation"
]

avg_scores = df[cols].mean()



# In[20]:


avg_scores.plot(kind='bar', color='orange')
plt.title("Average Feedback Scores")
plt.xlabel("Score")
plt.tight_layout()
plt.show()


# In[26]:


import plotly.graph_objects as go

scores = [8.5, 9.0, 7.5, 6.0, 8.0, 7.0, 8.8, 9.2]

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=scores,
    theta=cols,
    mode='lines+markers',
    fill='toself',
    name='Feedback Score',
    hoverinfo='text',
    text=[f"{label}: {score}" for label, score in zip(cols, scores)]
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(visible=True, range=[0, 10])
    ),
    showlegend=False,
    title='Course Feedback Radar Chart'
)

fig.show()


# In[37]:


sns.histplot(df['Satisfaction Score'], bins=10, kde=True, color='red')
plt.title('Distribution of Student Satisfaction Scores')
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')
plt.show()


# In[39]:


features = ['Concepts Explaination', 'Presentation Use', 'Assignment Difficulty',
            'Doubts Solving', 'Course Structuring', 'Student Supports', 'Course Recommendation']

correlations = df[features + ['Satisfaction Score']].corr()['Satisfaction Score'][features]
correlations.sort_values().plot(kind='barh', color='orchid')
plt.title('Feature Correlation with Satisfaction')
plt.xlabel('Correlation Coefficient')
plt.show()


# In[40]:


sentiment_cols = ['Satisfaction Score_Sentiment', 'Concepts Explaination_Sentiment', 
                  'Doubts Solving_Sentiment', 'Student Supports_Sentiment']

for col in sentiment_cols:
    sentiment_counts = df[col].value_counts()
    sentiment_counts.plot(kind='bar', color='goldenrod')
    plt.title(f'{col} Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.show()


# In[ ]:





# In[ ]:




