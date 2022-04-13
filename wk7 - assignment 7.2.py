7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
        X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average
of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
sum = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                sum = sum + float(line[20:])
                count = count + 1

print("Average spam confidence:", sum/count)

#UPDATED APR 13 2022: without using sum() function 
fname = input("Enter file name: ")
fh = open(fname)
total = 0.0
count = 0

for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") :
                continue
        else:
                total = total + float(line[20:])
                count = count + 1

print("Average spam confidence:", total/count)
