select * from financial_loan;
--**  Key performance Indicator
-- total number of loan application
select count(id) as total_loan_app from financial_loan;

--	month to date loan application 
select count(id) as total_lA_myd from financial_loan 
where MONTH(issue_date)=12 and YEAR(issue_date)=2021;

--	 previous month to date loan application 
select count(id) as Ptotal_lA_myd from financial_loan 
where MONTH(issue_date)=11 and YEAR(issue_date)=2021;

--total funded amount/loan amount
select SUM(loan_amount) as total_loan_amount from financial_loan;

-- monthly basis total funded amount/loan amount
select SUM(loan_amount) as total_loan_amount from financial_loan
where MONTH(issue_date)=12 and YEAR(issue_date)=2021;

-- average interest 
 select avg(int_rate)*100	as avg_interest from financial_loan;
 select round(avg(int_rate),4)*100	as avg_interest from financial_loan
 
 -- as per latest month and year
  select round(avg(int_rate),4)*100	as avg_interest from financial_loan
  where MONTH(issue_date)=12 AND YEAR(issue_date)=2021;

  -- as per  previous month and year
  select round(avg(int_rate),4)*100	as avg_interest from financial_loan
  where MONTH(issue_date)=11 AND YEAR(issue_date)=2021;

-- average dti 
select round(avg(dti),4)*100 as avg_dti from financial_loan;

-- as per month and year
select round(avg(dti),4)*100 as avg_dti from financial_loan
where MONTH(issue_date)=12 and YEAR(issue_date)=2021;

-- previoius month dti 
select round(avg(dti),4)*100 as avg_dti from financial_loan
where MONTH(issue_date)=11 and YEAR(issue_date)=2021;

-- good  Loan Percentage
SELECT (COUNT(CASE WHEN loan_status= 'Fully Paid' OR loan_status='Current' THEN id END)*100)
/ COUNT(id) as good_loan_perfo from financial_loan;

--good loan application

select COUNT(id) good_loan_app from financial_loan
where loan_status='Fully Paid' or loan_status='Current'; 

--good loan funded amount


select sum(loan_amount) good_loan_amt from financial_loan
where loan_status='Fully Paid' or loan_status='Current'; 


--good loan recieved amt
select sum(total_payment) good_loan_recived_amt from financial_loan
where loan_status='Fully Paid' or loan_status='Current'; 


-- bad loan percentage

SELECT (COUNT(CASE WHEN loan_status= 'Charged Off'  THEN id END)*100)
/ COUNT(id) as bad_loan_percen from financial_loan;

-- bad loan application
select COUNT(id) bad_loan_app from financial_loan
where loan_status='Charged Off'; 

-- bad loan funded amt
select sum(loan_amount) bad_loan_amt from financial_loan
where loan_status='Charged Off' ; 

-- bad loan recived amt 
select sum(total_payment) bad_loan_recived_amt from financial_loan
where loan_status='Charged Off';  loan

--loan status grid  view
select  loan_status,
	COUNT(id) As  Total_loan_app,
	SUM(total_payment) AS Total_Amount_Recieved,
	SUM(loan_amount) As Total_funded_Amount,
	AVG(int_rate *100) As  Interest_rate,
	AVG(dti*100) As Dti 
	from financial_loan 
	group by loan_status;

-- loan status grid view month to date
select  loan_status,SUM(total_payment) As mid_t_p,
SUM(loan_amount) as mtd_loan_amount
from financial_loan  where MONTH(issue_date)=12 
group by  loan_status;






