Upload the file
Skip first 7 rows in csv file
Select usefull columns usecols=['Occurred On (NT)', 'Cleared On (NT)', 'MO Name', 'Name']
Remove "NodeB Name=" & after the , part from "MO Name" column
Extract last 2 characters from MO Name column place it as seperate column name ['Region ID']
Extract first 6 characters from MO Name column place it as seperate column name ['Site ID']
Check If 'NOA' tag is include in 'MO Name' then set 'Region ID' to 'NOA'
Move 'Site ID' column to before 'MO Name' column
Add 'Site Type' column to table and define sites as their type
Add 'Duration' column and calculate the Duration
Round up the duration first decimal point
Convert the dataframe to an html table
render the table in the table.html template

#Generate chart
    count the occurrences by site ID
    create a dictionary containing the data for the chart
    print the JSON string to the console in debug mode

Connect with MongoDB
Update Cleared On column with Date Now
replace '-' with current date and time in 'Cleared On (NT)' column

FTG table upload
Compare values with ftg table put them into New column


use fontawesome icons and google fonts to modify that.Also use material ui concepts.Use only Tailwind CSS.forms should be in 3 columns.background color should #14213d.You can match text color as better to background.