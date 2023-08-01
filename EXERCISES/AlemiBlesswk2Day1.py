

# exercise

class TemperatureConverter:
    def __init__(self, celsius):
        self._celsius = celsius
    
    def get_celsius(self):
        return self._celsius
    
    def set_celsius(self, new_celsius):
        self._celsius = new_celsius
    
    def celsius_to_fahrenheit(self):
        fahrenheit = (self._celsius * 9/5) + 32
        return fahrenheit


# Example usage
celsius_temp = float(input("Enter temperature in Celsius: "))

converter = TemperatureConverter(celsius_temp)
print("Temperature in Celsius:", converter.get_celsius())
print("Temperature in Fahrenheit:", converter.celsius_to_fahrenheit())





# assignment
class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    def get_name(self):
        return self._name
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self, new_salary):
        self._salary = new_salary
    
    def apply_increment(self, increment_amount):
        self.set_salary(self.get_salary() + increment_amount)


# Example usage
employee = Employee("John Doe", 850000)
print("Employee Name:", employee.get_name())
print("Current Salary:", employee.get_salary())

increment_amount = 150000
employee.apply_increment(increment_amount)

print("New Salary:", employee.get_salary())
