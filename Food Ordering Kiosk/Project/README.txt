# Point of Sale (POS) System
This README file provides an overview of the Point of Sale (POS) system implemented in Python using the Tkinter library.

## Description
This POS system is a graphical user interface application designed for managing sales transactions in a retail or food service environment. It allows users to select items, add them to a cart, calculate totals, and process payments.

## Features

1. Graphical user interface with Tkinter
2. Item selection through image buttons
3. Shopping cart functionality
4. Real-time calculation of subtotal, tax, and total
5. Payment processing with change calculation
6. Ability to remove items from the cart
7. Reset functionality to clear the current transaction

## Requirements
- Python 3.x
- Tkinter library (usually comes pre-installed with Python)

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Clone or download this repository to your local machine.
3. Make sure all image files are in the correct directory as specified in the code.

## Usage

1. Run the script using Python:
  
   python POS.py
   
2. The POS system window will appear.
3. Click on item images to add them to the cart.
4. Use the buttons at the bottom to process payment, remove items, or reset the transaction.

## File Structure
- `pos_system.py`: The main Python script containing the POS system code.
- `images/`: Directory containing all the product images used in the GUI.

## Customization
You can customize the items, prices, and images by modifying the respective sections in the code
- Update image paths in the `__init__` method
- Modify or add item functions (e.g., `burger1()`, `coke1()`, etc.) to change prices or add new items
- Adjust the GUI layout by modifying the grid positions of buttons and frames

## Notes
- This system uses local image files. Ensure all image paths are correct before running the application.
- The tax rate is set to a fixed percentage and can be adjusted in the code if needed.

