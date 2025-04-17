from fpdf import FPDF

# Create a one-page PDF with all core Python concepts
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Complete Python Concepts Guide", ln=True, align="C")
        self.ln(5)

    def body(self, sections):
        self.set_font("Arial", "", 10)
        for section, items in sections.items():
            self.set_font("Arial", "B", 11)
            self.cell(0, 8, section, ln=True)
            self.set_font("Arial", "", 10)
            for item in items:
                self.cell(0, 6, f"- {item}", ln=True)
            self.ln(2)

# Define all the core Python concepts
sections = {
    "1. Python Basics": [
        "Data types: int, float, bool, str, list, tuple, dict, set",
        "Type casting, Operators, Input/output, Comments"
    ],
    "2. Control Flow": [
        "if, elif, else", "for loops, while loops", "break, continue, pass"
    ],
    "3. Functions": [
        "def, return, default/keyword args, *args, **kwargs, recursion"
    ],
    "4. Data Structures": [
        "Lists, Tuples, Dictionaries, Sets – with methods and operations"
    ],
    "5. Strings": [
        "String methods, formatting, f-strings, indexing and slicing"
    ],
    "6. Modules & Packages": [
        "import, from ... import, built-in modules, custom modules"
    ],
    "7. File Handling": [
        "open(), read(), write(), append(), with statement (context manager)"
    ],
    "8. Exception Handling": [
        "try, except, finally, else, raising & custom exceptions"
    ],
    "9. OOP": [
        "Classes, __init__, self, Inheritance, Polymorphism, Encapsulation, Abstraction"
    ],
    "10. Functional Tools": [
        "lambda, map(), filter(), reduce(), comprehensions"
    ],
    "11. Iterators & Generators": [
        "iter(), next(), yield, generator functions"
    ],
    "12. Decorators": [
        "@decorator, @staticmethod, @classmethod"
    ],
    "13. Pythonic Tools": [
        "zip(), enumerate(), any(), all(), sorted(), isinstance(), type hinting"
    ],
    "14. Standard Libraries": [
        "collections, datetime, math, random, itertools, json, os, sys"
    ]
}

# Create and build the PDF
pdf = PDF()
pdf.add_page()
pdf.body(sections)
pdf.output("complete_python_concepts_one_page.pdf")
