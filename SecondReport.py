#Program to generate second exception report
#for One Stop Insurance Company
#Date written : DECEMBER 05 2023
#Author : SIREESHA KUPPAMPATI
import FormatValues as FV
import datetime
import time
Today = datetime.datetime.now()
TodayDsp = datetime.datetime.strftime(Today, "%Y-%m-%d")
# Open the defaults file and read the values into variables
f = open('OSICD.dat','r')
POL_NUM = int(f.readline())
BASIC_PREM = float(f.readline())
DISC_ADDT_CARS =float(f.readline())
EXTRA_LIAB_COV_COST = float(f.readline())
GLS_COV_COST =float(f.readline())
LOANER_CARCOV_COST = float(f.readline())
HST_RATE = float(f.readline())
PROC_MON_FEE = float(f.readline())
f.close()
print()
# Process to follow when generating a report.
# Print the summary / analytics data.
print()
print("  ONE STOP INSURANCE COMPANY")                   
print(f"  MONTHLY PAYMENT AS OF  {(TodayDsp):<12s}")
print()
print("   POLICY    CUSTOMER                TOTAL            HST        TOTAL        DOWN         MONTHLY")
print("   NUMBER    NAME                    PREMIUM                     COSTS        PAYMENT      PAYMENT")
print("=====================================================================================================")
print()
# Initialize counters and accumulators for summary / analytics.
PolicyNumberCtr = 0
Tot_Premium_sum = 0
HST_Sum = 0
Total_Cost_Sum = 0
Tot_DownPay_Sum = 0
Mon_Payment_sum = 0
# Open the file with the "r" mode for read.
f = open("Policies 2.dat", "r")
# Set up the loop to process all the records in the file.
for PolicyRecord in f:      
    # Input - read the first record and split into a list.
    PolicyList = PolicyRecord.split(",")

    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    Inv_Num = PolicyList[0].strip()
    Cust_First_Name = PolicyList[2].strip()
    Cust_Last_Name = PolicyList[3].strip()
    Payment_Type = PolicyList[13].strip()
    Down_Pay = float(PolicyList[14].strip())
    No_Of_Cars = int(PolicyList[9].strip())
    Ext_service = PolicyList[10].strip()
    Glass_Service = PolicyList[11].strip()
    Loaner_Service = PolicyList[12].strip()

    # Perform any required calculations.  In this report, none are necessary.
    if Ext_service == "Y":
        EXTRA_LIAB_COV_COST = 130.00
    else:
        Ext_service  == "N"
        EXTRA_LIAB_COV_COST = 0

    if Glass_Service == "Y":
        GLS_COV_COST = 86.00
    else:
        Glass_Service  == "N"
        GLS_COV_COST = 0

    if Loaner_Service == "Y":
        LOANER_CARCOV_COST = 58.00
    else:
        Loaner_Service  = "N"
        LOANER_CARCOV_COST = 0
    
    Total_Extra_Costs = EXTRA_LIAB_COV_COST + GLS_COV_COST + LOANER_CARCOV_COST
    Discount =  No_Of_Cars * (869.00 - (869.00 * 0.25))
    if No_Of_Cars > 1:
        Ins_Premium = 869.00  + Discount
        Tot_Premium = Ins_Premium + (Total_Extra_Costs * No_Of_Cars)
    else:
        Ins_Premium = 869.00    
        Tot_Premium = Ins_Premium + Total_Extra_Costs
    HST = Tot_Premium * HST_RATE
    Total_Cost = Tot_Premium + HST_RATE
   
    if Payment_Type == "Monthly":
        Mon_Payment = (Total_Cost + PROC_MON_FEE) / 12
    elif Payment_Type =="Down Pay":
        Mon_Payment = ((Total_Cost-Down_Pay) + PROC_MON_FEE) / 12
    
        print(f"  {Inv_Num:<4s}     {Cust_First_Name:<6s}{Cust_Last_Name:>8s}          {FV.FDollar2(Tot_Premium):>9s}       {FV.FDollar2(HST):>9s}    {FV.FDollar2(Total_Cost):>9s}    {FV.FDollar2(Down_Pay):>9s}     {FV.FDollar2(Mon_Payment):>9s}")
    # Print the detail line.  A detail line is the details of the record you want.
    # Increment and Accumulate the summary / analytics data.
        PolicyNumberCtr += 1
        Tot_Premium_sum += Tot_Premium
        HST_Sum += HST
        Total_Cost_Sum += Total_Cost
        Tot_DownPay_Sum += Down_Pay
        Mon_Payment_sum += Mon_Payment
    
f.close()
    # Print the summary / analytics data.
print("=====================================================================================================")
print()
print(f" Total Policies:{PolicyNumberCtr:>3d}               {FV.FDollar2(Tot_Premium_sum):>10s}       {FV.FDollar2(HST_Sum):>10s}   {FV.FDollar2(Total_Cost_Sum):>10s}    {FV.FDollar2(Tot_DownPay_Sum):>10s}   {FV.FDollar2(Mon_Payment_sum):>10s}") 
print()


# Write the current values back t the default file. Note the use of “w” to overwrite and the use of
# the \n so that each value is placed on a separate line.
f = open('OSICD.dat', 'w')
f.write("{}\n".format(str(POL_NUM)))
f.write("{}\n".format(str(BASIC_PREM)))
f.write("{}\n".format(str(DISC_ADDT_CARS)))
f.write("{}\n".format(str(EXTRA_LIAB_COV_COST)))
f.write("{}\n".format(str(GLS_COV_COST)))
f.write("{}\n".format(str(LOANER_CARCOV_COST)))
f.write("{}\n".format(str(HST_RATE)))
f.write("{}\n".format(str(PROC_MON_FEE)))
f.close()
print()