# python-challenge

In the PyBank challenge I had the task to analyze the financial data of a company. 

The following are a list of things that I had to find

#The total number of months included in the dataset

  I made a for loop to get the total months count by just adding 1 with the starting value of zero.

#The net total amount of "Profit/Losses" over the entire period

  The toal amount of Profit/Losses was calculated by using the same for loop but by only adding interger values in the rows to get the net total.

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
  
  In the first for loop I also added the dates into a list for each row and the profit for each indidividual row into a list.
  By doing this I was able to git the changes in profit/losses and the average as well. I created a formula to get the difference between each row. These differences were then added all together and divded by the length of the rows.

#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

Since the greatest decrease was a negative number I could use zero in order to compare increase and decrease. Using the for loop I could compare increases and decreases to find the largest ones.

I didn't have enough time to start the other challenge. I'm planning on resubmitting this assignment. 
