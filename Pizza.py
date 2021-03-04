import timeit

class Pizza():
    def __init__(self):
        self.submission_list = list()
        self.start_time = timeit.default_timer()

    def unda_data(self , path):
        file = open(path,'r') 
        content = file.read()
        file_lines = content.split('\n')
        pizza_and_teams = file_lines[0].split(' ')
        self.pizza_ingredients_list = list(map(lambda x: x.split(' ')[1:],file_lines[1:]))
        self.pizza_ingredient_count_list = list(map(lambda x : int(x.split(' ')[0]),file_lines[1:]))
        number_of_pizzas = int(pizza_and_teams[0])
        self.member2_teams = int(pizza_and_teams[1])
        self.member3_teams = int(pizza_and_teams[2])
        self.member4_teams = int(pizza_and_teams[3])
        total_members = self.member2_teams*2 + self.member3_teams*3 + self.member4_teams*4
        self.number_of_iterations = min(total_members,number_of_pizzas) #pick pizza/people to iterate through depending on which is less
        
    def allocate_pizza(self):
        while self.number_of_iterations > 11 : # sum of 2+3+4 +2 , to cater of a case like 10 
                                           # which will have a remainder of 1, thus cause an infinite loop  
            if self.member4_teams > 0 : 
                self.individual_team_allocation(4)

            if self.member3_teams > 0 :
                self.individual_team_allocation(3)

            if self.member2_teams > 0 :
                self.individual_team_allocation(2)
        
        #when the sum goes below 9 ; this ensures that all vailable pizzas are given out or all mebers get a pizza if pizzas are more
        while self.number_of_iterations > 0 : #pick best combination to finish without a remaining pizza/member to serve in a team
            for team_size in [2,3,4]:
                if self.number_of_iterations % 2 == team_size % 2 and self.number_of_iterations >= team_size :# odd vs_even
                    self.individual_team_allocation(team_size)
                                
            
        return 

    def individual_team_allocation(self, no_of_members):
        #append submission string for each allocation to the submission list
        subm_str = str(no_of_members)+' '+' '.join( [str(i) for i in range( self.number_of_iterations, self.number_of_iterations - no_of_members, -1 )]  )
        self.submission_list.append(subm_str)
        if no_of_members == 4:
            self.member4_teams -= 1
        if no_of_members == 3:
            self.member3_teams -= 1
        if no_of_members == 2:
            self.member2_teams -= 1                    
        del self.pizza_ingredients_list[-no_of_members:]
        self.number_of_iterations-= no_of_members
            


    def output_data(self,output_file_name):
        self.allocate_pizza()
        file =  open(output_file_name,'w')
        file.write(str(len(self.submission_list))) #number of teams served
        file.write("\n")
        for i in self.submission_list:
            file.write(i)
            file.write('\n')
        file.write("\n\nTime it took : ")
        file.write(str(timeit.default_timer() - self.start_time))
        file.close()



pizza_allocation = Pizza()
pizza_allocation.unda_data('e_many_teams.in')
pizza_allocation.output_data('e py submission file.out')



