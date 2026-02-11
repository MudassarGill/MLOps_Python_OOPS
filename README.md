# MLOps Python OOPs Concepts

This repository is a comprehensive guide to Object-Oriented Programming (OOP) in Python, tailored for MLOps and general Python development. It covers fundamental to advanced concepts through practical examples and mini-projects.

## Project Overview

The goal of this project is to demonstrate core OOP principles such as Class & Objects, Inheritance, Polymorphism, Encapsulation, and Abstraction. It includes standalone scripts for specific concepts as well as integrated applications like a Bank Management System and a generic "Chatbook" application.

## 📂 File Descriptions

### 1. `All_in_One.py` (Bank Management System)
A complete **Bank Management System** that integrates multiple OOP concepts into a single application.
- **Concepts**: Classes, Instance & Class Attributes, Private Attributes (Encapsulation), Getters/Setters, Static Methods, Class Methods, Inheritance (SavingAccount), and Polymorphism.
- **Features**: Create accounts, withdraw/deposit funds, check balances, and manage bank details.

### 2. `OOps_project.py` (Chatbook)
A console-based social media application simulation called **Chatbook**.
- **Features**: 
    - User Login/Signup
    - Forgot Password
    - Write Posts
    - Send Messages
- **Concepts**: Class design, menu-driven logic, state management (`is_logged_in`).

### 3. `inheritance.py`
A deep dive into **Inheritance** types with clear examples:
- **Single Inheritance**: Basic parent-child relationship.
- **Multiple Inheritance**: inheriting from multiple parents.
- **Multilevel Inheritance**: A chain of inheritance.
- **Hierarchical Inheritance**: Multiple children from one parent.
- **Hybrid Inheritance**: A combination of multiple types.
- **Real-world Example**: `Person` -> `Student` hierarchy.

### 4. `Encap.py`
Demonstrates **Encapsulation** and data hiding.
- **Bank Class**: Shows how `__balance` (private variable) is protected and how access attempts are handled.
- **ATM Machine**: A practical use case of encapsulation with `withdraw` and `deposit` methods exposing controlled access to private data.

### 5. `poly.py`
Illustrates **Polymorphism** (Method Overriding).
- **Payment System**: A base `payment` class with subclasses `CreditCard` and `DebitCard`.
- **Logic**: Both subclasses implement their own version of the `pay()` method, demonstrating how the same method name can behave differently based on the object type.

### 6. `oop1.py`
Introduction to **Classes and Objects**.
- Basic class definitions for `employee`, `Car`, `student`, and `Mobile`.
- Demonstrates constructors (`__init__`), attributes, and methods showing object details.

### 7. `importClass.py`
A simple script demonstrating modularity by importing the `Chatbook` class from `OOps_project.py`.

### 8. `content.txt`
A text file outlining the syllabus and topics covered in this repository.

## 🚀 How to Run

You can run any of the scripts using Python. For example:

```bash
# Run the Bank Management System
python All_in_One.py

# Run the Chatbook Application
python OOps_project.py

# Run Inheritance Examples
python inheritance.py
```

## 📚 Topics Covered

- **Classes & Objects**: Blueprints and instances.
- **Encapsulation**: Public vs. Private members, Getters & Setters.
- **Inheritance**: Code reusability through parent-child relationships.
- **Polymorphism**: Flexibility in method implementation.
- **Abstraction**: Hiding complex implementation details (implied through method interfaces).
- **Static & Class Methods**: Methods bound to the class rather than the instance.

---
*Created for MLOps Python OOPs learning.*
