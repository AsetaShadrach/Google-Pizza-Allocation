# Google-Pizza-Allocation 
## Using equal group allocation
The idea behind this is that each team size , in this case 4/3/2 gets allocated almost equal allocations.
That is, after allocation a 4 member team pizzas, next will be a 3 member team then a 2 member team then back to 4 then 3 then 2. 
But also at the same time trying to increae the variance within the teams, i.e team gets pizzas with different pizza ingredients
(The statement above will become more clear after reading the practice pdf)

## Note 
This is not the most optimal solution with regards to the score method described in the pdf

### (case 1) *While checking to increase variance*
- Here we allocate a pizza to an individual in a group, then for the next pizza in the same group , we try to select a pizza that will add the most number of ingredients that aren't already in the group i.e increase the variance
- This method takes quite a while to run : around 2+ hours for 100,000 pizzas
- This is because i have to repeatedly determine which of the remaining pizzas results in the highest variance
- Files : Pizza Notebook.ipynb , e submission file.out
       
### (case 2) *Without checking to increase variance*
- Here we do the same treversal as above minus checking of the variance
- This one takes a short time ,0.5 seconds , and could be shorter if you opt for the direct code instead of using function calls(0.3 or 0.4 seconds) , but i used fuctions just for neatness
- You simply allocate the pizzas as they appear on the list from either top to bottom or bottom to top
- Files : Pizza.py , e py submission file.out
___
___

- A method to increase score could be , using non uniform allocation : Giving 2 member teams until all 2 member teams are over(you'll have more numbers to square)
 
- Any input on how to reduce the runtime of the 2hour code while maininng the same funtionality is highlly appreciated
