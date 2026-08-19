Identify the Big Problem:
The big problem is that the school vending machine fails to reliably work for students.

Sub-Problems:
The machine sometimes gives the wrong amount of change.
The machine does not alert staff when items are sold out.
Students often select the wrong item by pressing incorrect buttons.
The machine responds slowly when many students use it one after another.

Define Computational Thinking Approaches:
  Sub-Problem 1: Change Calculation
    CT Skill: Abstraction
    Solution: Focus only on the selected item's price and total cash inserted to calculate accurate change.
  Sub-Problem 2: Inventory Tracking
    CT Skill: Decomposition
    Solution: Break inventory management into item counters that decrease with each purchase and trigger a signal when stock reaches zero.
  Sub-Problem 3: User Selection Errors
    CT Skill: Algorithmic Thinking
    Solution: Implement a two-step confirmation prompt to let users cancel accidental presses.
  Sub-Problem 4: System Latency
    CT Skill: Pattern Recognition
    Solution: Identify hours of most use during lunch breaks and program background memory clearing routines to those specific time period.

Psuedocode:
BEGIN CanteenCheckout
    SET totalCost = 0
    SET itemPrice = 0
    SET quantity = 0
    SET amountPaid = 0
    SET change = 0
    
    DISPLAY "--- Smart Canteen Checkout System ---"
    REPEAT
        INPUT itemPrice
        INPUT quantity
        SET itemTotal = itemPrice * quantity
        SET totalCost = totalCost + itemTotal
        
    INPUT "Add another item? (YES/NO)", userChoice
        UNTIL userChoice == "NO"
    
    DISPLAY "Total Amount Due: " + totalCost
    
    REPEAT
        INPUT "Enter cash payment: ", amountPaid
        IF amountPaid < totalCost THEN
            DISPLAY "Insufficient payment. Please enter a valid amount."
        ENDIF
    UNTIL amountPaid >= totalCost
    
    SET change = amountPaid - totalCost
    DISPLAY "Payment Accepted!"
    DISPLAY "Change to return: " + change

END CanteenCheckout
