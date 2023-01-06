from IPython.display import clear_output




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


            
            
            
def us():
    
    figure = 'WRONG'
    
    
    while figure.isdigit()==False:
        
    
        figure = input('Please input annual salary ($):')   
            
        if figure.isdigit()==False:
        
            print('Please choose a digit, not a letter.')
                  
                  
    else:  
        
        
        
        #TAX
        #Income Tax
        max_tax10 = 9950*0.1
        max_tax12 = ((40525-9951)*0.12)+max_tax10
        max_tax22 = ((86375-40526)*0.22)+max_tax12
        max_tax24 = ((164925-86376)*0.24)+max_tax22
        max_tax32 = ((209425-164926)*0.32)+max_tax24
        max_tax35 = ((523600-209426)*0.35)+max_tax32
        
        #Taxed Amount
        sum_10 = 9950*0.9
        sum_12 = ((40525-9950)*0.88)+sum_10
        sum_22 = ((86375-40526)*0.78)+sum_12
        sum_24 = ((164925-86376)*0.76)+sum_22
        sum_32 = ((209425-164956)*0.68)+sum_24
        sum_35 = ((523600-209426)*0.65)+sum_32
        
        
        
        #10%
        if int(figure)<9950:
            
            income_tax = int(figure)*0.1
            taxed_amount = int(figure)-(int(figure)*0.1)
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income tax:', "{:.2f}".format(income_tax))
                    
        #12%
        if int(figure) in range(9951,40525):
            
            income_tax = ((int(figure)-9950)*0.12)+max_tax10
            taxed_amount = ((int(figure)-9950)*0.88)+sum_10
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income tax:', "{:.2f}".format(income_tax))
            
        #22%
        if int(figure) in range(40526,86375):
            
            income_tax = ((int(figure)-40525)*0.22)+max_tax12
            taxed_amount = ((int(figure)-40525)*0.78)+sum_12
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income tax:', "{:.2f}".format(income_tax))
        
        #24%
        if int(figure)in range(86376,164925):
            
            income_tax = ((int(figure)-86375)*0.24)+max_tax22
            taxed_amount = ((int(figure)-86375)*0.76)+sum_22
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
        
        #32%
        if int(figure) in range(164926,209425):
        
            income_tax = ((int(figure)-164925)*0.32)+max_tax24
            taxed_amount = ((int(figure)-164925)*68)+sum_24
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income tax:', "{:.2f}".format(income_tax))
        
        #35%
        if int(figure) in range(209426,523600):
        
            income_tax = ((int(figure)-209425)*0.35)+max_tax32
            taxed_amount = ((int(figure)-209524)*65)+sum_35
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
                    
        #37%
        if int(figure) > 523600:
        
            income_tax = ((int(figure)-523600)*0.37)+max_tax35
            taxed_amount = ((int(figure)-523600)*0.63)+sum_35
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
            
 



def china():
    
    figure = 'WRONG'
    
    
    while figure.isdigit()==False:
        
    
        figure = input('Please input annual salary (¥):')   
            
        if figure.isdigit()==False:
        
            print('Please choose a digit, not a letter.')
                  
                  
    else:  
        
        #Tax
        max_tax3 = 36000*0.03
        max_tax10 = ((144000-36000)*0.1)+max_tax3
        max_tax20 = ((300000-144000)*0.2)+max_tax10
        max_tax25 = ((420000-300000)*0.25)+max_tax20
        max_tax30 = ((660000-420000)*0.3)+max_tax25
        max_tax35 = ((960000-660000)*0.35)+max_tax30
        
        #Taxed Amount
        sum_3 = 36000*0.97
        sum_10 = ((144000-36000)*0.9)+sum_3
        sum_20 = ((300000-144000)*0.8)+sum_10
        sum_25 = ((420000-300000)*0.75)+sum_20
        sum_30 = ((660000-420000)*0.7)+sum_25
        sum_35 = ((960000-660000)*0.65)+sum_30
        
    
        if int(figure) in range(0,36000):
            
            income_tax = int(figure)*0.03
            taxed_amount = int(figure)*0.97
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
    
        if int(figure)in range(36000,144000):
            
            income_tax = ((int(figure)-36000)*0.1)+ max_tax3
            taxed_amount = ((int(figure)-36000)*0.9)+ sum_3
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))

        if int(figure) in range(144000,300000):
        
            income_tax = ((int(figure)-144000)*0.2)+ max_tax10
            taxed_amount - ((int(figure)-144000)*0.8) + sum_10
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
    
        if int(figure) in range(300000,420000):
        
            income_tax = ((int(figure)-300000)*0.25)+max_tax20
            taxed_amount = ((int(figure)-30000)*0.75)+sum_20
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
    
        if int(figure) in range(420000,660000):
        
            income_tax = ((int(figure)-420000)*0.3)+max_tax25
            taxed_amount = ((int(figure)-420000)*0.7)+sum_25
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
    
        if int(figure) in range(660000,960000):
        
            income_tax = ((int(figure)-660000)*0.35)+max_tax30
            taxed_amount = ((int(figure)-660000)*0.65)+sum_30
            
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
        
        if int(figure) > 960001:
        
            income_tax = ((int(figure)-960000)*0.45)+max_tax35
            taxed_amount = ((int(figure)-960000)*0.55)+sum_35
        
            print('Pay after tax:', "{:.2f}".format(taxed_amount))
            print('Income Tax:', "{:.2f}".format(income_tax))
  
        
    
    
    
    
    
def CountrySelection():
    
    country = ''
    countries = (['us', 'united kingdom', 'united states', 'uk', 'china'])
    usa = ('us','united states')
    u_k = ('uk','united kingdom')
    chinese = ('china')
    
    country = input('Please choose a country, UK, US or China:').lower()
    
    while country.isdigit() or country not in countries:
        
        clear_output()
        print('Invalid Country')
        country = input('Please choose a country, UK, US or China:').lower()
    
    else:
        if country in usa:
            return clear_output(),us()
    
        elif country in u_k:
            return clear_output(),uk()
    
        elif country in chinese:
            return clear_output(),china()  
         
            

 

def Homepage():
    
    print("Del Boy's Tax Calculator")
    
    
    
    
    
    
 def ReturnHome():
    
    choice = 'wrong'
    
    choice = input('Return to homepage? Yes/No:').lower()
    
    while choice.isdigit()==True or choice != 'yes' and choice != 'no':
        
        choice = input('Return to homepage? Yes/No:').lower()
        
        
    else: 
        if choice == 'yes':
            return clear_output(),DelsCalculator()
        
        if choice == 'no':
            print("Chateauneuf du pape, Rodney. We're millionaires")
    
    
    
    
    
def DelsCalculator():#Home page
    

    Homepage()
    
    #Country Selection
    
    CountrySelection()
    
    
    #Input figure
    
    #Would you like to return to homepage
    ReturnHome()
    
   



DelsCalculator()
