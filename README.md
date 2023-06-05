# Office Quotes API

The Quotes API is a RESTful web service that allows you to manage and retrieve quotes from a MongoDB database. It provides endpoints to create, read, update, and delete quotes.

## Features

- Create a new quote with a quote text and author.
- Retrieve a list of all quotes or filter quotes by author or keyword.
- Update an existing quote with new text or author.
- Delete a quote by its unique identifier.
- Simple and easy-to-use API for managing quotes.

## Technologies Used

- Flask: A lightweight web framework for building RESTful APIs.
- PyMongo: A Python driver for MongoDB, used for database operations.
- MongoDB: A NoSQL document-oriented database for storing quotes.

## Setup and Installation

1. Clone the repository: `git clone https://github.com/your-username/quotes-api.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your MongoDB database and update the connection string in the Flask app.
4. Run the Flask app: `python app.py`
5. The API will be available at: `http://localhost:5000`

## API Endpoints

- `GET /quote`: Retrieve a list of all quotes.
- `POST /add`: Create a new quote.
- `DELETE /delete`: Delete a quote.

For detailed information about each endpoint and the expected request/response formats, refer to the API documentation.

## Contribution

Contributions to the Quotes API project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the project's code style and guidelines.

## Want to add Quotes?

Just Add Your quotes and author in add_quotes.txt & I'll take care of the rest or you can use the API Endpoint which will instantly add your data to the database.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as per the terms of the license.

