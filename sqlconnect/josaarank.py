
import tabula

# Read PDF File
# this contain a list
df = tabula.read_pdf("C:/Users/Ankit/Desktop/deepak.pdf")

# # Convert into Excel File
# df.to_csv('C:\Users\Ankit\Desktop\deep.csv')
print(df)
