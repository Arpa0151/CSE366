import random

def load_student_ids(file_path):
    """Load and return a list of student IDs from a file."""
    try:
        with open(file_path, 'r') as file:
            ids = [line.strip() for line in file if line.strip()]
        return ids
    except FileNotFoundError:
        print("Error: The file could not be found.")
        return []

def shuffle_and_select(ids):
    """Shuffle student IDs and then select them one by one."""
    if not ids:
        print("No students available for selection.")
        return

    random.shuffle(ids)  # Shuffle the list of student IDs
    for idx, student_id in enumerate(ids, start=1):
        print(f"Round {idx}: Selected Student ID - {student_id}")

def main():
    """Main execution function to manage the viva selection process."""
    file_path = 'student_ids.txt'
    
    # Load student IDs from the file
    student_ids = load_student_ids(file_path)
    
    if not student_ids:
        return  # Exit if no students are available

    print("Starting the viva selection process...\n")
    shuffle_and_select(student_ids)
    
    print("\nAll students have been selected for the viva.")

if __name__ == "__main__":
    main()
