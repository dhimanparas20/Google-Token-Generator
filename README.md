# Google Token Generator

This project generates `credentials.json` and `token.json` files required to use the Google Drive API. 

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/dhimanparas20/Google-Token-Generator
    ```

2. Navigate to the project directory:
    ```bash
    cd Google-Token-Generator
    ```

3. Activate your Python environment (if you are using a virtual environment):
    ```bash
    source your_virtual_env/bin/activate  # On Unix or MacOS
    your_virtual_env\Scripts\activate     # On Windows
    ```

4. Install the required packages:
    ```bash
    pip3 install -r requirements.txt
    ```

## Usage
1. Rename `config_sample.conf` to `config.conf` and fill the required variables there:


2. Import the `gentoken` module into your Python script (e.g., `app.py`):
    ```python
    import gentoken
    ```

3. Generate the `credentials.json` file by calling `writeCredentialsJson()`:
    ```python
    gentoken.writeCredentialsJson()
    ```

4. Generate the `token.json` file by calling `genTokenJson()`:
    ```python
    gentoken.genTokenJson()
    ```

5. The `genTokenJson()` method also returns an object which u can use as per need:
   

After running the above methods, the `credentials.json` and `token.json` files will be generated.

**Note:** Only run this code on a local machine, not on remote machines.

## Example

Here is an example of how you can use the `gentoken` module in your `app.py` script:

```python
import gentoken

# Generate credentials.json
gentoken.writeCredentialsJson()

# Generate token.json
gentoken.genTokenJson()

print("Credentials and Token files have been generated successfully.")
