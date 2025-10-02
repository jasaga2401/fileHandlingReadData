# file handline
# G Allcock
# 02/10/25
# AS Computer Science

# [comment]
def two():
    pass

# read information from a file
def readFile(filePath):
    try:
        with open(filePath, "r") as file:
            content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("Error occurred:", e )

# Execute the main program
def main():
    filePath = "country.txt"
    print(readFile(filePath))

if (__name__ == "__main__"):
    main()
