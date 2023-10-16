---

# Flask MongoDB Data Upload and Display

This Python script utilizes Flask, pandas, and MongoDB to enable uploading and displaying data in an HTML table. The data is extracted from an uploaded CSV file, processed using pandas, and stored in a MongoDB database for display in a web application.

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [How to Use](#how-to-use)
- [Uploading Data](#uploading-data)
- [Displaying Data](#displaying-data)
- [Contributing](#contributing)
- [License](#license)

## Overview

This script sets up a Flask web application to allow users to upload a CSV file containing specific alarm data. The data is then processed, including various transformations and calculations, and stored in a MongoDB database. The stored data is later displayed in an HTML table.

## Dependencies

The following libraries and components are required:

- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [pandas](https://pandas.pydata.org/)
- [pymongo](https://pymongo.readthedocs.io/)
- [MongoDB](https://www.mongodb.com/)

You can install the necessary Python packages using pip:

```bash
pip install Flask pandas pymongo
```

Ensure MongoDB is installed and running on your system.

## How to Use

1. Clone the repository or download the provided script.
2. Ensure MongoDB is running and accessible.
3. Run the script using Python:

   ```bash
   python your_script_name.py
   ```

4. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the web application.

## Uploading Data

- Access the web application through the provided URL.
- Choose a CSV file containing the required alarm data and upload it.
- The script will process the file, perform necessary transformations, and store the data in the MongoDB database.

## Displaying Data

- Navigate to [http://127.0.0.1:5000/table](http://127.0.0.1:5000/table) after uploading data.
- The uploaded data will be retrieved from MongoDB and displayed in an HTML table.

## Contributing

Contributions and feedback are welcome! Feel free to open issues or submit pull requests if you have any suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).

---
