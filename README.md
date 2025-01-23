# Local Python Debugging example with Debugpy

## VSCode setup

- Install plugin in your VSCode workspace

> Name: Python
Id: ms-python.python
Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
Version: 2024.22.2
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python

## Project setup

1. Create virtual environment: `python3 -m venv ./venv`
2. Entry the python virtual environment: `source ./venv/bin/activate`
3. Pip install dependencies: `pip install --no-cache-dir -r requirements.txt`

## Try the example

### launch the program via plugin

1. Open anyone the `example/*.py`, for example: `example/two_sum.py`
2. Add breakpoints, conditional breakpoints or logpoints.
3. In the sidebar, select `RUN AND DEBUG` > select `Python: All by plugin` > Click `Start Debugging` \ Click `F5`
4. Observe the execution flow and value of variables in the debugger

### launch the program via debugpy cli (debugpy as listener)

1. Open anyone the `example/*.py`, for example: `example/two_sum.py`
2. Add breakpoints, conditional breakpoints or logpoints.
3. In terminal, execute `python3 -m debugpy --listen localhost:5678 --wait-for-client example/two_sum.py`.
4. In the sidebar, select `RUN AND DEBUG` > select `Python Debugger: Client connects to debugpy listening` > Click `Start Debugging` \ Click `F5`.
5. Observe the execution flow and value of variables in the debugger

### launch the program via debugpy cli (debugpy connect to client)

1. Open anyone the `example/*.py`, for example: `example/two_sum.py`
2. Add breakpoints, conditional breakpoints or logpoints.
3. In the sidebar, select `RUN AND DEBUG` > select `Python Debugger: Client listens to debugpy connection` > Click `Start Debugging` \ Click `F5`.
4. In terminal, execute `python3 -m debugpy --connect localhost:5678 --wait-for-client example/two_sum.py`.
5. Observe the execution flow and value of variables in the debugger

### launch the program via debugpy api (debugpy as listener)

1. Open anyone the `example/*.py`, for example: `example/two_sum.py`
2. Uncomment the `# import debugpy`, `# debugpy.listen(5678)`, `# debugpy.wait_for_client()`.
3. Add breakpoints, conditional breakpoints or logpoints.
4. In terminal, execute `python3 example/two_sum.py`.
5. In the sidebar, select `RUN AND DEBUG` > select `Python Debugger: Client listens to debugpy connection` > Click `Start Debugging` \ Click `F5`.
6. Observe the execution flow and value of variables in the debugger