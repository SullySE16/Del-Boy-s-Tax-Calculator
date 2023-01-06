def uk():
    
    figure = 'WRONG'
    
    while figure.isdigit()==False:
    
        figure = input('Please input annual salary (£):')
        
        if figure.isdigit()==False:
            print('Please ensure you use numbers, not letters.')
            
        
    else:
        
        figure.isdigit()==True
        
        #NATIONAL INSURANCE
        
        NI_primary_threshold = (int(figure)-9568)*0.12
        NI_upper_earnings_limit = (int(figure)-50284)*0.02
        
        
        NI_bracket12 = (50284-9568)*0.12
        
            
        #TAX DEDUCTIONS
        
        bracket20_total = ((50270-12570)*0.8)+12570
        bracket40_total = (150000-bracket20_total)*0.6+bracket20_total
        
        max_income_tax20 = (50270-12570)*0.2
        max_income_tax40 = (150000-50270)*0.4
        
        
        

        #NO TAX
        if int(figure)<12570:
            if int(figure) in range(9568,12570):
                taxed_amount0 = int(figure)- NI_primary_threshold
                print('Pay after tax:', "{:.2f}".format(taxed_amount0))
                print('National Insurance:', "{:.2f}".format(NI_primary_threshold))
                print('Income Tax:', '0.00')
                
            if int(figure)<9568:
                taxed_amount0 = int(figure)
                print('Pay after tax:', "{:.2f}".format(taxed_amount0))
                print('National Insurance:', '0.00')
                print('Income Tax:', '0.00')
        
        
        
        
        #20%
        if int(figure) in range(12571,50271):
            
            income_tax1 = (int(figure)-12570)*0.2
            taxed_amount1 = (int(figure) - ((int(figure)-12570)*0.2))-NI_primary_threshold
            print('Pay after tax:', "{:.2f}".format(taxed_amount1))
            print('National Insurance:', "{:.2f}".format(NI_primary_threshold))
            print('Income Tax:', "{:.2f}".format(income_tax1))

        
        
        
        
        #40%
        
        if int(figure) in range(50271,50284):
            
            income_tax2 = ((int(figure)-50271)*0.4)+max_income_tax20
            taxed_amount2 = (int(figure) - (((int(figure)-50270)*0.4))-max_income_tax20)-NI_primary_threshold
            print('Pay after tax:', "{:.2f}".format(taxed_amount2))
            print('National Insurance:', "{:.2f}".format(NI_primary_threshold))
            print('Income Tax:', "{:.2f}".format(income_tax2))
            
        if int(figure) in range(50284,150000):
            
            NI40 = NI_bracket12+NI_upper_earnings_limit
            income_tax2 = ((int(figure)-50271)*0.4)+max_income_tax20
            taxed_amount2 = (int(figure) - (((int(figure)-50270)*0.4))-max_income_tax20)-(NI_bracket12+NI_upper_earnings_limit)
            print('Pay after tax:', "{:.2f}".format(taxed_amount2))
            print('National Insurance:', "{:.2f}".format(NI40))
            print('Income Tax:', "{:.2f}".format(income_tax2))
                     
        
        
        
        
        #45%
        if int(figure) > 150000:
            
            NI40 = NI_bracket12+NI_upper_earnings_limit
            income_tax3 = ((int(figure)-150000)*0.45)+(max_income_tax40+max_income_tax20)
            taxed_amount3 = (int(figure) - ((int(figure)-150000)*0.45))-(max_income_tax40+max_income_tax20)-(NI_bracket12+NI_upper_earnings_limit) 
            print('Pay after tax:', "{:.2f}".format(taxed_amount3))
            print('National Insurance:', "{:.2f}".format(NI40))
            print('Income Tax:', "{:.2f}".format(income_tax3))
