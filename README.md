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

2. Install PyTorch and torchvision:
    check installation command based on your machine [here](https://pytorch.org/get-started/locally/)
    or just
    ```bash
    pip install torch torchvision
    ```

3. Install Server dependencies:
    ```bash
    pip install flask
    pip install torch
    pip install numpy
    pip insatll pillow
    pip install pillow-heif
    ```

Once you have completed these steps, you are ready to run the server using the following command:
```bash
flask run
```
