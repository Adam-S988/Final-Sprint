import datetime



def program8():  

    def HighestVolumeDate(Date):
        FormattedDate = ""
        with open("rentalrevenue.dat", "r") as file:
            for line in file:
                if Date in line:
                        DateObject = datetime.datetime.strptime(Date, "%Y/%m/%d")
                        FormattedDate = DateObject.strftime("%Y/%m/%d") 
                        break
                
        return FormattedDate

    def LowestVolumeDate(Date):
        FormattedDate2 = ""
        with open("rentalrevenue.dat", "r") as file:
            for line in file:
                if Date in line:
                        DateObject2 = datetime.datetime.strptime(Date, "%Y/%m/%d")
                        FormattedDate2 = DateObject2.strftime("%Y/%m/%d") 
                        break
                
        return FormattedDate2

    def HighestExpensedItem(ItemNumber):
        ExpensedItem = ""
        with open("Supplies.dat", "r") as file:
            for line in file:
                if ItemNumber in line:
                    return ItemNumber
                    

    def LowestExpensedItem(ItemNumber2):
        ExpensedItem2 = ""
        with open("Supplies.dat", "r") as file:
            for line in file:
                if ItemNumber2 in line:
                    return ItemNumber2
                    
    def HighestRentalRevenue(Date3):
        FormattedDate3 = ""
        with open("rentalrevenue.dat", "r") as file:
            for line in file:
                if Date3 in line:
                        DateObject3 = datetime.datetime.strptime(Date3, "%Y/%m/%d")
                        FormattedDate3 = DateObject3.strftime("%Y/%m/%d") 
                        break
                
        return FormattedDate3
                
    def LowestRentalRevenue(Date4):
        FormattedDate4 = ""
        with open("rentalrevenue.dat", "r") as file:
            for line in file:
                if Date4 in line:
                        DateObject4 = datetime.datetime.strptime(Date4, "%Y/%m/%d")
                        FormattedDate4 = DateObject4.strftime("%Y/%m/%d") 
                        break
                
        return FormattedDate4
    
    HighestDateNeeded = HighestVolumeDate("2024/01/05")
    LowestDateNeeded = LowestVolumeDate("2024/01/01")
    HighestExpensedItemNeeded = HighestExpensedItem("111221")
    LowestExpensedItemNeeded = LowestExpensedItem("111121")
    HighestRentalRevenueNeeded = HighestRentalRevenue("2024/01/05")
    LowestRentalRevenueNeeded = LowestRentalRevenue("2024/01/08")

    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("                                         MONTHLY HIGHLIGHT REPORT")
    print("-----------------------------------------------------------------------------------------------------------")
    print("                                          HAB TAXI SERVICE")
    print("                                          442 MONTREAL ST")
    print("                                        ST. JOHN'S NL, A1A1A1")
    print("                                            (709) 907-7979")
    print("-----------------------------------------------------------------------------------------------------------")
    print("                             MONTHLY HIGHLIGHTS FROM 2024/01/01 - 2024/01/31")
    print()
    print("   HIGHLIGHT SUMMARY:")
    print("-----------------------------------------------------------------------------------------------------------")
    print("   RENTAL NUMBERS:")
    print()
    print(f"   HIGHEST VOLUME DAY:     {HighestDateNeeded:<10s}")       
    print(f"   LOWEST VOLUME DAY:      {LowestDateNeeded:<10s} ") 
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("   EXPENSED ITEMS:")
    print()
    print(f"   MOST EXPENSED ITEM:     {HighestExpensedItemNeeded:<6s}")
    print(f"   LEAST EXPENSED ITEM:    {LowestExpensedItemNeeded:<6s}")
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("   RENTAL REVENUE:")
    print()
    print(f"   HIGHEST RENTAL REVENUE DAY: {HighestRentalRevenueNeeded:<10s} ")
    print(f"   LEAST RENTAL REVENUE DAY:   {LowestRentalRevenueNeeded:<10s}")
    print()
    print("-----------------------------------------------------------------------------------------------------------")
    print("   HIGHLIGHT SUMMARY:")
    print()
    print(f"   HIGHEST VOLUME DAY:         {HighestDateNeeded:<10s}") 
    print(f"   MOST EXPENSED ITEM:         {HighestExpensedItemNeeded:<6s}")
    print(f"   HIGHEST RENTAL REVENUE DAY: {HighestRentalRevenueNeeded:<10s}")
    print("-----------------------------------------------------------------------------------------------------------")
    print("                                      * * * * * END OF REPORT * * * * *")
    print()
    input(f"PRESS ENTER TO CONTINUE TO MAIN MENU")