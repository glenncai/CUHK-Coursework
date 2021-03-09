NAME: Cai Long Hua
SID: 1155126875
Class ID: 1


1. I edited the Edges.csv file on blackboard to sociomatrix.csv (check in the folder)
2. I found a total of 9 class IDs without commenting on anyone, including 24,34,41,45,64,71,75,82,87 (So their relative rows are all 0).


Run program:
step1: Open the CMD.
step2: Run in CMD, it takes a long time to run because the direct graph is being generated.
step3: If running fail, please try again.
step4: Close the graph windows and see the values of in-degree, out-degree, closeness centrality and shortest-path betweenness(betweenness centrality) on CMD screen.


From the result values showing on the CMD screen, the out-degree of node 1 is 14, 
because I commented on blogs with class ID of 3, 5, 6 (commented this two times, just count as value 1), 11, 13, 16, 22, 25, 45, 56, 73, 76, 83, 88
Then, the in-degree of node 1 is 19, it means that there are 19 classmates commented my blog, 
they are 8, 12, 19, 27, 28, 32, 36, 42, 51, 56, 57, 59, 62, 63, 66, 74, 76, 84, 88.


More details, please see CMD screen...


Source code reference:
https://networkx.org/documentation/stable/tutorial.html
https://whitakerlab.github.io/scona/_modules/scona/classes.html
https://stackoverflow.com/questions/49683445/create-networkx-graph-from-csv-file-in-python-3
