from document import Document
from document import Copy

# Creating instances of Document class
doc1 = Document("Introduction to Python", "2023-10-30")
doc2 = Document("Data Analysis Techniques", "2023-11-27")

# Creating instances of Copy class
copy1 = Copy("Introduction to Python", "2023-10-30", 100, "2023-11-29")
copy2 = Copy("Data Analysis Techniques", "2023-11-27", 101, "2023-11-30")

# Displaying document and copy information
print(doc1.to_string())
print(doc2.to_string())
print("\n"+copy1.to_string())
print(copy2.to_string())

# Comparing documents and copies
if doc1.equals(doc2):
     print("\nThe documents have the same code.")
else:
     print("\nThe documents have different codes.")

if copy1.equals(copy2):
    print("\nThe copies have the same number.")
else:
     print("\nThe copies have different numbers.")
