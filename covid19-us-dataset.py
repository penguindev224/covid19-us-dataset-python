import urllib.request as request
import csv
import re


# [Cleaning] Import dataset from John Hopkin's excel file
r = request.urlopen('https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv').read().decode('utf8').split("\n")
John_dataset = csv.reader(r)
John_US = []
for line in John_dataset:
    for singlerow in line:
    	# [Filtering] Extract only US data into an array named "John_US"
    	# [Filtering] Input the dataset only if it has a date - This requirement is not explicitly listed but it is done anyway so the feature is left here.
    	if (singlerow == "US"):
    		x = re.search(r'\d{4}-\d{1,2}-\d{1,2}', line[0])
    		if x:
    			John_US.append(line)


# [Cleaning] Import dataset from NYT's excel file
r = request.urlopen('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv').read().decode('utf8').split("\n")
NYT = csv.reader(r)
NYT_withaDate = []
for row in NYT:
	#  [Filtering] Input the dataset only if it has a date - This requirement is not explicitly listed but it is done anyway so the feature is left here.
	x = re.search(r'\d{4}-\d{1,2}-\d{1,2}', row[0])
	if x:
		NYT_withaDate.append(row)


#[Joining] Merge recovery data from John Hopkin's dataset into NYT's dataset
#[Filtering] Remove the data without matching dates in both dataset
NYTandJohn = []
NYTandJohn.append(['Date', 'Cases', 'Deaths', 'Recoveries'])
for n in NYT_withaDate:
	for j in John_US:
		if (n[0]==j[0]):
			tempList = n + [j[4]]
			NYTandJohn.append(tempList)
			break


# The result would be printed to the output once to ensure that the dataset is correct
# Check the output
for z in NYTandJohn:
	print (z)


# Export file into an excel file (csv) for higher readibility
with open("merge.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(NYTandJohn)