'''
STUDENT ID 31213294
STUDENT NAME KAPISH KUCHROO
Date Created :14th april2020
Last modified :30th april 2020

'''

'''FLOW OF PROGRAM
 
1.    read_data function will read the data from the file 'AU_INV_START.txt'
 	  and using readline command it will read and store the values of the string type
  	  (which are converted to integer data type)
  	  for start year, start stock and start revenue returned to the read_data function.

2.    calculate_stock_revenue funtion will have received a dictionary.
      First we are calculating revenue of months with certain deciding factors for every month like global financial crises,peak months sale,inflation,
      defective items revenue,which are added to the monthly_revenue and provided to total_revenue which is returned to the dictionary with return call.
      Stock updataion is done daily and final value is returned to the end_stock variable when stocks drop below 400.
      Finally an increment operation is done on the end year of the file input(end_year).

3.	  write_data function will write the data from the calculate_stock_revenue funtion to the file 'AU_INV_END.txt'.
	  We are opening the file in write mode and 
	  endyear,total_stock,and total_revenue will be returned as the final output with the print statement.'''
 


'''read function for reading values from file and storing it in the inventory_info dictionary'''

def read_data():
	fhand=open('AU_INV_START.txt','r') #format for reading the data from the file in read mode
	inventory_info={}   #name of the dictionary
	inventory_info['start_year']=int(fhand.readline())  		#storing  start year
	inventory_info['start_stock']=int(fhand.readline()) 		#storing  start stock
	inventory_info['start_revenue']=int(fhand.readline())	#storing  start revenue
	return inventory_info  #dictionary returned


'''calculate function returns the end year, end stock and end revenue'''

def calculate_stock_revenue(initial_values_inventory):
	monthly_revenue=0
	prevDefectiveItems=0
	previous_rrp=0
	start_year=initial_values_inventory['start_year']   
	total_stock=initial_values_inventory['start_stock']		
	total_revenue=initial_values_inventory['start_revenue']
	
	
	for month in range(0,12):     #iterating over months using range
		
		if month==0:		 #january 		#conditional statements if/elif
			no_days=31        
			if start_year==2009:  				#global financial crisis
				distribution=36 - (20*36)/100	
				rrp=705+(10*705)/100
			elif start_year==2010:				#global financial crisis
				distribution=36-(10*36)/100
				rrp=705+(5*705)/100
			elif start_year==2011:				#global financial crisis
				distribution=36-(5*36)/100
				rrp=705+(3*705)/100
			else:   
				distribution=36
				rrp=705
			
		elif month==1:	#feburary
			# Leap year check
			if start_year % 4 == 0 and start_year % 100 != 0:
				no_days=29
			else:
				no_days=28

		elif month==2:	#march
			no_days=31
			distribution =distribution - (35*distribution)/100
			rrp = rrp - (20*rrp)/100

		elif month==3:	 #april
			no_days=30

		elif month==4:	 #may
			no_days=31
		
		elif month==5:	 #june
			no_days=30
		
		elif month==6:	 #july(inflation)
			no_days=31
			distribution=distribution + (10*distribution)/100
			rrp = rrp + (5*rrp)/100
		
		elif month==7:   #august
			no_days=31
		
		elif month==8:	 #september
			no_days=30
		
		elif month==9:	 #october
			no_days=31
		
		elif month==10:  #november(peak sale)
			no_days = 30
			distribution = distribution + (35*distribution)/100
			rrp = rrp + (20*rrp)/100
		
		elif month==11:	 #december
			no_days = 31


		distribution=int(distribution)
		totalItems = no_days * distribution
		curDefectiveItems =(5*totalItems)/100 #defective items back to warehouse
		curDefectiveItems = int(curDefectiveItems)
		monthly_revenue = totalItems * rrp
		monthly_revenue = monthly_revenue - curDefectiveItems*rrp#revenue after defective revenue is removed
		monthly_revenue = monthly_revenue + prevDefectiveItems*((80 * previous_rrp)/100) #monthly revenue after adding resale of previous month
		prevDefectiveItems = curDefectiveItems	#defective items of previous month used in the next month's monthly revenue
		previous_rrp=rrp #stores the previous month's rrp
		total_revenue=total_revenue+monthly_revenue  #total_revenue are returned to dictionary
		

		# Re-stocking is done from day1 to no_days
		for stock_check in range(1,no_days+1):
				total_stock=total_stock-distribution
				if (total_stock<400):#restocked if less than 400
					total_stock=total_stock+600 #returned to dictionary after 12 months
		print(total_stock)

	inventory_calculation={}					#dictionary type declaration
	inventory_calculation['end_year']=start_year+1 # year increment in the output file
	inventory_calculation['end_stock']=total_stock
	inventory_calculation['end_revenue']=total_revenue
	return inventory_calculation	#returned value of end year,end stock,end revenue 


#write function for printing values to file.

def write_data(final_values_inventory):  #stores data returned from the calculate_stock_revenue function
	fhand=open('AU_INV_END.txt','w') #opened in write mode
	end_year=final_values_inventory['end_year']				#dictionary key 'end_year' used to store data in end_year
	total_stock=final_values_inventory['end_stock']			#dictionary key 'end_stock' used to store data in total_stock
	total_revenue=final_values_inventory['end_revenue']		#dictionary key 'end_revenue' used to store data in total_revenue
	print(end_year,file=fhand) #writing values to file
	print(total_stock,file=fhand)
	print(total_revenue,file=fhand) 


initial_values_inventory=read_data()   # initial_values_inventory stores the read dictionary data.

final_values_inventory=calculate_stock_revenue(initial_values_inventory) # variable stores data of the calculate function.

write_data(final_values_inventory) #writes the values to the file.

