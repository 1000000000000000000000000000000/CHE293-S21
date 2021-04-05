import sys
import pandas as pd

'''
####################################################################################################
To use this script:

python output_to_csv.py [INPUT TYPE] [SEQUENCE NAME] [INPUT VALUES]

Example:

python output_to_csv.py e6 1aa7 0.10000094301032349,0.8701883352082787,0.053361433898144774,
0.053092652126686124,0.1940914724635971,0.9483219853442273,0.3306576724498245,0.6879327099561908,
1.2548325790728785,0.07668346215539201,0.1396246476315025,0.27523407620439627,0.012628703101327032,
0.10997895755054084,0.03559891746031243,0.2870047965449099,0.11392988629966698,0.20413947585217165,
0.14582306776830062,0.11202065669472744,0.37565077552345605

Note:

The output of the above example is a file called "e6_1aa7.csv" located in the current working
directory.

If there are problems with this script please contact: richard.pearson@sjsu.edu

#####################################################################################################
'''

sequence_name = sys.argv[2]

input_length = len(sys.argv[3])
input = sys.argv[3][0:input_length]
input = input.split(',')

input_type = sys.argv[1]

# make output list variable
output = []

# loop through the input and append to list
for number in input:
    output.append(number)

# generate dataframe
df = pd.DataFrame()
df[str(input_type)] = output

# prints dataframe to terminal (testing purposes)
print(df)

# generate the csv with the output values
df.to_csv(str(input_type)+'_'+str(sequence_name)+'.csv')
