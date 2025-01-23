# CMS Word Phrase Manager

A simple Content Management System (CMS) for managing words and phrases in a local SQLite database. This project allows administrators to view, edit, and update content easily, with features like pagination, search, and initial data loading from a JSON file.

## Features
- **View Words and Phrases**: Display a paginated list of words/phrases, including translations and example sentences.
- **Edit Words and Phrases**: Update word/phrase, translation, and example sentence fields.
- **Search and Filter**: Filter words/phrases by keyword using a search bar.
- **Load Initial Data**: Automatically populate the database with data from a JSON file.

### Prerequisites
- Python 3.x
- Django
  
## Setup Instructions
1. **Set Up a Virtual Environment**:
   ```bash
      python -m venv venv
   ```
2. **Activate the Virtual Environment**:
 ```bash
   venv\Scripts\activate
   ```
3. **Install Dependencies**:
 ```bash
   pip install django
   ```
4. **Set Up the Database**:
  ```bash
   python manage.py migrate
   ```
5. **Load Initial Data**:Run the script to load data from the JSON file:
  ```bash
   python content_manager/load_data.py
   ```
6. **Run the Development Server**:Run the script to load data from the JSON file:
 ```bash
   python manage.py runserver
   ```
7. **Access the CMS:** Open your browser and go to:
   ```bash
     http://127.0.0.1:8000/
   ```

### Steps to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/cms-word-phrase-manager.git
   cd cms-word-phrase-manager
