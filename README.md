# Lottery-Simulator  
This is a practice lottery simulator that can be set to your likings.  
**Note:**  
      -This is not a real lottery, you cant actually play it but just see its "real" odds  
      -The random module in python can never be fully random.  
      -There is no kind of mega ball.        
       
      
**How to use:**      
          
balls_amount: in a real lottery there are different balls to set the lottery outcome, the same here.  
You can simply set the amount of balls used in this simulation.  
The tries needed for winning increase drastically with every ball and the execution time too.         
      
max_number_amount: this sets the max amount of numbers on every ball.  
The higher, the longer the execution time.  
  
lotteries_amount: this is basically how often your lottery should be done.  
If you set it on five for example, it will do five lotteries and calculates the avg tries at the end.   
    
print_intermediate_results: this sets if you want to print the results of every lottery or if you just want the avg results.  
Its recommended to turn this on, but it will always increase the execution time.   
     
    
**How the code works:**  
      
The code will generate two random combinations of balls every single time that have to be equal to continue.  
When the combinations are equal, the tries get printed if (print_intermediate_results) is true or if it's just a single lottery.     






      
      
