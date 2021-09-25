Authored by Michael Stepzinski

Decision Trees
	DT_train_binary implementation
		This function uses helper functions to implement the desired functionality. These helper functions are: calculate_entropy, find_split_entropy, table_checker, and findIG. Calculate entropy finds the entropy of the entire set in the beginning of the problem. Find split entropy finds the entropies of each split and traverses the tree as it is built to put decisions in the proper place. Table checker is the tree traversal mechanism, it essentially checks for entries not yet assigned to be a 'No' or a 'Yes' and uses those to continue building the tree. Find IG finds the Information Gain of a decision.
		The function loops iteratively, until max_depth is reached, all features are solved, or an explicit stop command is given. The function starts by calculating total entropy and setting helper variables to a blank state. Then each feature is looked at and information gain is calculated. The function splits on the highest information gain. The tree is built using this decision. This process repeats until the above stated features, or until information gain is 0. This was primarily tested using the dataset from the Netflix example in class.

	DT_test_binary implementation
		Test binary is essentially a wrapper over a for loop that calls DT_make_prediction and checks if the predicted value is the same as the actual value.

	DT_make_prediction implementation
		Make prediction loops over the tree that was created and returns the value of a decision instruction.


Nearest Neighbors
	KNN_test implementation
		This function has multiple looping steps. First it calculates the distance of all values in X_Val from X_train. Then it finds the K closest neighbors by utilizing the min function and the indices of the neighbors with the smallest distance. Then all neighbor y values are added up, and the function checks if they are greater than 0, less than 0, or equal to 0. This process happens in a loop. If equal to 0, then the function defaults to 1. To get a total accuracy, the calculated  y values are compared to the true Y values from Y_val.

Clustering
	K_Means implementation
		K means was not implemented, I spent too much time on the decision tree and ran out of time :(