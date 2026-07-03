from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

program = """
def calculate_compound_interest(principal, annual_rate, num_times_compounded_per_year, time_in_years):
    # Convert the annual rate from percentage to decimal
    r = annual_rate / 100.0
    
    # Calculate compound interest using the formula
    amount = principal * (1 + r / num_times_compounded_per_year) ** (num_times_compound_per_year * time_in_years)
    
    return amount

# Example usage
principal = float(input("Enter the principal amount: "))
annual_rate = float(input("Enter the annual interest rate (as a percentage): "))
num_times_compounded_per_year = int(input("Enter the number of times the interest is compounded per year: "))
time_in_years = float(input("Enter the time in years: "))

compound_interest = calculate_compound_interest(principal, annual_rate, num_times_compounded_per_year, time_in_years)

print(f"The amount after {time_in_years} years is: ${amount:.2f}")
"""

# this splitter support multiple formats like :
# Python
# HTML
# MARKDOWN

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

doc = splitter.split_text(program)
print(doc[0])
