import csv
import os

class MiniDB:
    def __init__(self, filename):
        self.filename = filename
        # Ensure the file is created if it doesn't exist
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()
    
    def create(self, rows):
        """Creates new row-value pairs in the CSV file"""
        try:
            with open(self.filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
        except IOError:
            print("Error: Could not write to file.")
    
    def show(self):
        """Shows all row-value pairs in the CSV file"""
        try:
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for row, value in reader:
                    print(f"Row: {row}, Value: {value}")
        except IOError:
            print("Error: Could not read from file.")
        except csv.Error:
            print("Error: Could not read from file.")
    
    def update(self, rows):
        """Updates row-value pairs in the CSV file"""
        try:
            data = []
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for r, v in reader:
                    data.append([r, v])
            for row, value in rows:
                for i, (r, v) in enumerate(data):
                    if r == str(row):
                        data[i] = [row, value]
                        break
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except IOError:
            print("Error: Could not write to file.")
    
    def delete(self, rows):
        """Deletes row-value pairs from the CSV file"""
        try:
            data = []
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                for r, v in reader:
                    data.append([r, v])
            for row in rows:
                data = [item for item in data if item[0] != str(row)]
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except IOError:
            print("Error: Could not write to file.")
    
    def get_available_files(self):
        """Gets a list of all available files in the same directory as the script"""
        files = []
        for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
            if os.path.isfile(file) and file != os.path.basename(__file__):
                files.append(file)
        return files

def main():
    filename = input("Enter filename or leave blank to list available files: ")
    if not filename:
        db = MiniDB("")
        files = db.get_available_files()
        print("\nAvailable files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        filename = input("Enter the number of the file you want to open: ")
        try:
            filename = files[int(filename) - 1]
        except (IndexError, ValueError):
            print("Error: Invalid input. Please try again.")
            exit()
    db = MiniDB(filename)

    while True:
        print("\n1. Create data")
        print("2. Show data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Close database and exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                rows = []
                while True:
                    row, value = input("Enter row and value (comma separated) or 'done' to finish: ").split(',')
                    row = row.strip()
                    value = value.strip()
                    if row == "done":
                        break
                    rows.append([row, value])
            except ValueError:
                print("Error: Invalid input. Please enter a comma-separated value.")
                continue
            db.create(rows)
        elif choice == "2":
            db.show()
        elif choice == "3":
            try:
                rows = []
                while True:
                    row, value = input("Enter row and value (comma separated) or 'done' to finish: ").split(',')
                    row = row.strip()
                    value = value.strip()
                    if row == "done":
                        break
                    rows.append([row, value])
            except ValueError:
                print("Error: Invalid input. Please enter a comma-separated value.")
                continue
            db.update(rows)
        elif choice == "4":
            try:
                rows = []
                while True:
                    row = input("Enter row or 'done' to finish: ").strip()
                    if row == "done":
                        break
                    rows.append(row)
            except ValueError:
                print("Error: Invalid input. Please enter a comma-separated value.")
                continue
            db.delete(rows)
        elif choice == "5":
            print("Database closed. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

