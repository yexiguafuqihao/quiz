## The solution to the mid-term quiz
1. Converting seconds into standard time format.

Convert the input seconds to days/hours/minutes/seconds. Singular and plural nouns need to be considered in the output format.

2. Write a program to find the sum of the digits of an integer.

The program takes a string of integers as input, iterates over each character in the string, converts each character into an integer, and sums them together. Also, the output format should be built carefully.

3. Find the median number of a given array.

Firstly, parse the input string into a list of numbers. Then sort them in ascending order. Finally, returns the median in the sorted array, as defined by the median.

4. Circular shift array

The given position k partitions a given array into 2 parts. And the 2 parts need to be swapped. Take the circular right shift as example. It first needs to partition a given array/list into 2 parts according to the given k, then the 2 parts needs to be swapped. After swap, the first part needed to be reversed to produce the final result. Therefore, we can reverse the 2 splits at first, respectively. Then reverse the whole array. The final result can be obtained. Because the 2 reversion conducted on the 2 parts has been canceled out.


5. Output the most frequently occurred words in a given string.

Firstly, count the frequency of each word in the given string.
Secondly, sort the unique words in alphabetic order.
Thirdly, find out the largest frequency from the sorted unique words.
Finally, output those words whose frequency higher than the equals to the largest frequency.
