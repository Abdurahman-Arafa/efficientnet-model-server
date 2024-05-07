## Prerequisites
Make sure your python version >= 3.8 to run pytorch.

You can check your python version by running the following command:
```bash
python --version
```
Before running the server, please make sure you have set up a virtual environment and installed the necessary dependencies. Here are the steps:

1. Activate the virtual environment:
    ```bash
    source <venv_name>/bin/activate  # for Linux/Mac
    . <venv_name>/Scripts/activate  # for Windows
    ```
2. Install Dependencies
    to install pytorch and torchvision check installation command based on your machine [here](https://pytorch.org/get-started/locally/)
    or just install them with the rest of the dependencies using this command:
    ```bash
    pip install -r requirements.txt
    ```
    if you're facing problems with the requirements file, you can install manually with:
    ```bash
    pip install torch torchvision flask numpy pillow pillow-heif
    ```

Once you have completed these steps, you are ready to run the server using the following command:
```bash
flask run
```
or on linux:
```bash
pip install gunicorn
```
and then run it with:
```bash
gunicorn app:app
```
