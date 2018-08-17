# Tempfile Module
import tempfile

# Create a temporary file
tempFile = tempfile.TemporaryFile()

# Write to a temporary file
tempFile.write(b'save this special number for me 5678990')
tempFile.seek(0)

# Read the temporary file
print(tempFile.read())

# Close the temporary
tempFile.close()
