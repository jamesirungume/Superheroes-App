## Installation

### Backend (Flask)

1. Clone the repository to your local machine.

   ```shell
   git clone <repository-url>
   cd Superheroes-App/server

    Create a virtual environment using Pipenv (recommended).

    shell

pipenv install

Activate the virtual environment.

shell

pipenv shell

Install Python dependencies.

shell

pip install -r requirements.txt

Create the SQLite database.

shell

flask db init
flask db migrate
flask db upgrade

Start the Flask server.

shell

    flask run

The Flask server should now be running on http://localhost:5555.
Frontend (React)

    Navigate to the client directory

    shell

cd ../client

Install JavaScript dependencies and build the React app.

shell

npm install --prefix client && npm run build --prefix client

Start the React development server.

shell

    npm start --prefix client

The React app should now be accessible at http://localhost:3000.
Usage

    Visit http://localhost:3000 in your web browser to access the Superheroes App.
    Explore the varous features and functionalities to manage superheroes and their powers.

License

This project is licensed under the MIT License