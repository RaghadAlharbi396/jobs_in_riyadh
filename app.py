import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Load the data
jobs_data = pd.read_csv('clean_job_data.csv')

# Custom styling for Streamlit app using inline CSS
st.markdown("""
    <style>
        /* Background Color */
        body {
            background-color: #fff3e2;  /* App background */
        }
        /* Container Background Color */
        .css-18e3th9 {
            background-color: #f5f5f5;  /* Light background color for containers */
            padding: 2rem;
            border-radius: 12px;
        }
        /* Title and header text color */
        h1, h3 {
            color: #80a3ec;  /* Text color */
        }
        /* Button style */
        .stButton>button {
            background-color: #003366;
            color: white;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("""
<div style="display: flex; align-items: center; justify-content: space-between; direction: rtl;">
    <h2 style="margin-right: 10px;">هل الرياض هي أرض الأحلام لحديثي التخرج؟</h2>
    <img src="https://cdn.alweb.com/thumbs/travel/article/fit710x532/ما-هي-مميزات-مدينة-الرياض.jpg" 
         alt="الرياض" width="120" height="120" style="border-radius: 8px; margin-left: 10px;">
</div>
""", unsafe_allow_html=True)



# Intro
st.markdown('<p style="text-align:right" dir="rtl">الحمد لله، تخرجت من الجامعة، لكن لم أجد وظيفة حتى الآن. والكل يقول لي إن الرياض هي المكان الذي سأجد فيه وظيفة الأحلام.</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:right" dir="rtl">لكن، هل هذا الكلام صحيح؟</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:right" dir="rtl">لقد تم جمع بيانات الوظائف المعلنة على منصة جدارات وحللتها لأرى إذا كانت الرياض هي أكثر مدينة تعلن عن وظائف لحديثي التخرج.</p>', unsafe_allow_html=True)

# Section: Region Chart
st.markdown('<h3 style="text-align:right" dir="rtl">هل الرياض هي المدينة الأكثر إعلانًا عن الوظائف؟</h3>', unsafe_allow_html=True)
region_counts = jobs_data['region'].value_counts().reset_index()
region_counts.columns = ['region', 'count']
fig = go.Figure(data=go.Bar(
    x=region_counts['count'],
    y=region_counts['region'],
    orientation='h',
    marker=dict(color='#9FB3DF')  # Bar color updated to match your request
))
fig.update_layout(
    title='توزيع إعلانات الوظائف حسب المدينة',
    xaxis_title='عدد الإعلانات',
    yaxis_title='المدينة',
    plot_bgcolor='white',
    font=dict(family="Cairo", size=14)
)
st.plotly_chart(fig, use_container_width=True)

st.markdown('<p style="text-align:right" dir="rtl">من خلال البيانات المتاحة، يبدو أن الرياض هي الأكثر في إعلانات الوظائف، حيث تمثل تقريبًا نصف إجمالي الإعلانات على "جدارات".</p>', unsafe_allow_html=True)

# Section: Gender
st.markdown('<h3 style="text-align:right" dir="rtl">هل هناك تمييز بين الجنسين في الوظائف المعلنة بالرياض؟</h3>', unsafe_allow_html=True)
jobs_in_riyadh = jobs_data[jobs_data['region'] == 'الرياض']
gender_counts = jobs_in_riyadh['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']
fig_gender = go.Figure(data=go.Bar(
    x=gender_counts['count'],
    y=gender_counts['gender'],
    orientation='h',
    marker=dict(color='#9FB3DF')  # Bar color updated to match your request
))
fig_gender.update_layout(
    title='توزيع الوظائف حسب الجنس في الرياض',
    xaxis_title='عدد الإعلانات',
    yaxis_title='الجنس',
    plot_bgcolor='white',
    font=dict(family="Cairo", size=14)
)
st.plotly_chart(fig_gender, use_container_width=True)
st.markdown('<p style="text-align:right" dir="rtl">من خلال التحليل، يتضح أنه لا يوجد تمييز بين الجنسين، حيث تركز الجهات في الرياض على المهارات والكفاءات أكثر من التركيز على جنس المتقدم.</p>', unsafe_allow_html=True)

# Section: Experience
st.markdown('<h3 style="text-align:right" dir="rtl">هل تفضل الجهات بالرياض أصحاب الخبرة أم حديثي التخرج؟</h3>', unsafe_allow_html=True)
jobs_in_riyadh['experience in years'] = pd.to_numeric(jobs_in_riyadh['experience in years'], errors='coerce')
jobs_in_riyadh['experience_category'] = jobs_in_riyadh['experience in years'].apply(lambda x: 'أصحاب خبرة' if x > 0 else 'حديثو التخرج')
experience_counts = jobs_in_riyadh['experience_category'].value_counts().reset_index()
experience_counts.columns = ['experience_category', 'count']
fig_experience = go.Figure(data=go.Bar(
    x=experience_counts['count'],
    y=experience_counts['experience_category'],
    orientation='h',
    marker=dict(color='#9FB3DF')  # Bar color updated to match your request
))
fig_experience.update_layout(
    title='الفئة المطلوبة في الوظائف: خبرة أم حديثو التخرج؟',
    xaxis_title='عدد الإعلانات',
    yaxis_title='الفئة',
    plot_bgcolor='white',
    font=dict(family="Cairo", size=14)
)
st.plotly_chart(fig_experience, use_container_width=True)
st.markdown('<p style="text-align:right" dir="rtl">يظهر التمثيل أن أكثر من نصف الوظائف المعلنة في الرياض لحديثي التخرج، ربما لأنهم يملكون أفكارًا جديدة وحماسًا عاليًا للعمل.</p>', unsafe_allow_html=True)

# Section: Salary Distribution
st.markdown('<h3 style="text-align:right" dir="rtl">ما هو متوسط رواتب حديثي التخرج بالرياض؟</h3>', unsafe_allow_html=True)
fresh_graduates = jobs_in_riyadh[jobs_in_riyadh['experience in years'] == 0].copy()
fresh_graduates['Salary'] = pd.to_numeric(fresh_graduates['Salary'], errors='coerce')
fresh_graduates = fresh_graduates.dropna(subset=['Salary'])
fig_salary = px.histogram(
    fresh_graduates,
    x='Salary',
    nbins=20,
    color_discrete_sequence=['#9FB3DF']  # Bar color updated to match your request
)
fig_salary.update_layout(
    title='توزيع الرواتب للخريجين الجدد في الرياض',
    xaxis_title='الراتب (ريال سعودي)',
    yaxis_title='عدد الإعلانات',
    plot_bgcolor='white',
    font=dict(family="Cairo", size=14)
)
st.plotly_chart(fig_salary, use_container_width=True)
st.markdown('<p style="text-align:right" dir="rtl">متوسط الرواتب لحديثي التخرج في الرياض من 4000 إلى 5000 ريال بالشهر، لكن السؤال: هل يكفي هذا الراتب للعيش؟</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:right" dir="rtl">بحسب دراسة من منصة سكن، فإن تكلفة المعيشة للفرد شهريًا تتراوح بين 3000 و5000 ريال سعودي.</p>', unsafe_allow_html=True)

# Final Summary
st.markdown("""<p style="text-align:right" dir="rtl">بعد مراجعة هذه البيانات، يمكننا القول إن الرياض تُعد أرض الأحلام للخريجين الجدد. فهي الأكثر في عدد الإعلانات، ولا يوجد تمييز جنسي، وتقدّم العديد من الفرص لاكتساب الخبرة.</p>""", unsafe_allow_html=True)

# Search by job title
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:right" dir="rtl">يمكنك الآن البحث عن متوسط الراتب حسب المسمى الوظيفي</h3>', unsafe_allow_html=True)
fresh_grads_riyadh = jobs_in_riyadh[jobs_in_riyadh['experience in years'] == 0].copy()
fresh_grads_riyadh['Salary'] = pd.to_numeric(fresh_grads_riyadh['Salary'], errors='coerce')
fresh_grads_riyadh = fresh_grads_riyadh.dropna(subset=['Salary'])
job_titles = sorted(fresh_grads_riyadh['job_title'].dropna().unique())
selected_title = st.selectbox('🔍 اختر المسمى الوظيفي:', job_titles)
filtered_jobs = fresh_grads_riyadh[fresh_grads_riyadh['job_title'] == selected_title]

if not filtered_jobs.empty:
    avg_salary = filtered_jobs['Salary'].mean()
    st.markdown(
        f'<p style="text-align:right; font-size:18px;" dir="rtl">📊 متوسط الراتب لمسمى <strong>{selected_title}</strong> في الرياض هو <strong>{avg_salary:,.0f} ريال سعودي</strong>.</p>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<p style="text-align:right" dir="rtl">عذرًا، لا توجد بيانات حالية لهذا المسمى الوظيفي.</p>',
        unsafe_allow_html=True
    )
