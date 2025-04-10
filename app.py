import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Load the data
jobs_data = pd.read_csv('clean_job_data.csv')


# Title in RTL
st.markdown('<h1 style="text-align:right" dir="rtl">هل الرياض هي أرض الأحلام لحديثي التخرج؟</h1>', unsafe_allow_html=True)

# First paragraph in RTL
st.markdown('<p style="text-align:right" dir="rtl">الحمد لله، تخرجت من الجامعة، لكن لم أجد وظيفة حتى الآن. والكل يقول لي إن الرياض هي المكان الذي سأجد فيه وظيفة الأحلام.</p>', unsafe_allow_html=True)

# Another paragraph in RTL
st.markdown('<p style="text-align:right" dir="rtl">لكن، هل هذا الكلام صحيح؟</p>', unsafe_allow_html=True)

# More paragraphs in RTL
st.markdown('<p style="text-align:right" dir="rtl">لقد تم جمع بيانات الوظائف المعلنة على منصة جدارات وحللتها لأرى إذا كانت الرياض هي أكثر مدينة تعلن عن وظائف لحديثي التخرج.</p>', unsafe_allow_html=True)

# Another question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">هل الرياض هي المدينة الأكثر إعلانًا عن الوظائف؟</h3>', unsafe_allow_html=True)
# Aggregate data by region
region_counts = jobs_data['region'].value_counts().reset_index()
region_counts.columns = ['region', 'count']

# Create the Plotly bar chart
fig = go.Figure(data=go.Bar(
    x=region_counts['count'],
    y=region_counts['region'],
    orientation='h',
    marker=dict(color='#B0C4DE')
))

# Customize the chart layout
fig.update_layout(
    xaxis_title='Job Postings Count',
    yaxis_title='Region',
    plot_bgcolor='white'
)

# Display the chart in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Continue with the rest of the Streamlit content
st.markdown('<p style="text-align:right" dir="rtl">من خلال البيانات المتاحة، يبدو أن الرياض هي الأكثر في إعلانات الوظائف، حيث تمثل تقريبًا نصف إجمالي الإعلانات على "جدارات".</p>', unsafe_allow_html=True)

# Gender discrimination question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">هل هناك تمييز بين الجنسين في الوظائف المعلنة بالرياض؟</h3>', unsafe_allow_html=True)
# Filter for Riyadh
jobs_in_riyadh = jobs_data[jobs_data['region'] == 'الرياض']

# Aggregate data by gender
gender_counts = jobs_in_riyadh['gender'].value_counts().reset_index()
gender_counts.columns = ['gender', 'count']

# Create Plotly bar chart
fig_gender = go.Figure(data=go.Bar(
    x=gender_counts['count'],
    y=gender_counts['gender'],
    orientation='h',
    marker=dict(color='#FFA07A')
))

# Customize layout
fig_gender.update_layout(
    xaxis_title='Job Postings Count',
    yaxis_title='Gender',
    plot_bgcolor='white'
)

# Display in Streamlit
st.plotly_chart(fig_gender, use_container_width=True)
# Analysis paragraph about gender in RTL
st.markdown('<p style="text-align:right" dir="rtl">من خلال التحليل، يتضح أنه لا يوجد تمييز بين الجنسين، حيث تركز الجهات في الرياض على المهارات والكفاءات أكثر من التركيز على جنس المتقدم.</p>', unsafe_allow_html=True)

# Experience preference question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">هل تفضل الجهات بالرياض أصحاب الخبرة أم حديثي التخرج؟</h3>', unsafe_allow_html=True)
# Categorize data into 'Experienced' and 'Fresh Graduate'
jobs_in_riyadh['experience_category'] = jobs_in_riyadh['experience in years'].apply(
    lambda x: 'Experienced' if int(x) > 0 else 'Fresh Graduate'
)

# Aggregate data
experience_counts = jobs_in_riyadh['experience_category'].value_counts().reset_index()
experience_counts.columns = ['experience_category', 'count']

# Create Plotly chart
fig_experience = go.Figure(data=go.Bar(
    x=experience_counts['count'],
    y=experience_counts['experience_category'],
    orientation='h',
    marker=dict(color='#ADD8E6')
))

# Customize layout
fig_experience.update_layout(
    xaxis_title='Job Postings Count',
    yaxis_title='Experience Level',
    plot_bgcolor='white'
)

# Display in Streamlit
st.plotly_chart(fig_experience, use_container_width=True)
st.markdown('<p style="text-align:right" dir="rtl"> .يظهر التمثيل ان اكثر من نصف الوظائف المعلنة في الرياض لحديثي التخرج، ممكن لان الكثير من الجهات تفضل حديثي التخرج لان حديثي التخرج لديهم الافكار الجديدة والروح الحماسية في العمل </p>', unsafe_allow_html=True)

# Final salary question in RTL
st.markdown('<h3 style="text-align:right" dir="rtl">ما هو متوسط رواتب حديثي التخرج بالرياض؟</h3>', unsafe_allow_html=True)
# Convert experience to numeric
jobs_in_riyadh['experience in years'] = pd.to_numeric(jobs_in_riyadh['experience in years'], errors='coerce')

# Filter fresh graduates
fresh_graduates = jobs_in_riyadh[jobs_in_riyadh['experience in years'] == 0].copy()

# Convert Salary to numeric
fresh_graduates['Salary'] = pd.to_numeric(fresh_graduates['Salary'], errors='coerce')
fresh_graduates = fresh_graduates.dropna(subset=['Salary'])

# Create histogram
fig_salary = px.histogram(
    fresh_graduates,
    x='Salary',
    nbins=20,
    color_discrete_sequence=['#B0C4DE']
)

fig_salary.update_layout(
    xaxis_title='Salary (SAR)',
    yaxis_title='Number of Job Postings',
    plot_bgcolor='white'
)

st.plotly_chart(fig_salary, use_container_width=True)

st.markdown('<p style="text-align:right" dir="rtl">متوسط الرواتب لحديثي التخرج في الرياض من 4000 الى 5000 بالشهر لكن السؤال هنا هل يكفي هذا الراتب للعيش بالرياض؟</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align:right" dir="rtl">بحسب دراسة اجرتها منصة سكن تظهر ان يمكن تقدير متوسط تكلفة المعيشة في السعودية للفرد الواحد خلال الشهر من 3000 إلى 5000 ريال سعودي شهرياً.</p>', unsafe_allow_html=True)

st.markdown("""<p style="text-align:right" dir="rtl">بعد مراجعة هذه البيانات، يمكننا أن نقول إن الرياض هي أرض الأحلام لحديثي التخرج. حيث إن معظم الوظائف المعلنة توجد في الرياض، ولا يوجد تمييز على أساس الجنس، مما يتيح الكثير من الفرص للخريجين الجدد. صحيح أن الراتب المتوقع قد لا يكون مرتفعًا جدًا، ولكن إذا أخذنا في الاعتبار العمل لمدة سنتين لاكتساب الخبرة، يمكننا بعدها البحث عن وظائف براتب أعلى.
</p>""", unsafe_allow_html=True)
st.markdown('<h3 style="text-align:right" dir="rtl">يمكنك الان البحث عن متوسط الراتب لحيثي التخرج بالرياض حسب المسمى الوظيفي  </h3>', unsafe_allow_html=True)
# Section title in Arabic
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:right" dir="rtl">اختر المسمى الوظيفي لمعرفة متوسط الرواتب في الرياض لحديثي التخرج </h3>', unsafe_allow_html=True)

# Make sure job titles are filtered only from Riyadh & fresh grads
jobs_in_riyadh['experience in years'] = pd.to_numeric(jobs_in_riyadh['experience in years'], errors='coerce')
fresh_grads_riyadh = jobs_in_riyadh[jobs_in_riyadh['experience in years'] == 0].copy()

# Clean salary column
fresh_grads_riyadh['Salary'] = pd.to_numeric(fresh_grads_riyadh['Salary'], errors='coerce')
fresh_grads_riyadh = fresh_grads_riyadh.dropna(subset=['Salary'])

# Get unique job titles
job_titles = sorted(fresh_grads_riyadh['job_title'].dropna().unique())

# User selects job title
selected_title = st.selectbox('اختر المسمى الوظيفي', job_titles, index=0)

# Filter based on selection
filtered_jobs = fresh_grads_riyadh[fresh_grads_riyadh['job_title'] == selected_title]

# Show average salary
if not filtered_jobs.empty:
    avg_salary = filtered_jobs['Salary'].mean()
    st.markdown(
        f'<p style="text-align:right" dir="rtl">متوسط الراتب لمسمى <strong>{selected_title}</strong> في الرياض هو تقريبًا <strong>{avg_salary:,.0f} ريال سعودي</strong>.</p>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<p style="text-align:right" dir="rtl">عذرًا، لا توجد بيانات حالية لهذا المسمى الوظيفي.</p>',
        unsafe_allow_html=True
    )


