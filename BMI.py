
# BMI CALCULATER
def bmi_calculator():
    print("=== BMI Calculator ===")
    try:
        weight = float(input("Enter your weight (in kg): "))
        height_cm = float(input("Enter your height (in cm): "))

        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except ZeroDivisionError:
        print("Height cannot be zero!")

bmi_calculator()
