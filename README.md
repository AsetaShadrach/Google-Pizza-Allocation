# Google-Pizza-Allocation 
## (Using equal group allocation)
The idea behind this is that each team size , in this case 4/3/2 gets allocated almost equal allocations.
That is, after allocation a 4 member team pizzas, next will be a 3 member team then a 2 member team then back to 4 then 3 then 2. 
But also at the same time trying to increae the variance within the teams, i.e team gets pizzas with different pizza ingredients
(The statement above will become more clear after reading the practice pdf)

## Note 
This is not the most optimal solution with regards to the score method described in the pdf
The method i use to determin allocation based on variance takes too long (2+ hours) for 100,000 pizzas
- This is because i have to repeatedly determine which of the remaining pizzas results in the highest variance
- Any help reducing it will be highly appreciated
