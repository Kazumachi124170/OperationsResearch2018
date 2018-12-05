Use Simulated Annealing(SA) algorithm to solve the Traveling Salesman Problem
	* Simulated Annealing(SA) algorithm
		1. Set the maximum iteration times(n), temperature(temper), and cooling rate(cRate).
			In my code, I set the initial temperature 1000, and cooling rate 0.999
		2. Set the Initial path(path), and calculate the old solution(F).
			In my code I set [1,2,3,...,16,17,1]
		3. Randomly select 2 city and swap them, create a new path(npath), and calculate the new solution
		4. When the new solution(nF) is smaller than the old solution, set the old solution become new solution, record the path (in anspath) and solution (in ans).
			When the new solution is not, random a number, if the random number is bigger than the temperature, set the old solution become new solution, if it isn't, do nothing 
			
		5. Go to step 3 until reach the maximum iteration.
