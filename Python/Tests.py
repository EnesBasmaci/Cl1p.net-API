# The Cl1p.net API Test Client

# Import the module
from Cl1pAPI import *

# Create the main class
CB = Cl1pBoard()

# Define a cl1pboard name
CB.Cl1pBoardName = "ClipBoardTest"

DATA = "TestData"
Timeout = 1 #minutes

# Test 1 >> Existence of a clipboard
print(CB.isClipboardAvailable())

# Test 2 >> Creation of a clipboard
CB.createClipboard(DATA, Timeout)

# Test 3 >> Get Data from a clipboard
print(CB.getClipboard().strip())

# Test 4 >> Delete a clipboard
print(1 if CB.deleteClipboard() else 0)

print()

print(CB.Cl1pBoardName)
print(CB.ExpireDate)
print(CB.DeleteKey)