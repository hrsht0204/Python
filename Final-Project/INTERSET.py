import math

while True:
    try:
        # Input Principal
        P_input = input("PRINCIPLE (or press Enter to skip): ")
        p = (P_input)
        if (P_input == ""):
            
            N_input = input("Compunded in every(months)")
            n= float(N_input)
            
            R_input = input("RATE: ")
            r = float(R_input) 
            # Input Time
            T_input = input("TIME: ")
            t = float(T_input) 
            # If Principal is missing, ask for the Final Amount
        
            A_input = float(input("enter the FINAL AMOUNT: "))
            
            p = A_input / (1 + (r / n))**(n* t)
            print("your principal is :" + p)
      # Input Rate
        R_input = input("RATE (or press Enter to skip): ")
        R = float(R_input) 
        if (R_input == " "):
            
            N_input = input("Compunded in every(months)")
            N= float(N_input)
            
            R_input = input("RATE (or press Enter to skip): ")
            R = float(R_input) 
    
            # Input Time
            T_input = input("TIME (or press Enter to skip): ")
            T = float(T_input) 
    
            # If Principal is missing, ask for the Final Amount
        
            A_input = float(input("enter the FINAL AMOUNT: "))
            
            A = P = A_input / (1 + (R / N))**(N * T)

        # Input Time
        T_input = input("TIME (or press Enter to skip): ")
        T = float(T_input) 

        # If Principal is missing, ask for the Final Amount
    
        A_input = input("enter the FINAL AMOUNT: ")
        A = float(A_input)
        
        N_input = input("Compunded in every(months)")
        N= float(N_input)
        

        # Check if user wants to calculate CI
        if P is not None and A is not None:
            H = input("Calculate Compound Interest (y/n)? ").strip().lower()
            if H == "y":
                CI = A - P
                print(f"Compound Interest (CI): {CI:.2f}")
            elif H == "n":
                break
        else:
            print("Can't calculate CI without both Principal and Amount.")

        # Exit prompt
        cont = input("Do you want to perform another calculation (y/n)? ").strip().lower()
        if cont != "y":
            break

    except ValueError:
        print("Invalid input! Please enter valid numbers.")
