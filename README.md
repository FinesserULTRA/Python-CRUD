# Python CRUD App

A simple Python CRUD (Create, Read, Update, Delete) application with a CRUDCall class for making database operations and a Cruddb class to manage the database.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [CrudCall](#CrudCall)
  - [CrudDB](#CrudDB)
  - [Main Application](#main-application)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Python CRUD app provides a simple interface to perform basic database operations, including inserting, editing, and removing records.

## Features

- Create, Read, Update, and Delete records.
- Interactive command-line interface for easy interaction.
- Modular code structure with separate classes for CRUD operations.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.xx.xx)
- mysql connector
- 

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/FinesserULTRA/Python-CRUD.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Python-CRUD
    ```


## Usage

### CrudCall

The `CrudCall` class handles the database operations. Here are its main functions:

- **insert(data):** Inserts a new record into the database.
- **update_rec(record_id, new_data):** Edits an existing record in the database.
- **delete(record_id):** Removes a record from the database.
- **view():** Retrieves all records from the database.
- **view(record_id):** Gets one record
Example usage in the main application:

```python
from datasys import CrudCall

# Create an instance of CrudCall
crud_call = CrudCall()

# Insert a new record
crud_call.insert_record({"name": "John Doe", "age": 30, "email": "john.doe@example.com"})

# Edit an existing record
crud_call.edit_record(1, {"name": "Updated Name", "age": 31, "email": "updated.email@example.com"})

# Remove a record
crud_call.remove_record(1)

# Get all records
all_records = crud_call.get_all_records()
print(all_records)
```

## Main Application
In your main application, you can use both CRUDCall and Cruddb classes as shown in the examples above. Customize the code according to your specific database structure and requirements.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to open an issue or create a pull request.
Need to fix some stuff:
- **Add more queries**
- **csv needs to be updated**

## License

This project is licensed under the [MIT License](LICENSE).
