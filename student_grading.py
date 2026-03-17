def calculate_grade(score):
    if not isinstance(score, (int, float)):
        return "Invalid"
    
    if score > 100 or score < 0:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"