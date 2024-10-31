 import  math 
 from  decimal  import  Decimal, getcontext 
 # Set precision for Decimal calculations 
 getcontext().prec =  20  # You can adjust this value  for even higher precision 
 def  is_prime(num): 
 """  Check if a number is prime.  """ 
 if  num  <=  1  : 
 return  False 
 for  i  in  range  (  2  ,  int  (num  **  0.5  )  +  1  ): 
 if  num  %  i  ==  0  : 
 return  False 
 return  True 
 def  calculate_primes_ratio(x): 
 """  Calculate the ratio of prime numbers up to  x using the specified method.  """ 
 primes = [] 
 x = Decimal(x)  # Use Decimal for high precision 
 limit = Decimal(math.sqrt(x))  +  1 
 # Finding primes less than or equal to sqrt(x) 
 for  num  in  range  (  2  ,  int  (limit)): 
 if  is_prime(num): 
 primes.append(Decimal(num)) 
 # Calculate composite contributions using the  formula C(x) 
 C = Decimal(  0  )  # Total composite contributions 
 previous_C = Decimal(  0  )  # C_i for previous iterations 
 for  k  in  range  (  len  (primes)): 
 P_k = primes[k] 
 # Calculate the current contribution to C  based on previous contributions 
 C  +  = (Decimal(  1  )  /  P_k)  *  (Decimal(  1  )  -  previous_C) 
 previous_C  +  = (Decimal(  1  )  /  P_k)  *  ( 
 Decimal(  1  )  -  previous_C 
 )  # Update previous C 
 # Calculate the ratio of prime numbers P(x) 
 k = Decimal(  len  (primes))  # Total number of primes  found 
 C  -  = k  /  x 
 P_x = Decimal(  1  )  -  C 
 return  P_x 
 # Main function to prompt for input and calculate the ratio of primes 
 def  main(): 
 x =  int  (  input  (  "  Enter the upper bound (x):  "  )) 
 prime_ratio = calculate_primes_ratio(x) 
 print  (  f"  Estimated ratio of prime numbers from  1 to  {  x  }  :  {  prime_ratio  }"  ) 
 print  (  f"  Estimated number of prime numbers from 1 to  {  x  }  :  {  round  (prime_ratio  *  x)  }"  ) 
 if  __name__  ==  "  __main__  "  : 
 main() 
