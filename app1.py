# Date                                               
# Children apprehended and placed in CBP custody       
# Children in CBP custody                              
# Children transferred out of CBP custody             
# Children in HHS Care                               
# Children discharged from HHS Care 
 

import streamlit as st
import pandas as pd
import numpy as np
import openpyxl
import matplotlib.pyplot as plt

#from ydata_profiling import ProfileReport

#from data_profiling.profile_report import ProfileReport
import streamlit.components.v1 as components
import base64
from PIL import Image
import os
import plotly.express as px

#from sklearn.linear_model import LinearRegression
#from sklearn.model_selection import train_test_split

from statsmodels.tsa.statespace.sarimax import SARIMAX

st.set_page_config(page_title ='Healthcare Analytics Dashboard',layout="wide", initial_sidebar_state="expanded")
#--------------------------------------
#Page Background Color-->
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: lightblue;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
#--------------------------------------------
#st.markdown("""
#<style>

#/* Move page navigation downward */
#[data-testid="stSidebarNav"] {
#    padding-top: 20px;
#}

#/* Add icon + text together at top */
#[data-testid="stSidebarNav"]::before {
#    content: "HEALTHCARE Analytics";
#    white-space: pre-line;
#    display: block;
#    text-align: center;
#    font-size: 24px;
#    font-weight: 900 !important;
#    padding-top: 140px;
#    margin-bottom: 5px;

#    background-image: url("https://raw.githubusercontent.com/M339KUMAR/DataAnalytics1/main/MedPlus.jpg");
#    background-repeat: no-repeat;
#    background-position: top center;
#    background-size: 125px;
#}

#</style>
#""", unsafe_allow_html=True)

st.sidebar.markdown(
    """
    <div style="text-align:center;">
        <img src="https://raw.githubusercontent.com/M339KUMAR/DataAnalytics1/main/MedPlus.jpg" width="120">
        <h3>HEALTHCARE Analytics</h3>
    </div>
    """,
    unsafe_allow_html=True
)

#--------------------------------------------
#--------------------------------------
#Image Icons Display-->
image_path1 = "SScope.jpeg"
image_path2 = "graph_bar-chart.jpeg"

if os.path.exists(image_path1) & os.path.exists(image_path2):
    img1 = Image.open(image_path1)
    img1 = img1.resize((300, 150))
    img2 = Image.open(image_path2)
    img2 = img2.resize((300,150)) 
 
    # st.image([img1,img2] use_column_width=False)
    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        st.image(img1, use_column_width=True)
    with col2:
        st.image(img2, use_column_width=True)
    with col3:
        st.write("Health Care Data Analysis \n Helps to Understand the Present Data & \n Predict The Future Situation & Aiding The Healthcare Personnel to Plan Ahead To take necessary steps")
else:
    st.error(f"Image not found: {image_path}")
#--------------------------------------
#CSS Style Button-->
st.markdown("""
<style>
div.stButton > button {
    background-color: #1E88E5;
    color: white;
    border-radius: 15px;
    border: none;
    height: 50px;
    width: 100px;
    font-size: 20px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #1565C0;
}
</style>
""", unsafe_allow_html=True)
#--------------------------------------
#Metric Cards Customization-->
# CSS for colorful metric cards
st.markdown("""
<style>

/* Metric card styling */
div[data-testid="stMetric"] {
    background-color: #FFD1DC;
    padding: 20px;
    border-radius: 15px;
    border: 2px solid #FFB6C1;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
    text-align: center;
}

/* Metric label */
div[data-testid="stMetricLabel"] {
    color: #6A1B4D;
    font-size: 25px;
    font-weight: bold;
}

/* Metric value */
div[data-testid="stMetricValue"] {
    color: #C2185B;
    font-size: 32px;
    font-weight: bold;
}

/* Delta styling */
div[data-testid="stMetricDelta"] {
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)
#--------------------------------------

#df = pd.read_excel('/content/sample_data/HHS_Unaccompanied_Alien_Children_Program.xlsx')
df = pd.read_excel('HHS_Unaccompanied_Alien_Children_Program.xlsx', engine='openpyxl')

#st.title("Hello from Colab via ngrok")
#st.write("This works!")

#st.title("Unified Mentor") 

st.markdown("<h1 style='text-align: center;'>UNIFIED MENTOR</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Data Analytics Intern</h2>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'> Project-1: HEALTHCARE Analytics</h2>", unsafe_allow_html=True)
st.write("***📌US-HHS Unaccompanied Children Program  Dashboard***")

st.dataframe(df)

st.write("***EXPLORATORY DATA ANALYSIS***")
#try:
   #from ydata_profiling import ProfileReport
#   report = ProfileReport(df, explorative=True)
   # Save report
   #profile.to_file("report.html")
#   html = report.to_html()

   # Read HTML file
   #with open("report.html", "r", encoding="utf-8") as f:
   #     html = f.read()

   # Display in Streamlit
#   components.html(html, height=1000, scrolling=True)
#except ValueError: 
#   st.write("Issue in Report Generation:")
#finally :
st.write("Generating EDA Report..")

#st.dataframe(df['Date'])
st.title("📊 HHS Care System Dashboard")

col1, col2 = st.columns([2, 5])

with col1:
    # Create a Matplotlib figure
    #st.pyplot(fig)
    if st.button("Plot-1"):
       #fig, ax = plt.subplots()
       #ax.plot(df['Date'], df['Children in CBP custody'], color='orange', linestyle='--', label="Children in CBP Custody")
       #ax.set_title("Children in CBP Custody")
       #ax.set_xlabel("Date")
       #ax.set_ylabel("CBP Custidy")
       #ax.tick_params(axis='x', rotation=45)
       #ax.legend()
       #st.pyplot(fig)
       fig = px.line(
             df,
             x="Date",
             y="Children in CBP custody",
             markers=True,
             title="Children in CBP Custody"
             )

       fig.update_traces(
             line_color="orange",
             line_dash="dash"
             )

       fig.update_layout(
             xaxis_title="Date",
             yaxis_title="CBP Custody",
             hovermode="x unified"
             )

       st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write("Click the PLOT Button to Display the Date vs Children in CBP Custody Graph")

# Convert datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort from oldest to newest
df = df.sort_values(by='Date', ascending=True)

col1, col2 = st.columns([0.75, 5])

with col1:
 if st.button("Plot-2"):
   df['Cumulative_Load'] = df['Children in CBP custody'].cumsum()
   # -----------------------------
   # Plot
   # -----------------------------
   fig, ax = plt.subplots(figsize=(10, 5))
   ax.plot(
       df['Date'],
       df['Cumulative_Load'],
       color='cyan',
       linestyle='-.',
       label = "Cumsum of Children in CBP Custody"
   )
   ax.set_title("Cumulative Load Over Time")
   ax.set_xlabel("Date")
   ax.set_ylabel("Cumulative Load")
   ax.legend()
   # Rotate x-axis labels
   plt.xticks(rotation=45)
   st.pyplot(fig)

with col2:
    st.write("Click the PLOT Button to Display the CumSum of CBP Custody")

# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort chronologically
df = df.sort_values('Date')

# Create complete daily index
df = df.set_index('Date').asfreq('D')

# Missing values
df = df.fillna(0)

# Logical constraints
df['Anomaly_Flag'] = 0

df.loc[(df['Children transferred out of CBP custody'] > df['Children in CBP custody']), 'Anomaly_Flag'] = 1
df.loc[(df['Children discharged from HHS Care'] > df['Children in HHS Care']), 'Anomaly_Flag'] = 1

# Total system load
df['Total_Load'] = df['Children in CBP custody'] + df['Children in HHS Care']

# Net intake
df['Net_Intake'] = df['Children transferred out of CBP custody'] - df['Children discharged from HHS Care']

# Growth rate
#df['Growth_Rate'] = df['Total_Load'].pct_change() * 100
df['Growth_Rate'] = (
    df['Total_Load'].pct_change() * 100
).fillna(0)

#df['Growth_Rate'] = df['Total_Load'][-1]

# Backlog indicator
df['Backlog'] = (df['Net_Intake'] > 0).astype(int)

df['7_day_avg'] = df['Total_Load'].rolling(7).mean()
df['14_day_avg'] = df['Total_Load'].rolling(14).mean()

last_avg = df['Total_Load'].rolling(7).mean().iloc[-1]

days=30

future_dates = pd.date_range(start=df.index[-1], periods=days+1)[1:]

forecast_values = [last_avg] * days

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecast_Load': forecast_values
})

# Total Load
current_load = df['Total_Load'].iloc[-1]
previous_load = df['Total_Load'].iloc[-2]
load_delta = current_load - previous_load

# Net Intake
current_intake = df['Net_Intake'].iloc[-1]
previous_intake = df['Net_Intake'].iloc[-2]
intake_delta = (current_intake - previous_intake)

# Growth Rate
#current_growth = df['Growth_Rate'].iloc[-1]
#previous_growth = df['Growth_Rate'].iloc[-2]
#growth_delta = (current_growth - previous_growth)

current_load = df['Total_Load'].iloc[-1]

# Check if previous row exists
if len(df) > 1:
    previous_load = df['Total_Load'].iloc[-2]
else:
    previous_load = current_load

# Avoid divide-by-zero
if previous_load != 0:
    growth_rate = ((current_load - previous_load)/ previous_load) * 100
else:
    growth_rate = 0

# Backlog
current_backlog = df['Backlog'].sum()
previous_backlog = df['Backlog'].iloc[:-1].sum()
backlog_delta = (current_backlog- previous_backlog)

# st.title("📊 HHS Care System Dashboard")

# -------------------------------
# KPI SECTION
# -------------------------------
#st.subheader("🔑 Key Metrics")
st.subheader("🔑 Key Performance Indicators- Overall")

col1, col2, col3, col4 = st.columns(4)

#col1.metric("Total Load", int(df['Total_Load'].iloc[-1]), "+50",  delta_color ="normal" )
#col2.metric("Net Intake", int(df['Net_Intake'].iloc[-1]), "-1", delta_color ="normal" )
#col3.metric("Growth Rate %", round(df['Growth_Rate'].iloc[0], 2), "0%")
#col4.metric("Backlog Active", int(df['Backlog'].sum()), "+5", delta_color ="normal" )

with col1:
    st.metric(
        "Total Load",
        int(current_load),
        delta=f"{load_delta:+,.0f}",
        delta_color="normal"
    )

with col2:
    st.metric(
        "Net Intake",
        int(current_intake),
        delta=f"{intake_delta:+,.0f}",
        delta_color="normal"
    )

with col3:
    st.metric(
        "Growth Rate %",
        round(growth_rate, 2),
        delta=f"{growth_rate:+.2f}%"
    )

with col4:
    st.metric(
        "Backlog Active",
        int(current_backlog),
        delta=f"{backlog_delta:+,.0f}",
        delta_color="normal"
    )

st.sidebar.header("🔧 Filters")
# =====================================
# SIDEBAR FILTERS
# =====================================
#st.sidebar.header("Filters")

# -------- Date Range --------
start_date = st.sidebar.date_input(
    "Start Date",
    value=df.index.min().date()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df.index.max().date()
)

# -------- Time Granularity --------
granularity = st.sidebar.selectbox(
    "Time Granularity",
    ["Daily", "Weekly", "Monthly", "Yearly"]
)

# =====================================
# DATE FILTER
# =====================================
# Convert index to datetime
df.index = pd.to_datetime(
    df.index,
    errors='coerce'
)

# Remove invalid dates
df = df[df.index.notna()]

filtered_df = df[(df.index.date >= start_date) & (df.index.date <= end_date)].copy()

if filtered_df.empty:
    st.warning("No data available")
    st.stop()

# =====================================
# APPLY TIME GRANULARITY
# =====================================
if granularity == "Daily":
    grouped_df = filtered_df.groupby(
        filtered_df.index.date
    ).sum(numeric_only=True)

elif granularity == "Weekly":
    grouped_df = filtered_df.groupby(
        filtered_df.index.to_period('W')
    ).sum(numeric_only=True)

elif granularity == "Monthly":
    grouped_df = filtered_df.groupby(
        filtered_df.index.to_period('M')
    ).sum(numeric_only=True)

elif granularity == "Yearly":
    grouped_df = filtered_df.groupby(
        filtered_df.index.to_period('Y')
    ).sum(numeric_only=True)

# Reset index
grouped_df = grouped_df.reset_index()

#st.write(df.columns.tolist())
#st.write(grouped_df.columns.tolist())
# =====================================
# KPI CALCULATIONS
# =====================================

# Total Children Care
total_children_care = (grouped_df['Children in CBP custody'].iloc[-1]+grouped_df['Children in HHS Care'].iloc[-1])

# Intake
total_intake = grouped_df['Children apprehended and placed in CBP custody*'].iloc[-1]

# Discharge
total_discharge = grouped_df['Children discharged from HHS Care'].iloc[-1]

# Net Intake Pressure
if total_intake != 0:
    net_intake_pressure = ((total_intake - total_discharge) / total_intake) * 100
else:
    net_intake_pressure = 0

# Care Load Volatility Index
load_col = grouped_df['Children in CBP custody']

if load_col.mean() != 0:
    volatility_index = (load_col.std() / load_col.mean()) * 100
else:
    volatility_index = 0

# Backlog Accumulation Rate
initial_load = grouped_df['Children in CBP custody'].iloc[0]
current_load = grouped_df['Children in CBP custody'].iloc[-1]

if initial_load != 0:
    backlog_rate = ((current_load - initial_load) / initial_load) * 100
else:
    backlog_rate = 0

# Discharge Offset Ratio
if total_intake != 0:
    discharge_ratio = (total_discharge / total_intake)
else:
    discharge_ratio = 0


# =====================================
# KPI DASHBOARD
# =====================================
st.subheader("🔑 Key Performance Indicators - Filtered")
st.write("Select the Date Range & Granularity for KPI Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Total Children Care",
        value=f"{total_children_care:,.0f}",
        delta=f"{total_children_care:+,.0f}",
        delta_color="normal"
    )

with col2:
    st.metric(
        "Net Intake Pressure",
        value=f"{net_intake_pressure:,.2f}%",
        delta=f"{net_intake_pressure:+,.2f}%",
        delta_color="normal"
    )

with col3:
    st.metric(
        "Care Load Volatility Index",
        value=f"{volatility_index:,.2f}%",
        delta=f"{volatility_index:+,.2f}%",
        delta_color="normal"
    )

#col4, col5 = st.columns(2)

with col4:
    st.metric(
        "Backlog Accumulation Rate",
        value=f"{backlog_rate:,.2f}%",
        delta=f"{backlog_rate:+,.2f}%",
        delta_color="normal"
    )

with col5:
    st.metric(
        "Discharge Offset Ratio",
        value=f"{discharge_ratio:,.2f}",
        delta=f"{discharge_ratio:+,.2f}",
        delta_color="normal"
    )


# =====================================
# SHOW FILTERED DATA
# =====================================
st.subheader(
    f"{granularity} Aggregated Data"
)

st.dataframe(grouped_df)
#-------------------------------------------

# Initialize session state
#if "input_value" not in st.session_state:
#    st.session_state.input_value = ""

# Function to validate input
#def validate_input():
#    value = st.session_state.input_value

    # Check if input is an integer
#    try:
#        int(value)

#    except ValueError:
#        st.error("❌ Please enter a valid integer number.")
        
        # Clear the field
#        st.session_state.input_value = ""

# Label + input field
#st.text_input(
#    label="Enter an Integer Number:",
#    key="input_value",
#    on_change=validate_input
#)

# Display valid input
#if st.session_state.input_value != "":
#    st.success(
#        f"✅ Valid Integer Entered: {int(st.session_state.input_value)}"
#    )
#------------------------------------------------
#number = st.number_input(
#    "Enter a Number:",
#    min_value=0,
#    step=1,
#    format="%d"
#) 
st.subheader(f"Machine Learning Model Predictions")
st.write("****📌Note: All fields are Mandatory, pls enter your values****")
st.write("*****To Forecast Total Load for Next Day*****")

col1, col2 = st.columns([3, 1])
with col1:
    CAPCBP = st.number_input("1.Children apprehended and placed in CBP custody (range:1-333)", step=1)

col1, col2 = st.columns([3, 1])
with col1:
    CinCBP = st.number_input("2.Children in CBP custody (range:7-531)", step=1)
 
col1, col2 = st.columns([3, 1])
with col1:
    CtoCBP = st.number_input("3.Children transferred out of CBP custody (range:0-440)", step=1)

col1, col2 = st.columns([3, 1])
with col1:
    CinHHS = st.number_input("4.Children in HHS Care (range:1972-11516)", step=1)

col1, col2 = st.columns([3, 1])
with col1:
    CdHHS = st.number_input("5.Children discharged from HHS Care (range:0-505)", step=1)

st.write("*****After Entering Values - Use The Train Model Button First*****")
#st.write(grouped_df.columns.tolist())
try:
 if st.button("Train Model"):
    st.write("*****Training The Model....*****")
    target = grouped_df['Total_Load']
    exog = grouped_df[['Children apprehended and placed in CBP custody*',
                'Children in CBP custody',
                'Children transferred out of CBP custody',
                'Children in HHS Care',
                'Children discharged from HHS Care']]
     
    model = SARIMAX(
        target,
        exog=exog,
        order=(1,1,1),
        seasonal_order=(1,1,1,7)
    )

    st.session_state.results = model.fit()

    st.success("Model Trained")
except Exception : 
  pass
 
st.write("*****Click The Predict Button to forecast for next day*****")
#st.write(grouped_df.columns.tolist())
if st.button("Predict1"):

    # Store all values in a list
    values = [CAPCBP, CinCBP, CtoCBP, CinHHS, CdHHS]

    errors = []

    # Range validation
    if not (1 <= CAPCBP <= 333):
       errors.append("1.Value must be between 1 and 333")

    if not (7 <= CinCBP <= 531):
       errors.append("2.Value must be between 7 and 531")

    if not (0 <= CtoCBP <= 440):
       errors.append("3.Value must be between 0 and 440")

    if not (1972 <= CinHHS <= 11516):
       errors.append("4.Value must be between 1972 and 11516")

    if not (0 <= CdHHS <= 505):
       errors.append("5.Value must be between 0 and 505") 

    # Show errors
    if errors:
       st.error("❌ Invalid Inputs")

       for error in errors:
           st.write(error)
    
    else:
       st.success("✅ All values are valid")
       # Further processing
       st.write("Proceeding with prediction...")
       
       #results = model.fit()
       
       future_exog = pd.DataFrame({
                                  'Children apprehended and placed in CBP custody*':[CAPCBP],
                                  'Children in CBP custody':[CinCBP],
                                  'Children transferred out of CBP custody':[CtoCBP],
                                  'Children in HHS Care':[CinHHS],
                                  'Children discharged from HHS Care':[CdHHS]
                                 })
try:
       if "results" in st.session_state:
           forecast = st.session_state.results.forecast(
                steps=1,
                exog=future_exog
           )
       #forecast = results.forecast(
       #                            steps=1,
       #                            exog=future_exog
       #                           )
     
       predicted_value = forecast.iloc[0]
     
       st.write("*****The Forecast of Total Load for next Day:*****")
       st.metric(
           "Predicted Total Load",
           f"{predicted_value:,.2f}"
        )
except Exception:
    print("Train The Model - using Train Model Button")
#st.write(results.summary())

st.write("------------------------------------------")
#st.write("****📌Note: All fields are Mandatory, pls enter your values****")
st.write("*****To Forecast Total Load within next 7 days(Week)*****")
st.write("*****Use the slider to set num. of days to forecast & Enter The Values*****")
n_steps = st.slider(
    "Select future prediction steps",
    min_value=1,
    max_value=7,
    value=3
)

exog_columns = ['Children apprehended and placed in CBP custody*',
                'Children in CBP custody',
                'Children transferred out of CBP custody',
                'Children in HHS Care',
                'Children discharged from HHS Care'
               ]

# -----------------------------------
# Create empty dataframe
# -----------------------------------
empty_df = pd.DataFrame(
    np.zeros((n_steps, len(exog_columns))),
    columns=exog_columns
)

future_exog = st.data_editor(
    empty_df,
    num_rows="fixed",
    use_container_width=True,
    key="future_exog_table"
   )

validation_passed = True
error_messages =[]

if (future_exog < 0).values.any():
    validation_passed = False
    error_messages.append(
        "Negative values are not allowed."
    )

limits = {
    "Children apprehended and placed in CBP custody*": (1, 333),
    "Children in CBP custody": (7, 531),
    "Children transferred out of CBP custody": (0, 440),
    "Children in HHS Care": (1972, 11516),
    "Children discharged from HHS Care": (0, 505)
}

for col, (min_val, max_val) in limits.items():

    invalid_mask = (
                      (future_exog[col] < min_val) | (future_exog[col] > max_val)
                   )

    if invalid_mask.any():

        invalid_rows = (
            future_exog.index[invalid_mask]
            .tolist()
        )

        validation_passed = False

        error_messages.append(
            f"{col} must be between "
            f"{min_val} and {max_val}. "
            f"Problem in row(s): "
            f"{invalid_rows}"
        )

# -----------------------------
#if st.button("Predict2", key="predict2_button"):
    #if validation_passed:
        #st.success("All inputs are valid.")
     
        #forecast = results.forecast(
            #steps=n_steps,
            #exog=future_exog
        #)

        #st.dataframe(forecast)
        #st.write(f"*****The Forecast of Total Load for next {n_steps} Day:*****")
        #cols = st.columns(n_steps)

        #for i in range(n_steps):
           #with cols[i]:
               #st.metric(
                    #f"Day {i+1}",
                    #f"{forecast.iloc[i]:,.2f}"
                    #)
st.write(f"*****Click The Predict Button to get forecast for {n_steps} Days*****")

if st.button(
    "Predict2",
    key="forecast_btn"):

    if "results" not in st.session_state:

        st.error(
            "Please train model first "
            "using Predict1."
        )

    elif validation_passed:

        forecast = (
            st.session_state.results
            .forecast(
                steps=n_steps,
                exog=future_exog
            )
        )

        st.dataframe(forecast)

        st.write(
            f"Forecast of Total Load "
            f"for next {n_steps} day(s)"
        )

        cols = st.columns(n_steps)

        for i in range(n_steps):

            with cols[i]:

                st.metric(
                    f"Day {i+1}",
                    f"{forecast.iloc[i]:,.2f}"
                )

    else:
        st.write("Train Model First &")
        st.write("Check All Values Submitted &")
        st.write("Click Predict2")
        for err in error_messages:
            #st.write("Please Train Model")
            st.error(err)
    
 
    #else:
        #for err in error_messages:
            #st.error(err)


#------------------------------------------------------
    # Check if any field is empty
    #if any(v is None for v in values):
        #st.error("❌ Please fill all 5 fields.")

    #else:
        #st.success("✅ All fields entered correctly!")

        # Further processing
        #total = sum(values)

        #st.write(grouped_df.columns.tolist())
        #st.write("Total =", total)

#@st.cache_resource
#def train_model():
#    model = LinearRegression()
#    model.fit(X, y)
#    return model

#model = train_model()

st.write("***Tableau Dashboard***")

tableau_url = "https://public.tableau.com/views/USHHSUAC/Dashboard1?:showVizHome=no&:embed=yes"

st.components.v1.iframe(
    tableau_url,
    height=1000,
    scrolling=True
)
#st.write("------------------------------------")
#st.write("*****PRAVEENKUMAR MOPURU*****")
#st.write("*****UMID20032685175*****")
#st.write("*****Data Analyst Intern*****")
#st.write("*****25th March 2026 Batch*****")
#st.write("------------------------------------")


#This automatically restricts input to integers and avoids
# Date range selector
#min_date = df.index.min()
#max_date = df.index.max()

#date_range = st.sidebar.date_input(
#    "Select Date Range",
#    [min_date, max_date]
#)

# Metric toggle
#metric = st.sidebar.selectbox(
#    "Select Metric",
#    ["Total", "Inflow", "Outflow", "Backlog"]
#)

# Time granularity
#granularity = st.sidebar.selectbox(
#    "Time Granularity",
#    ["Daily", "Weekly", "Monthly"]
#)

#df_filtered = df[
#    (df['Date'] >= pd.to_datetime(date_range[0])) &
#    (df['Date'] <= pd.to_datetime(date_range[1]))
#]

#df_filtered = df[
#    (df.index >= pd.to_datetime(date_range[0])) &
#    (df.index <= pd.to_datetime(date_range[1]))
#]

# Resampling based on granularity
#if granularity == "Weekly":
#    df_filtered = df_filtered.resample('W').sum().reset_index()
#elif granularity == "Monthly":
#    df_filtered = df_filtered.resample('M').sum().reset_index()


