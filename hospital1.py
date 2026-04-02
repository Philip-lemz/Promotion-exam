"""
HOSPITAL MANAGEMENT SYSTEM
A complete Python program for managing patient records and hospital operations.
Developed for the Promotion Exam (Practical Only).
Due Date: 29/03/2026
"""



# Global dictionary to store all patient records
patients = {}


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("        HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Patient")
    print("2. View All Patients")
    print("3. View Patient Report")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Search Patient")
    print("7. Hospital Statistics")
    print("8. Exit")
    print("=" * 50)


def get_positive_float(prompt):
    """
    Get a positive float value from user input.
    Continues prompting until a valid positive number is entered.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be positive. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")


def get_positive_int(prompt):
    """
    Get a positive integer value from user input.
    Continues prompting until a valid positive integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Error: Age must be a positive number. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_unique_patient_id():
    """
    Prompt user for a unique Patient ID.
    Checks against existing patients and ensures uniqueness.
    """
    while True:
        patient_id = input("Enter Patient ID (e.g., P001): ").strip().upper()
        if patient_id == "":
            print("Error: Patient ID cannot be empty.")
        elif patient_id in patients:
            print("Error: Patient ID already exists. Please use a unique ID.")
        else:
            return patient_id


def add_patient():
    """
    Add a new patient with all required details.
    Captures: Patient ID, Name, Age, Gender, Diagnosis, and at least 2 treatments.
    """
    print("\n--- ADD NEW PATIENT ---")
    
    # Get unique Patient ID
    patient_id = get_unique_patient_id()
    
    # Get basic patient information
    name = input("Enter Full Name: ").strip().title()
    if name == "":
        print("Error: Name cannot be empty. Patient addition cancelled.")
        return
    
    age = get_positive_int("Enter Age: ")
    
    # Gender validation
    gender = input("Enter Gender (M/F/Other): ").strip().capitalize()
    while gender not in ["M", "F", "Other"]:
        print("Error: Please enter M, F, or Other.")
        gender = input("Enter Gender (M/F/Other): ").strip().capitalize()
    
    diagnosis = input("Enter Diagnosis (e.g., Malaria, Flu, etc.): ").strip().title()
    if diagnosis == "":
        print("Error: Diagnosis cannot be empty. Patient addition cancelled.")
        return
    
    # Get at least 2 treatments with costs
    treatments = {}
    print("\n--- ADD TREATMENTS (Minimum 2) ---")
    treatment_count = 0
    
    while treatment_count < 2:
        treatment_name = input(f"Enter treatment #{treatment_count + 1} name: ").strip().title()
        if treatment_name == "":
            print("Error: Treatment name cannot be empty.")
            continue
        
        # Check for duplicate treatment names
        if treatment_name in treatments:
            print("Error: Treatment already exists. Please enter a different treatment.")
            continue
        
        cost = get_positive_float(f"Enter cost for {treatment_name}: K")
        treatments[treatment_name] = cost
        treatment_count += 1
        
        # After having at least 2 treatments, ask if user wants to add more
        if treatment_count >= 2:
            more = input("Add another treatment? (y/n): ").strip().lower()
            if more != 'y':
                break
    
    # Create patient record
    patients[patient_id] = {
        "name": name,
        "age": age,
        "gender": gender,
        "diagnosis": diagnosis,
        "treatments": treatments
    }
    
    print(f"\nPatient {name} (ID: {patient_id}) has been successfully added!")


def view_all_patients():
    """Display all patients with ID, Name, and Diagnosis."""
    print("\n--- ALL PATIENTS ---")
    
    if not patients:
        print("No patients found in the system.")
        return
    
    print(f"{'Patient ID':<12} {'Name':<25} {'Diagnosis':<20}")
    print("-" * 60)
    
    for patient_id, details in patients.items():
        print(f"{patient_id:<12} {details['name']:<25} {details['diagnosis']:<20}")
    
    print(f"\nTotal patients: {len(patients)}")


def calculate_total_bill(treatments):
    """Calculate the total bill from treatments dictionary."""
    return sum(treatments.values())


def view_patient_report():
    """
    Display a detailed report for a selected patient.
    Shows all treatments, costs, and total bill.
    """
    print("\n--- PATIENT REPORT ---")
    
    if not patients:
        print("No patients found in the system.")
        return
    
    patient_id = input("Enter Patient ID to view report: ").strip().upper()
    
    if patient_id not in patients:
        print(f"Error: Patient with ID '{patient_id}' not found.")
        return
    
    details = patients[patient_id]
    
    print("\n" + "=" * 50)
    print("                 PATIENT REPORT")
    print("=" * 50)
    print(f"Patient ID    : {patient_id}")
    print(f"Name          : {details['name']}")
    print(f"Age           : {details['age']}")
    print(f"Gender        : {details['gender']}")
    print(f"Diagnosis     : {details['diagnosis']}")
    print("-" * 50)
    print("TREATMENTS:")
    print(f"{'Treatment':<25} {'Cost (K)':>10}")
    print("-" * 50)
    
    for treatment, cost in details['treatments'].items():
        print(f"{treatment:<25} K{cost:>10.2f}")
    
    total_bill = calculate_total_bill(details['treatments'])
    print("-" * 50)
    print(f"{'TOTAL BILL':<25} K{total_bill:>10.2f}")
    print("=" * 50)


def update_patient():
    """
    Update patient information.
    Options: update diagnosis, add treatment, update treatment cost, remove treatment.
    """
    print("\n--- UPDATE PATIENT ---")
    
    if not patients:
        print("No patients found in the system.")
        return
    
    patient_id = input("Enter Patient ID to update: ").strip().upper()
    
    if patient_id not in patients:
        print(f"Error: Patient with ID '{patient_id}' not found.")
        return
    
    details = patients[patient_id]
    
    while True:
        print("\n--- UPDATE OPTIONS ---")
        print(f"Patient: {details['name']} (ID: {patient_id})")
        print("1. Update Diagnosis")
        print("2. Add New Treatment")
        print("3. Update Treatment Cost")
        print("4. Remove Treatment")
        print("5. Return to Main Menu")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            # Update diagnosis
            new_diagnosis = input("Enter new diagnosis: ").strip().title()
            if new_diagnosis:
                details['diagnosis'] = new_diagnosis
                print(f"Diagnosis updated to '{new_diagnosis}'.")
            else:
                print("Diagnosis unchanged (empty input).")
        
        elif choice == "2":
            # Add new treatment
            treatment_name = input("Enter treatment name: ").strip().title()
            if not treatment_name:
                print("Error: Treatment name cannot be empty.")
                continue
            7
            
            if treatment_name in details['treatments']:
                print(f"Error: Treatment '{treatment_name}' already exists.")
                print("Use 'Update Treatment Cost' option to modify existing treatment.")
                continue
            
            cost = get_positive_float(f"Enter cost for {treatment_name}: K")
            details['treatments'][treatment_name] = cost
            print(f"Treatment '{treatment_name}' added with cost K{cost:.2f}.")
        
        elif choice == "3":
            # Update treatment cost
            if not details['treatments']:
                print("No treatments available to update.")
                continue
            
            print("\nCurrent treatments:")
            for idx, (name, cost) in enumerate(details['treatments'].items(), 1):
                print(f"{idx}. {name}: K{cost:.2f}")
            
            treatment_name = input("Enter treatment name to update: ").strip().title()
            if treatment_name not in details['treatments']:
                print(f"Error: Treatment '{treatment_name}' not found.")
                continue
            
            new_cost = get_positive_float(f"Enter new cost for {treatment_name}: K")
            details['treatments'][treatment_name] = new_cost
            print(f"Treatment '{treatment_name}' cost updated to K{new_cost:.2f}.")
        
        elif choice == "4":
            # Remove treatment
            if not details['treatments']:
                print("No treatments available to remove.")
                continue
            
            # Prevent removal if only one treatment remains
            if len(details['treatments']) <= 1:
                print("Error: Cannot remove the only remaining treatment. Patient must have at least one treatment.")
                continue
            
            print("\nCurrent treatments:")
            for idx, (name, cost) in enumerate(details['treatments'].items(), 1):
                print(f"{idx}. {name}: K{cost:.2f}")
            
            treatment_name = input("Enter treatment name to remove: ").strip().title()
            if treatment_name not in details['treatments']:
                print(f"Error: Treatment '{treatment_name}' not found.")
                continue
            
            confirm = input(f"Are you sure you want to remove '{treatment_name}'? (y/n): ").strip().lower()
            if confirm == 'y':
                del details['treatments'][treatment_name]
                print(f"Treatment '{treatment_name}' has been removed.")
            else:
                print("Removal cancelled.")
        
        elif choice == "5":
            print("Returning to main menu...")
            break
        
        else:
            print("Invalid option. Please select 1-5.")


def delete_patient():
    """Delete a patient from the system using Patient ID."""
    print("\n--- DELETE PATIENT ---")
    
    if not patients:
        print("No patients found in the system.")
        return
    
    patient_id = input("Enter Patient ID to delete: ").strip().upper()
    
    if patient_id not in patients:
        print(f"Error: Patient with ID '{patient_id}' not found.")
        return
    
    patient_name = patients[patient_id]['name']
    
    confirm = input(f"Are you sure you want to delete '{patient_name}' (ID: {patient_id})? (y/n): ").strip().lower()
    
    if confirm == 'y':
        del patients[patient_id]
        print(f"Patient '{patient_name}' has been deleted successfully.")
    else:
        print("Deletion cancelled.")


def search_patient():
    """
    Search for a patient by Patient ID or Name.
    Displays full details of matching patients.
    """
    print("\n--- SEARCH PATIENT ---")
    
    if not patients:
        print("No patients found in the system.")
        return
    
    search_term = input("Enter Patient ID or Name to search: ").strip().upper()
    
    if search_term == "":
        print("Error: Search term cannot be empty.")
        return
    
    results = []
    
    # Search by ID or by name (partial match)
    for patient_id, details in patients.items():
        if patient_id == search_term:
            results.append((patient_id, details))
        elif search_term.lower() in details['name'].lower():
            results.append((patient_id, details))
    
    if not results:
        print(f"No patients found matching '{search_term}'.")
        return
    
    print(f"\n--- SEARCH RESULTS ({len(results)} found) ---")
    
    for patient_id, details in results:
        print("\n" + "-" * 40)
        print(f"Patient ID    : {patient_id}")
        print(f"Name          : {details['name']}")
        print(f"Age           : {details['age']}")
        print(f"Gender        : {details['gender']}")
        print(f"Diagnosis     : {details['diagnosis']}")
        print("Treatments    :")
        for treatment, cost in details['treatments'].items():
            print(f"  - {treatment}: K{cost:.2f}")
        total_bill = calculate_total_bill(details['treatments'])
        print(f"Total Bill    : K{total_bill:.2f}")


def hospital_statistics():
    """
    Display hospital statistics:
    - Total number of patients
    - Total revenue (sum of all bills)
    - Patient with highest bill
    - Patient with lowest bill
    """
    print("\n--- HOSPITAL STATISTICS ---")
    
    if not patients:
        print("No patients in the system. Statistics unavailable.")
        return
    
    # Calculate total patients
    total_patients = len(patients)
    
    # Calculate total revenue and track min/max bills
    total_revenue = 0
    patient_bills = []
    
    for patient_id, details in patients.items():
        total_bill = calculate_total_bill(details['treatments'])
        total_revenue += total_bill
        patient_bills.append((patient_id, details['name'], total_bill))
    
    # Find patient with highest and lowest bill
    if patient_bills:
        # Sort by total bill
        patient_bills.sort(key=lambda x: x[2])
        lowest_patient = patient_bills[0]
        highest_patient = patient_bills[-1]
    
    print("\n" + "=" * 50)
    print("              HOSPITAL STATISTICS")
    print("=" * 50)
    print(f"Total Number of Patients : {total_patients}")
    print(f"Total Revenue            : K{total_revenue:,.2f}")
    print("-" * 50)
    print("Patient with HIGHEST Bill:")
    print(f"  - {highest_patient[1]} (ID: {highest_patient[0]})")
    print(f"    Total Bill: K{highest_patient[2]:,.2f}")
    print("-" * 50)
    print("Patient with LOWEST Bill:")
    print(f"  - {lowest_patient[1]} (ID: {lowest_patient[0]})")
    print(f"    Total Bill: K{lowest_patient[2]:,.2f}")
    print("=" * 50)


def main():
    """Main program loop."""
    print("\n" + "=" * 50)
    print("   WELCOME TO HOSPITAL MANAGEMENT SYSTEM")
    print("=" * 50)
    print("Initializing system...")
    
    # Optional: Add some sample data for testing (commented out)
    # Uncomment for testing purposes
    """
    patients["P001"] = {
        "name": "John Banda",
        "age": 25,
        "gender": "Male",
        "diagnosis": "Malaria",
        "treatments": {"Consultation": 50.0, "Medication": 120.0}
    }
    patients["P002"] = {
        "name": "Mary Phiri",
        "age": 45,
        "gender": "Female",
        "diagnosis": "Hypertension",
        "treatments": {"Consultation": 50.0, "Blood Test": 80.0, "Medication": 150.0}
    }
    """
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_patient()
        elif choice == "2":
            view_all_patients()
        elif choice == "3":
            view_patient_report()
        elif choice == "4":
            update_patient()
        elif choice == "5":
            delete_patient()
        elif choice == "6":
            search_patient()
        elif choice == "7":
            hospital_statistics()
        elif choice == "8":
            print("\nThank you for using the Hospital Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


# Program entry point
if __name__ == "__main__":
    main()
2
