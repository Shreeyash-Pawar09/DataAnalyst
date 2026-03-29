# Bank Loan Analysis 
#Imported the library which are necessary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr # when we get any error it gives the explanation in structure way.
import plotly.express as px # it  is sue to creaate a inetrcative charts or 
#visuals 

#Fetching the data into notebook from the folder 
df=pd.read_excel("C:/Data Analysis/Data Analyst  Project/Bank loan analysis/financial_loan.xlsx")

# Total Loan Application
total_loan_app=df['id'].count()
print("Total _ Loan application",total_loan_app)

# KPI  : Key Performance Indicator
 #  MTD Total Loan Application

latest_issue_date=df['issue_date'].max()
latest_year= latest_issue_date.year
latest_month=latest_issue_date.month
mtd_data=df[(df['issue_date'].dt.year==latest_year) & (df['issue_date'].dt.month==latest_month)]

mtd_loan_app=mtd_data['id'].count()
# print(f "") f is just a string which is use to take both text and dynamic   value
print(f"MTD loan application  (for  {latest_issue_date.strftime('%B %Y')}):{mtd_loan_app}") 
# b is for month and    y is for year and strftime function is use to convert data into moth and  year 

# Total Funded amount
totalfunded_amt=df['loan_amount'].sum() #sum functio it will give the total of  amount that is  there
total_fun_amt_mil=totalfunded_amt/1000000
print("The Total funded amount is : ${:.2f}M".format(total_fun_amt_mil))

# MTD  Total funded amount
latest_issue_date=df['issue_date'].max()
latest_year= latest_issue_date.year
latest_month=latest_issue_date.month
mtd_data=df[(df['issue_date'].dt.year==latest_year) & (df['issue_date'].dt.month==latest_month)]

mtd_loan_app=mtd_data['id'].count()
mtd_loan_amount=mtd_data['loan_amount'].sum()
mtd_loan_amount_mil=mtd_loan_amount/1000000
print("The total mtd loan amount is :${:.2f}M".format(mtd_loan_amount_mil))

# Total Amount Recieved 
total_receive_amt=df['total_payment'].sum() #sum functio it will give the total of  amount that is  there
total_recieve_amt_mil=total_receive_amt/1000000
print("The Total Receive amount is : ${:.2f}M".format(total_recieve_amt_mil))

# MTD Receive amount

latest_issue_date=df['issue_date'].max()
latest_year= latest_issue_date.year
latest_month=latest_issue_date.month
mtd_data=df[(df['issue_date'].dt.year==latest_year) & (df['issue_date'].dt.month==latest_month)]

mtd_loan_app=mtd_data['id'].count()
mtd_receive_amount=mtd_data['total_payment'].sum()
mtd_receive_amount_mil=mtd_receive_amount/1000000
print("The total mtd loan amount receive is :${:.2f}M".format(mtd_receive_amount_mil))

# Average Interset rate

avg_int_rate=df['int_rate'].mean()*100
print("The  Avg Interest Rate is: {:.2f}%".format(avg_int_rate))

# Average Debt to income Ratio

avg_dti_rate=df['dti'].mean()*100
print("The  Avg DTI  Rate is: {:.2f}%".format(avg_dti_rate))

#  Good Loan Metric

good_loans= df[df['loan_status'].isin(["Fully Paid","Current"])]

total_loan_app=df['id'].count()

good_loan_total_app= good_loans['id'].count()

good_loan_amt_fun= good_loans['loan_amount'].sum()

good_loan_rec_amt= good_loans['total_payment'].sum()

good_loan_perc=(good_loan_total_app/total_loan_app) * 100

#  Convert the number in millions

good_loan_fun_mill=good_loan_amt_fun/1000000

good_loan_rec_amt_mil=good_loan_rec_amt/1000000 

# Printing of  Values
print("The good loan application",good_loan_total_app)

print("The good loan percentage {:.2f}%".format(good_loan_perc))

print("The good  loan funded amount : ${:.2f}M".format(good_loan_fun_mill))

print("The good  loan receive amount : ${:.2f}M".format(good_loan_rec_amt_mil))

# Bad Loan Metric
bad_loans= df[df['loan_status'].isin(["Charged Off"])]

total_loan_app=df['id'].count()

bad_loan_total_app= bad_loans['id'].count()

bad_loan_amt_fun= bad_loans['loan_amount'].sum()

bad_loan_rec_amt= bad_loans['total_payment'].sum()

bad_loan_perc=(bad_loan_total_app/total_loan_app) * 100

#  Convert the number in millions

bad_loan_fun_mill=bad_loan_amt_fun/1000000

bad_loan_rec_amt_mil=bad_loan_rec_amt/1000000 

# Printing of  Values
print("The good loan application",bad_loan_total_app)

print("The good loan percentage {:.2f}%".format(bad_loan_perc))

print("The good  loan funded amount : ${:.2f}M".format(bad_loan_fun_mill))

print("The good  loan receive amount : ${:.2f}M".format(bad_loan_rec_amt_mil))

# Montly trend by issue date Funded amount

montly_funded=(
    df.sort_values('issue_date')
      .assign(month_name=lambda x :x['issue_date'].dt.strftime('%b %y'))
      .groupby('month_name', sort=False)['loan_amount'] 
      .sum()
      .div(1000000)
      .reset_index(name='loan_amount_millions')
)
plt.figure(figsize=(10,5))
plt.fill_between(montly_funded['month_name'],montly_funded['loan_amount_millions'],color='skyblue' ,alpha=0.7)
plt.plot(montly_funded['month_name'], montly_funded['loan_amount_millions'],color='blue',linewidth=2)
for i, row in montly_funded.iterrows():
    plt.text(i,row['loan_amount_millions']+0.1,f"{row['loan_amount_millions']:.2f}",
             ha='center',va='bottom', fontsize=9,rotation=0,color='black')
    
    
plt.title("Total Funded amount  by Month", fontsize=14)
plt.xlabel('Month')
plt.ylabel('Funded amount (Millons)')
plt.xticks(ticks=range(len(montly_funded)),label=montly_funded['month_name'],rotation=30)
plt.grid(True,linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()

# For Funds received
montly_received=(
    df.sort_values('issue_date')
      .assign(month_name=lambda x :x['issue_date'].dt.strftime('%b %y'))
      .groupby('month_name', sort=False)['total_payment'] 
      .sum()
      .div(1000000)
      .reset_index(name='loan_amount_millions')
)
plt.figure(figsize=(10,5))
plt.fill_between(montly_received['month_name'],montly_received['loan_amount_millions'],color='green' ,alpha=0.3)
plt.plot(montly_received['month_name'], montly_received['loan_amount_millions'],color='red',linewidth=2)
for i, row in montly_received.iterrows():
    plt.text(i,row['loan_amount_millions']+0.1,f"{row['loan_amount_millions']:.2f}",
             ha='center',va='bottom', fontsize=9,rotation=0,color='black')
    
    
plt.title("Total Recieved amount  by Month", fontsize=14)
plt.xlabel('Month')
plt.ylabel('Received amount (Millons)')
plt.xticks(ticks=range(len(montly_received)),label=montly_received['month_name'],rotation=30)
plt.grid(True,linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()

 # Loan Application

loan_app_mon=(
    df.sort_values('issue_date')
      .assign(month_name=lambda x :x['issue_date'].dt.strftime('%b %y'))
      .groupby('month_name', sort=False)['id'] 
      .count()
      .reset_index(name='loan_amount_millions')
)
plt.figure(figsize=(10,5))
plt.fill_between(loan_app_mon['month_name'],loan_app_mon['loan_amount_millions'],color='yellow' ,alpha=0.2)
plt.plot(loan_app_mon['month_name'], loan_app_mon['loan_amount_millions'],color='green',linewidth=2)
for i, row in loan_app_mon.iterrows():
    plt.text(i,row['loan_amount_millions']+0.1,f"{row['loan_amount_millions']:.2f}",
             ha='center',va='bottom', fontsize=9,rotation=0,color='black')
    
    
plt.title("Total Loan  Application  ", fontsize=14)
plt.xlabel('Month')
plt.ylabel('Total Loan appliaction ')
plt.xticks(ticks=range(len(loan_app_mon)),label=loan_app_mon['month_name'],rotation=30)
plt.grid(True,linestyle='--',alpha=0.5)
plt.tight_layout()
plt.show()

# Regional Analaysis by State for funded amount
state_funding = df.groupby('address_state')['loan_amount'].sum().sort_values(ascending=True)
state_funding_thousands = state_funding / 1000

plt.figure(figsize=(10, 8))
bars = plt.barh(state_funding_thousands.index, state_funding_thousands.values, color='blue')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}K', va='center', fontsize=9)

plt.title('Total Funded Amount by State (in ₹ Thousands)')
plt.xlabel('Funded Amount (₹ \'000)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# Regional Analaysis by State for Received  amount 

state_receive = df.groupby('address_state')['total_payment'].sum().sort_values(ascending=True)
state_receive_thousands = state_receive / 1000

plt.figure(figsize=(10, 8))
bars = plt.barh(state_receive_thousands.index, state_receive_thousands.values, color='green')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}K', va='center', fontsize=9)

plt.title('Total receive Amount by State (in ₹ Thousands)')
plt.xlabel('Receive Amount (₹ \'000)')
plt.ylabel('State')
plt.tight_layout()
plt.show()

# Regional analysis for Loan Appliaction
state_loan_app = df.groupby('address_state')['id'].count().sort_values(ascending=True)


plt.figure(figsize=(10, 8))
bars = plt.barh(state_loan_app.index, state_loan_app.values, color='pink',alpha=1)

for bar in bars:
    width = bar.get_width()
    plt.text(width + 10, bar.get_y() + bar.get_height() / 2,
             f'{width:,.0f}', va='center', fontsize=9)
 
plt.title('Total loan appliction by State')
plt.xlabel('Loan Appliaction') 
plt.ylabel('State')
plt.tight_layout()
plt.show()

# Loan term Analysis for  funded amount
term_funding_millions = df.groupby('term')['loan_amount'].sum() / 1000000

plt.figure(figsize=(5, 5))
plt.pie(
    term_funding_millions,
    labels=term_funding_millions.index,
    autopct=lambda p: f"{p:.1f}%\n${p*sum(term_funding_millions)/100:.1f}M",
    startangle=90,
    wedgeprops={'width': 0.4}
)

plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))
plt.title("Total Funded Amount by Term (in $ Millions)")
plt.show()

# loan term analaysis for amount received

term_recieve_millions = df.groupby('term')['total_payment'].sum() / 1000000

plt.figure(figsize=(5, 5))
plt.pie(
    term_recieve_millions,
    labels=term_recieve_millions.index,
    autopct=lambda p: f"{p:.1f}%\n${p*sum(term_recieve_millions)/100:.1f}M",
    startangle=90,
    wedgeprops={'width': 0.4}
)

plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))
plt.title("Total Received  Amount by Term (in $ Millions)")
plt.show()


# loan tem application

term_loan_app = df.groupby('term')['id'].count()
plt.figure(figsize=(5, 5))
plt.pie(
    term_loan_app,
    labels=term_loan_app.index,
    autopct=lambda p: f"{p:.1f}%\n{p*sum(term_loan_app)}",
    startangle=90,
    wedgeprops={'width': 0.4}
)

plt.gca().add_artist(plt.Circle((0, 0), 0.70, color='white'))
plt.title("Total loan appliction")
plt.show()

# Employee Length for  funded amount
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr # when we get any error it gives the explanation in structure way.
import plotly.express as px # it  is sue to creaate a inetrcative charts or 
#visuals 
df=pd.read_excel("C:/Data Analysis/Data Analyst  Project/Bank loan analysis/financial_loan.xlsx")
emp_funding =df.groupby('emp_length')['loan_amount'].sum().sort_values() / 1000

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_funding.index, emp_funding, color='purple')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height() / 2,
             f"{width:,.0f}K", va='center', fontsize=9)

plt.xlabel("Funded Amount (₹ Thousands)")
plt.title("Total Funded Amount by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# employee length for received amount
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr # when we get any error it gives the explanation in structure way.
import plotly.express as px # it  is sue to creaate a inetrcative charts or 
#visuals 
df=pd.read_excel("C:/Data Analysis/Data Analyst  Project/Bank loan analysis/financial_loan.xlsx")
emp_received =df.groupby('emp_length')['loan_amount'].sum().sort_values() / 1000

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_received.index, emp_received, color='red')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height() / 2,
             f"{width:,.0f}K", va='center', fontsize=9)

plt.xlabel("Received  Amount (₹ Thousands)")
plt.title("Total Received Amount by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# employee length by loan application
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings as wr # when we get any error it gives the explanation in structure way.
import plotly.express as px # it  is sue to creaate a inetrcative charts or 
#visuals 
df=pd.read_excel("C:/Data Analysis/Data Analyst  Project/Bank loan analysis/financial_loan.xlsx")
emp_loan_app =df.groupby('emp_length')['id'].count().sort_values() 

plt.figure(figsize=(10, 6))
bars = plt.barh(emp_loan_app.index, emp_loan_app, color='grey')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 5, bar.get_y() + bar.get_height() / 2,
             f"{width:,.0f}", va='center', fontsize=9)

plt.xlabel("Employee  length loan application ")
plt.title("Total loan application  by Employment Length")
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# loan purpose by funded amount
purpose_funding_millions = (df.groupby('purpose')['loan_amount'].sum().sort_values() / 1000000)

plt.figure(figsize=(10, 6))
bars = plt.barh(purpose_funding_millions.index, purpose_funding_millions.values, color='skyblue')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             f'{width:.2f}M', va='center', fontsize=9)

plt.title('Total Funded Amount by Loan Purpose (₹ Millions)', fontsize=14)
plt.xlabel('Funded Amount (₹ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# loan purpose by recived amount
purpose_funding_millions = (df.groupby('purpose')['total_payment'].sum().sort_values() / 1000000)

plt.figure(figsize=(10, 6))
bars = plt.barh(purpose_funding_millions.index, purpose_funding_millions.values, color='darkred')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             f'{width:.2f}M', va='center', fontsize=9)

plt.title('Total Funded Amount by Loan Purpose (₹ Millions)', fontsize=14)
plt.xlabel('Funded Amount (₹ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# loan purpose by total loan application
purpose_funding_millions = (df.groupby('purpose')['id'].count().sort_values())

plt.figure(figsize=(10, 6))
bars = plt.barh(purpose_funding_millions.index, purpose_funding_millions.values, color='darkgreen')

for bar in bars:
    width = bar.get_width()
    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
             f'{width:.2f}', va='center', fontsize=9)

plt.title('Total Funded Amount by Loan Purpose (₹ Millions)', fontsize=14)
plt.xlabel('Funded Amount (₹ Millions)')
plt.ylabel('Loan Purpose')
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# home Ownership for funded amount

home_funding = df.groupby('home_ownership')['loan_amount'].sum().reset_index() 
home_funding['loan_amount_millions'] = home_funding [ 'loan_amount'] / 1000000
fig= px.treemap(

home_funding,
path=['home_ownership'],
values='loan_amount_millions',
color='loan_amount_millions', 
color_continuous_scale='Blues',
title='Total Funded Amount by Home Ownership ( Millions)'
)
fig.show()

 # home ownership for  Received amount

home_funding = df.groupby('home_ownership')['total_payment'].sum().reset_index() 
home_funding['loan_amount_millions'] = home_funding [ 'total_payment'] / 1000000
fig= px.treemap(

home_funding,
path=['home_ownership'],
values='loan_amount_millions',
color='loan_amount_millions', 
color_continuous_scale='Blues',
title='Total Received Amount by Home Ownership ( Millions)'
)
fig.show()
# Total loan appliaction for home owner ship

loan_app_home = df.groupby('home_ownership')['id'].count().reset_index() 
loan_app_home['loan_amount_millions'] = home_funding [ 'id'] / 1000
fig= px.treemap(

loan_app_home,
path=['home_ownership'],
values='loan_amount_millions',
color='loan_amount_millions', 
color_continuous_scale='Blues',
title='Total  loan application  by Home Ownership'
)
fig.show()




