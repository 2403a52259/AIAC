def extract_student_info(student_dict):
    """
    Extract full name, branch, and SGPA from nested student dictionary.
    Returns tuple (full_name, branch, sgpa) or error message.
    """
    try:
        student = student_dict.get("student", {})
        name = student.get("name", {})
        first = name.get("first", "")
        last = name.get("last", "")
        full_name = f"{first} {last}".strip()
        
        branch = student.get("branch", "")
        sgpa = student.get("grades", {}).get("SGPA", 0.0)
        
        if full_name and branch and sgpa > 0:
            return (full_name, branch, sgpa)
        else:
            return "Error: Missing student information"
            
    except:
        return "Error: Invalid data structure"


# Test cases
if __name__ == "__main__":
    # Example 1
    student1 = {
        "student": {
            "name": {"first": "amit", "last": "verma"},
            "branch": "CSE",
            "grades": {"SGPA": 8.7}
        }
    }
    
    # Example 2
    student2 = {
        "student": {
            "name": {"first": "Neha", "last": "singh"},
            "branch": "ECE",
            "grades": {"SGPA": 9.1}
        }
    }
    
    print("Testing:")
    print(f"Student 1: {extract_student_info(student1)}")
    print(f"Student 2: {extract_student_info(student2)}")
