# River Crossing

**Introduction**

If you like logic puzzles or are a student of computer science (why, hello!), you've probably heard of river crossing problems such as: The Jealous Husbands; Fox, Goose and Bag of Beans; Wolf, Goat and a Cabbage; or the Missionaries and Cannibals problem.

We'll be looking at the Missionaries and Cannabals problem, which is typically stated something like this:

Three missionaries and three cannibals must cross a river using a boat, which can carry at most two people. There is a constraint that, for both banks, if there are missionaries present on the bank, they cannot be outnumbered by cannibals. (If they were, the cannibals would eat the missionaries.) 

How can the boat be used to safely carry all the missionaries and cannibals across the river?
There are only two valid moves in the game: Boat crossing with X missionaries and Y cannibals and boat returning with X missionaries and Y cannibals.

A solution for that particular problem (in case you haven't worked it out in your head)

![Sample Example](https://lh3.googleusercontent.com/-TjU5qmXI_js/VzPnV93IeyI/AAAAAAAAsKI/L4A734vhYhQjNCMp0pS-IzN-x70BwrvMACLcB/s0/missionaryproblem.PNG "missionaryproblem.PNG")

Easy, right? You could do that without a computer in your head. Now, what about the more generalized case of this problem?

**The Generalized Missionaries and Cannibals Problem**

Given M missionaries, C cannibals, and P people per boat capacity, give the sequence of actions for crossing the river safely.

**Some notes:**
   -  For scenarios of P >=3, if there are missionaries present on the boat, they cannot be outnumbered by cannibals. (Same rule as the banks)
   -  After a boat crossing, all passengers must disembark onto the shore, therefore a boat cannot be used as a safe place. The boat cannot cross the river by itself. 
   -  You need at least one rower. 
   -  Not EVERY combination of M, C, and P is solvable. 
   -  Solutions are not necessarily unique, but your solution must be a minimum crossings solution.

**The Problem**
 
Write the solver described above, and then use it to solve the following problems. They are written as M C P. 
So, the classic problem is written like 3 3 2 for 3 missionaries, 3 cannibals, and a boat capacity of 2.

Your solution should be, for each test case, some text that looks basically like the output you see above, which includes:

\# missionaries, \# cannibals on the originating bank
\# missionaries, \# cannibals on the destination bank
\# missionaries, \# cannibals on the boat
direction the boat is heading

The text doesn't have to be exactly the same as the sample solution for the above example, but your solution must meet all of the requirements for the solution and the submission. If the problem has no valid solution, simply state that the problem has no solution.

