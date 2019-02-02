import pandas as pd


#read the excel file/ preparing the data for pivot
mRate= pd.read_excel("state-marriage-rates-90-95-99-17.xlsx",
                     skiprows=5, # skip 1st 5 rows of excel file
                     header=0,       # header is now in the first row
                     skipfooter=8,  # skip last 8 rows of excel file
                     index_col=[0]   # index columns are 1st in excel file 
                     )

#drop the first empty row
mRate.drop(mRate.index[0],inplace=True)

# pivot the table
mRate=mRate.stack().reset_index()

#rename the column's name
mRate.rename(columns={"level_1": "Year", 0: "Rate"},inplace=True )  

#write a new excel file and delete pandas index
mRate.to_excel(excel_writer='cleaned_file.xls',index=False)
                                  
