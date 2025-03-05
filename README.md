# Django University Timetable

## Project Overview
The Django University Timetable project is designed to help students and faculty manage and view class schedules efficiently. The application provides a user-friendly interface for accessing timetable information, allowing users to easily navigate through different courses and their respective schedules.

### Key Features
- User authentication for secure access.
- Dynamic timetable generation based on user preferences.
- Responsive design for accessibility on various devices.
- Integration with a database to store and manage timetable data.

## Installation Guide

Follow these steps to set up the project locally:

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Django_University_Timetable
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Django**:
   ```bash
   pip install django==5.1.6
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Additional Information
- Ensure you have Python 3.x installed on your machine.
- For more information on Django, visit the [Django documentation](https://docs.djangoproject.com/en/5.1/).
