def program6():
                
# ------------------------------ RENTAL REVENUE ------------------------------------------------------

        # Pulling the transaction sub-total, and formatting it.

        def Format_Rental_Sub():
            with open("rentalrevenue.dat", "r") as file:
                SubTotalLst = []
                RentSubTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 4:
                        SubTotal = float(Parts[3])
                        RentSubTotalDsp = "${:.2f}".format(SubTotal)
                        SubTotalLst.append(SubTotal)
                RentSubTotals = sum(SubTotalLst)
                RentSubTotalsDsp = "${:.2f}".format(RentSubTotals) 
            return RentSubTotalDsp, RentSubTotalsDsp, RentSubTotals

        # Pulling HST and formatting it
        def Format_Rental_HST():
            with open("rentalrevenue.dat", "r") as file:
                HSTLst = []
                RentHSTDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 5:
                        HST = float(Parts[4])
                        RentHSTDsp = "${:.2f}".format(HST)  
                        HSTLst.append(HST)
                RentHSTTotals = sum(HSTLst)
                RentHSTTotalsDsp = "${:.2f}".format(RentHSTTotals) 
            return RentHSTDsp, RentHSTTotalsDsp, RentHSTTotals

        # Pulling Total and formatting it
        def Format_Rental_Tot():
            with open("rentalrevenue.dat", "r") as file:
                TotalLst = []
                RentTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 6:
                        Total = float(Parts[5])
                        RentTotalDsp = "${:.2f}".format(Total) 
                        TotalLst.append(Total)
                RentTotals = sum(TotalLst)
                RentTotalsDsp = "${:.2f}".format(RentTotals) 
            return RentTotalDsp, RentTotalsDsp, RentTotals

        # Pulls the date, Transaction ID and Driver ID from .dat
        def Read_Rental_Data():
            RentalData = []
            with open("rentalrevenue.dat", "r") as file:
                    for line in file:
                        Parts = line.strip().split(',')
                        if len(Parts) >= 4:
                            RentalDate = Parts[0]
                            TransID = Parts[1]
                            DrivID = Parts[2]
                            subtotal = Parts[3]
                            paymentHST = Parts[4]
                            paymentTotal = Parts[5]
                            RentalData.append((RentalDate, TransID, DrivID, subtotal, paymentHST, paymentTotal))
            return RentalData

        # Call functions
        RentSubTotalDsp, RentTotalsDsp, RentSubTotals = Format_Rental_Sub()
        RentHSTDsp, RentHSTTotalsDsp, RentHSTTotals = Format_Rental_HST()
        RentTotalDsp, RentTotalsDsp, RentTotals = Format_Rental_Tot()
        RentalData = Read_Rental_Data()


 #----------------------------------------------------------------------------------------------------


# ------------------------------ PAYMENT REVENUE -----------------------------------------------------


        # Pulling the transaction subtotal, and formatting it.
        def Format_Payment_Sub():
            with open("paymentrevenue.dat", "r") as file:
                SubTotalLst = []
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 4:
                        SubTotal = float(Parts[3])
                        PaySubTotalDsp = "${:.2f}".format(SubTotal)
                        SubTotalLst.append(SubTotal)  
                PaySubTotals = sum(SubTotalLst)  
                PaySubTotalsDsp = "${:.2f}".format(PaySubTotals)
            return PaySubTotalDsp, PaySubTotalsDsp, PaySubTotals

        # Pulling HST and formatting it
        def Format_Payment_HST():
            with open("paymentrevenue.dat", "r") as file:
                HSTLst = []
                PayHSTDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 5:
                        HST = float(Parts[4])
                        PayHSTDsp = "${:.2f}".format(HST)  
                        HSTLst.append(HST)
                PayHSTTotals = sum(HSTLst)
                PayHSTTotalsDsp = "${:.2f}".format(PayHSTTotals)  
            return PayHSTDsp, PayHSTTotalsDsp, PayHSTTotals

        # Pulling Total and formatting it
        def Format_Payment_Tot():
            with open("paymentrevenue.dat", "r") as file:
                TotalLst = []
                PayTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 6:
                        Total = float(Parts[5])
                        PayTotalDsp = "${:.2f}".format(Total)  
                        TotalLst.append(Total)
                PayTotals = sum(TotalLst)
                PayTotalsDsp = "${:.2f}".format(PayTotals)  
            return PayTotalDsp, PayTotalsDsp, PayTotals

        # Pulls the date, Transaction ID and Driver ID from .dat

        def Read_Payment_Data():
            PaymentData = []
            with open("paymentrevenue.dat", "r") as file:
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 4:
                        RentalDate = Parts[0]
                        TransID = Parts[1]
                        DrivID = Parts[2]
                        subtotal = Parts[3]
                        paymentHST = Parts[4]
                        paymentTotal = Parts[5]
                        PaymentData.append((RentalDate, TransID, DrivID, subtotal, paymentHST, paymentTotal))
            return PaymentData

        # Call functions
        PaySubTotalDsp, PaySubTotalsDsp, PaySubTotals = Format_Payment_Sub()
        PayHSTDsp, PayHSTTotalsDsp, PayHSTTotals = Format_Payment_HST()
        PayTotalDsp, PayTotalsDsp, PayTotals = Format_Payment_Tot()
        PayData = Read_Payment_Data()

        # Revenue calculations:
        # Sub-totals:
        RevSubTotals = RentSubTotals + PaySubTotals
        RevSubTotalDsp = "${:.2f}".format(RevSubTotals)
        # Totals:
        RevTotals = RentTotals + PayTotals
        RevTotalsDsp = "${:.2f}".format(RevTotals)
        # HST:
        RevHST = RentHSTTotals + PayHSTTotals
        RevHSTDsp = "${:.2f}".format(RevHST)

#----------------------------------------------------------------------------------------------------

#-------------------------------- REPAIR EXPENSES ---------------------------------------------------


        # Pulling the transaction sub-total, and formatting it.
        def Format_Repair_Sub():
            with open("repairs.dat", "r") as file:
                SubTotalLst = []
                RepSubTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 4:
                        SubTotal = float(Parts[3])
                        RepSubTotalDsp = "${:.2f}".format(SubTotal)  
                        SubTotalLst.append(SubTotal)
                RepSubTotals = sum(SubTotalLst)
                RepSubTotalsDsp = "${:.2f}".format(RepSubTotals)  
            return RepSubTotalDsp, RepSubTotalsDsp, RepSubTotals


        # Pulling HST and formatting it
        def Format_Repair_HST():
            with open("repairs.dat", "r") as file:
                HSTLst = []
                RepHSTDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 5:
                        HST = float(Parts[4])
                        RepHSTDsp = "${:.2f}".format(HST)  
                        HSTLst.append(HST)
                RepHSTTotals = sum(HSTLst)
                RepHSTTotalsDsp = "${:.2f}".format(RepHSTTotals) 
            return RepHSTDsp, RepHSTTotalsDsp, RepHSTTotals

        # Pulling Total and formatting it
        def Format_Repair_Tot():
            with open("repairs.dat", "r") as file:
                TotalLst = []
                RepTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 6:
                        Total = float(Parts[5])
                        RepTotalDsp = "${:.2f}".format(Total)  
                        TotalLst.append(Total)
                RepTotals = sum(TotalLst)
                RepTotalsDsp = "${:.2f}".format(RepTotals) 
            return RepTotalDsp, RepTotalsDsp, RepTotals

        # Pulls the date, Invoice # and Driver ID from .dat
        def Read_Repair_Data():
            RepairData = []
            with open("repairs.dat", "r") as file:
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 4:
                        RentalDate = Parts[0]
                        TransID = Parts[1]
                        DrivID = Parts[2]
                        subtotal = Parts[3]
                        paymentHST = Parts[4]
                        paymentTotal = Parts[5]
                        RepairData.append((RentalDate, TransID, DrivID, subtotal, paymentHST, paymentTotal))
            return RepairData

        # Call functions
        RepSubTotalDsp, RepSubTotalsDsp, RepSubTotals = Format_Repair_Sub()
        RepHSTDsp, RepHSTTotalsDsp, RepHSTTotals = Format_Payment_HST()
        RepTotalDsp, RepTotalsDsp, RepTotals = Format_Repair_Tot()
        RepairData = Read_Repair_Data()

        #----------------------------------------------------------------------------------------------------



        # ------------------------------ ITEM EXPENSES ----------------------------------------------------
        # Pulling the transaction subtotal, and formatting it.
        def Format_Item_Sub():
            with open("supplies.dat", "r") as file:
                SubTotalLst = []
                ItemSubTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 4:
                        SubTotal = float(Parts[3])
                        ItemSubTotalDsp = "${:.2f}".format(SubTotal)  
                        SubTotalLst.append(SubTotal)
                ItemSubTotals = sum(SubTotalLst)
                ItemSubTotalsDsp = "${:.2f}".format(ItemSubTotals)  
            return ItemSubTotalDsp, ItemSubTotalsDsp, ItemSubTotals

        # Pulling HST and formatting it
        def Format_Item_HST():
            with open("supplies.dat", "r") as file:
                HSTLst = []
                ItemHSTDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 5:
                        HST = float(Parts[4])
                        ItemHSTDsp = "${:.2f}".format(HST)  
                        HSTLst.append(HST)
                ItemHSTTotals = sum(HSTLst)
                ItemHSTTotalsDsp = "${:.2f}".format(ItemHSTTotals)  
            return ItemHSTDsp, ItemHSTTotalsDsp, ItemHSTTotals

        # Pulling Total and formatting it
        def Format_Item_Tot():
            with open("supplies.dat", "r") as file:
                TotalLst = []
                ItemTotalDsp = ""
                for line in file:
                    Parts = line.strip().split(',')
                    if len(Parts) >= 6:
                        Total = float(Parts[5])
                        ItemTotalDsp = "${:.2f}".format(Total)  
                        TotalLst.append(Total)
                ItemTotals = sum(TotalLst)
                ItemTotalsDsp = "${:.2f}".format(ItemTotals)  
            return ItemTotalDsp, ItemTotalsDsp, ItemTotals

        # Pulls the date, invoice number and Driver ID from .dat
        def Read_Item_Data():
            ItemData = []
            with open("supplies.dat", "r") as file:
                    for line in file:
                        Parts = line.strip().split(',')
                        if len(Parts) >= 4:
                            RentalDate = Parts[0]
                            TransID = Parts[1]
                            DrivID = Parts[2]
                            subtotal = Parts[3]
                            paymentHST = Parts[4]
                            paymentTotal = Parts[5]
                            ItemData.append((RentalDate, TransID, DrivID, subtotal, paymentHST, paymentTotal))
            return ItemData

        # Call functions
        ItemData = Read_Item_Data()
        ItemSubTotalDsp, ItemSubTotalsDsp, ItemSubTotals = Format_Item_Sub()
        ItemHSTDsp, ItemHSTTotalsDsp, ItemHSTTotals = Format_Item_HST()
        ItemTotalDsp, ItemTotalsDsp, ItemTotals = Format_Item_Tot()

        # Expense calculations:
        # Sub-totals:
        ExpSubTotals = RepSubTotals + ItemSubTotals
        ExpSubTotalDsp = "${:.2f}".format(ExpSubTotals)
        # Totals:
        ExpTotals = RepTotals + ItemTotals
        ExpTotalsDsp = "${:.2f}".format(ExpTotals)
        # HST:
        ExpHST = RepHSTTotals + ItemHSTTotals
        ExpHSTTotalsDsp = "${:.2f}".format(ExpHST)
        #----------------------------------------------------------------------------------------------------


        #--------------HIGHLIGHT SECTION------------------------------------------------------------------------
        NetProfit = RevSubTotals - ExpSubTotals
        NetProfitDsp = "${:.2f}".format(NetProfit)
        NetProfMargin = (NetProfit / RevSubTotals) * 100
        NetProfMarginDsp = "{:.2%}".format(NetProfMargin)

        # Call functions !!!
        #----------------------------------------------------------------------------------------------------





        print("-----------------------------------------------------------------------------------------------------------")
        print("                                         PROFIT LISTING REPORT")
        print("-----------------------------------------------------------------------------------------------------------")
        print("                                          HAB TAXI SERVICE")
        print("                                          442 MONTREAL ST")
        print("                                        ST. JOHN'S NL, A1A1A1")
        print("                                           (709) 907-7979")
        print("-----------------------------------------------------------------------------------------------------------")
        print("                             PROFIT LISTING FROM 2024/01/01 - 2024/01/31")
        print()
        print("   REVENUE SUMMARY:")
        print("-----------------------------------------------------------------------------------------------------------")
        print("   RENTAL REVENUE:")
        print()
        print("       DATE:             DRIVER NO.:        TRANS. ID:         SUBTOTAL:          HST:         TOTAL:")
        print()
        for rental in RentalData:
            print(f"       {rental[0]:<15}   {rental[1]:>10}         {rental[2]:>10}       {rental[3]:>10}      {rental[4]:>10}    {rental[5]:>10}")

        print()
        print(f"                  RENTAL TOTALS:                             {RentTotalsDsp:>10}      {RentHSTTotalsDsp:>10}    {RentTotalsDsp:>10}      ")
        print("-----------------------------------------------------------------------------------------------------------")
        print("   PAYMENT REVENUE:")
        print()
        print("       DATE:          DRIVER NO.:        TRANS. ID:         SUBTOTAL:          HST:         TOTAL:")
        print()
        for payment in PayData:
            print(f"       {payment[0]:<15}   {payment[1]:>10}         {payment[2]:>10}       {payment[3]:>10}      {payment[4]:>10}    {payment[5]:>10}")

        print()
        print(f"                  PAYMENT TOTALS:                           {PaySubTotalsDsp:>10}       {PayHSTTotalsDsp:>10}    {PayTotalsDsp:>10}      ")
        print("-----------------------------------------------------------------------------------------------------------")
        print(f"                  REVENUE TOTALS:                            {RevSubTotalDsp:>10}      {RevHSTDsp:>10}    {RevTotalsDsp:>10}      ")
        print("-----------------------------------------------------------------------------------------------------------")
        print()
        print("   EXPENSES SUMMARY:")
        print("-----------------------------------------------------------------------------------------------------------")
        print("   REPAIRS AND MAINTENANCE:")
        print()
        print("       DATE:          DRIVER NO.:        TRANS. ID:        SUBTOTAL:          HST:         TOTAL:")
        print()
        for repair in RepairData:
            print(f"       {repair[0]:<15}   {repair[1]:>10}         {repair[2]:>10}       {repair[3]:>10}      {repair[4]:>10}    {repair[5]:>10}")
        print()
        print(f"                   REPAIR TOTALS:                            {RepSubTotalsDsp:>10}      {RepHSTTotalsDsp:>10}    {RepTotalsDsp:>10}      ")
        print("-----------------------------------------------------------------------------------------------------------")
        print("   SUPPLIES EXPENSES:")
        print()
        print("       DATE:          ITEM NO.:          QUANTITY.:         SUBTOTAL:          HST:         TOTAL:")
        print()
        for item in ItemData:
            print(f"       {item[0]:<15}   {item[1]:>10}         {item[2]:>10}       {item[3]:>10}      {item[4]:>10}    {item[5]:>10}")
        print()
        print(f"                    SUPPLY TOTALS:                           {ItemSubTotalsDsp:>10}      {ItemHSTTotalsDsp:>10}    {ItemTotalsDsp:>10}      ")
        print("-----------------------------------------------------------------------------------------------------------")
        print(f"                   EXPENSE TOTALS:                           {(ExpTotalsDsp):>10}      {ExpHSTTotalsDsp:>10}    {ExpTotalsDsp:>10}      ")
        print("-----------------------------------------------------------------------------------------------------------")
        print("   REPORT SUMMARY:")
        print()                    
        print(f"   NET PROFIT:   {(NetProfitDsp):>10}                 NET PROFIT MARGIN:               {NetProfMarginDsp:>10}")
        print()
        print("-----------------------------------------------------------------------------------------------------------")
        print("                                      * * * * * END OF REPORT * * * * *")
        print()
        input(f"PRESS ENTER TO CONTINUE TO MAIN MENU")