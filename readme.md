# How to Python
1. Install Python 3
2. run  `python -m venv env`
3. run (windows) `.\env\Scripts\activate`
4. run `python -m pip install --upgrade pip`
5. run `pip install -r requirements.txt`

# How to run test suit
run in terminal: `pytest` or `pytest -v` for verbose. 

# Inventory Assignment
Character Inventory System 
 
You are tasked to write a part of the inventory system for a game. You must write the functions for the inventory and ensure that you have tests in place for all the functions. 
Make use of unit tests and integration tests in the appropriate situations.  
- Inventory size: 5 x 5 (25) 
- Wallet: Cash available 
- Maximum Weight: 100 
- Item Types 
    - Weapon 
    - Gear 
    - Consumable 
- Item 
    - Id 
    - Name 
    - Weight 
    - Value 
    - Type 
- Inventory functions 
    - Pickup item 
    - Drop item 
    - View all items 
    - View items for a type 
    - Group items by type  
    - Sort items by value 
    - Sort items by name 
    - Sort items by weight  
    - Get number of open slots 
    - Get total number of items in inventory 
    - Get remaining weight available 
    - Get total items weight 
    - Get item weight for type  
    - Sell item  
    - Buy item 
    - Pickup Cash 