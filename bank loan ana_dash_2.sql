				-- charts 

-- monthly trend by issue date and month wise loan status
select 
MONTH(issue_date) As month_number,DateName(MONTH,issue_date) Month_Name,
COUNT(id) as Total_loan_Application,
SUM(loan_amount) as funded_amount,
SUM(Total_payment) as total_fund_recieved 
from financial_loan 
group by  MONTH(issue_date),DateName(MONTH, issue_date)
order by MONTH(issue_date),DateName(MONTH,issue_date);


-- regional   analysis for address state
select
address_state,
COUNT(id) as Total_loan_Application,
SUM(loan_amount) as funded_amount,
SUM(Total_payment) as total_fund_recieved 
from financial_loan 
group by address_state
order by  address_state;

-- analysis for  loan term 
select
term,
COUNT(id) as Total_loan_Application,
SUM(loan_amount) as funded_amount,
SUM(Total_payment) as total_fund_recieved 
from financial_loan 
group by term
order by  COUNT(id)

--Employee length analysis
select
emp_length,
COUNT(id) as Total_loan_Application,
SUM(loan_amount) as funded_amount,
SUM(Total_payment) as total_fund_recieved 
from financial_loan 
group by emp_length
order by  COUNT(id) desc;

--loan purposee analysi
select
purpose,
COUNT(id) as Total_loan_Application,
SUM(loan_amount) as funded_amount,
SUM(Total_payment) as total_fund_recieved 
from financial_loan 
group by purpose
order by  COUNT(id) desc;

--home ownership analysis
select
home_ownership,
COUNT(id) as Total_loan_Application,
SUM(loan_amount) as funded_amount,
SUM(Total_payment) as total_fund_recieved 
from financial_loan 
group by home_ownership
order by  COUNT(id) desc;







