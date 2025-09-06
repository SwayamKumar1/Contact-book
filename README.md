# Contact Book

A simple **Python Contact Book** application that allows you to **add, search, update, show, and delete contacts**. Contacts are stored in a **JSON file**, so your data persists even after closing the program.  

---

## Description

**Contact Book** is a beginner-friendly Python project designed to help users efficiently manage their personal contacts. It allows users to perform all basic contact management operations through a **menu-driven interface**. Contact names are **case-insensitive**, while the original formatting is preserved for display.  

The project demonstrates key Python concepts, including **dictionaries, loops, functions, file handling, and user input validation**, making it a practical mini project for beginners.  

---

## Features

- Add new contacts (name and phone number)  
- Search for contacts by name (case-insensitive)  
- Update existing contacts  
- Delete contacts  
- Show all contacts  
- Persistent storage using `contacts.json`  

---

## How It Works

1. The program loads existing contacts from `contacts.json` if it exists.  
2. The user is presented with a menu to choose an action.  
3. Contacts are stored in a **dictionary**, with lowercase names as keys and a dictionary containing original name and phone number as value.  
4. Operations are **case-insensitive**, but the original name formatting is preserved for display.  
5. Changes are automatically saved to `contacts.json`.  

---

## Requirements

- Python 3.x  
- No external libraries required (uses built-in `json` module)  

---

## How to Run

1. Clone or download the repository.  
2. Open terminal/command prompt in the project folder.  
3. Run the program:  
```bash
python Contact_book.py
