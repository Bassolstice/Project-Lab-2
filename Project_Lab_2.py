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
   print(empname, start_date, end_date, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%f}", f"{incometax:,.2f}", f"{netpay:,.2f}")
   print()

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
   print()
   print(f"Total Number Of Employees: {TotEmployees}", f"Total Hours Worked: {TotHours:,.2f}", f"Total Gross Pay: {TotGrossPay:,.2f}", f"Total Tax: {TotTax:,.1%f}", f"Total Net Pay: {TotNetPay:,.2f}")

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
           "Start_date": Start_date,
           "End_date": End_date,
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
       printinfo(empname, from_date, to_date, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)
