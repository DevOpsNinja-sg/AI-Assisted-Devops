# AIOps Project

## Prerequisites
To create a virtual environment, follow these steps:

1. **Install `virtualenv`**: If you don't have `virtualenv` installed, you can install it using `pip`:
    ```sh
    pip install virtualenv
    ```

2. **Create a Virtual Environment**: Navigate to your project directory and create a virtual environment:
    ```sh
    virtualenv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```sh
        .\venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Deactivate the Virtual Environment**: When you're done working in the virtual environment, you can deactivate it using:
    ```sh
    deactivate
    ```

    ## Requirements

    To run the scripts `traditional_logs_analysis.py` and `ai-logs_analysis.py`, you need the following dependencies. Create a `requirements.txt` file with the following content:

    ```txt
    numpy
    pandas
    scikit-learn
    ```

    Install the dependencies using:

    ```sh
    pip install -r requirements.txt
    ```

