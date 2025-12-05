# CLI-ToDo

A simple command-line todo list manager built with Python using [Typer](https://typer.tiangolo.com/) and [Rich](https://rich.readthedocs.io/).  

› You can make, preview, complete, and delete tasks. All from your terminal.

---

## Installation

- Clone the repo:
```bash
git clone https://github.com/abdelkarimLog/cli-todo.git
cd cli-todo
```

- Install Typer (Rich will come with it):
```bash
pip3 install typer
```


## Usage

### Run with Python:
```bash
python3 todo.py --help
```

### Add a task:
```bash
python3 todo.py add Study
```
```bash
python3 todo.py add "Go Outside"
```

### Preview tasks:
```bash
python3 todo.py list
```
### Preview in table view:
```bash
python3 todo.py list --table #or -t for short
```

### Mark tasks as done:

Select tasks by their number
```bash
python3 todo.py done 1
```
Select all tasks
```bash
python3 todo.py done --all #or -a
```

### Delete tasks
```bash
python3 todo.py delete 2
```
```bash
python3 todo.py delete -a
```

---

This is a learning - practice project, hope you use it. 
