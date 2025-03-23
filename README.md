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
Before running the `generate.dockerfile.py` script, ensure you have the following setup:

1. **Python**: Make sure Python 3.6 or higher is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **pip**: Ensure you have `pip` installed. You can install it using:
    ```sh
    python -m ensurepip --upgrade
    ```

3. **Required Python Packages**: Install the necessary Python packages by running:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Script

To generate the Dockerfile, run the following command:
```sh
python generate.dockerfile.py
```

## Changing the Port for Ollama

If you encounter port conflicts with Ollama, you can change the port and run the server using the following commands:

```sh
set OLLAMA_HOST=127.0.0.1:6000
ollama serve
```

Replace `6000` with the port number you want to use.


