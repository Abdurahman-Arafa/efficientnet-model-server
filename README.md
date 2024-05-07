## Deployment:
- Build Command:
    ```bash
    pip install -r requirements.txt
    ```
- Run Command:
    ```bash
    gunicorn app:app
    ```
if you need to modify any of the run parameters refer to the 
[docs](https://docs.gunicorn.org/en/stable/run.html#commonly-used-arguments)

## Hosting Locally:
Make sure your python version >= 3.8 to run pytorch.

You can check your python version by running the following command:
```bash
python --version
```
Before running the server, please make sure you have set up a virtual environment
(recommended) and installed the necessary dependencies.

Here are the steps:

1. based on your OS [Create](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
and [Activate](https://docs.python.org/3/library/venv.html#how-venvs-work) a virtual environment

2. Install Dependencies
    - idealy you should be able to just run 
    ```bash
    pip install -r requirements.txt
    ```
    - if that doesn't work, install them manually with this command:
    ```bash
    pip install torch torchvision flask numpy pillow pillow-heif gunicorn
    ```

Once you have completed these steps, you are ready to run the server using the following command:
```bash
gunicorn app:app
```
