def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetStartDate():
    start_date = input("Enter Start date (mm/dd/yyyy): ")
    return start_date

def GetEndDate():
    end_date = input("Enter End date (mm/dd/yyyy): ")
    return end_date

def GetHoursWorked():
    hours = float(input("Enter hours worked: "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
   taxrate = float(input("Enter tax rate: "))
   return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
   grosspay = hours * hourlyrate
   incometax = grosspay * taxrate
   netpay = grosspay - incometax
   return grosspay, incometax, netpay

def printinfo(empname, start_date, end_date, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print("Name:  ", empname) 
    print("Start Date: ", f"{start_date}")
    print("End Date: ", f"{end_date}")
    print("Hourly Rate: ", f"{hourlyrate:,.2f}")
    print("Gross Pay: ", f"{grosspay:,.2f}")
    print("Tax Rate: ", f"{taxrate:,.1%}")
    print("Income Tax: ", f"{incometax:,.2f}")
    print("Net Pay: ", f"{netpay:,.2f}")
    print()

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")
    print(f"Total Gross Pay: {TotGrossPay:,.2f}")
    print(f"Total Tax: {TotTax:,.1%}")
    print(f"Total Net Pay: {TotNetPay:,.2f}")



if __name__ == "__main__":
   TotEmployees = 0
   TotHours = 0.00
   TotGrossPay = 0.00
   TotTax = 0.00
   TotNetPay = 0.00
   payroll_data = []
   while True:
       empname = GetEmpName()
       if (empname.upper() == "END"):
           break
       start_date = GetStartDate()
       end_date = GetEndDate()
       hours = GetHoursWorked()
       hourlyrate = GetHourlyRate()
       taxrate = GetTaxRate()

       grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
       payroll_data.append({
           "empname": empname,
           "start_date": start_date,
           "end_date": end_date,
           "hours": hours,
           "hourlyrate": hourlyrate,
           "taxrate": taxrate,
           "grosspay": grosspay,
           "incometax": incometax,
           "netpay": netpay
       })

       TotEmployees += 1;
       TotHours += hours 
       TotGrossPay += grosspay 
       TotTax += incometax 
       TotNetPay += netpay
       

PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
