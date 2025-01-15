# Django To-Do App

This is a simple To-Do application built with Django. It allows users to add, edit, mark as done, set as incomplete, and delete tasks.

## Features

- Add new tasks
- Edit existing tasks
- Mark tasks as done
- Set tasks as incomplete
- Delete tasks

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-todo-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-todo-app
    cd todoProject
    ```
3. Create and activate the virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Use the interface to manage your tasks.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.
