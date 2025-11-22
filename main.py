import typer, json
from rich import print
from typing_extensions import Annotated
from rich.table import Table

app = typer.Typer(no_args_is_help=True)

with open('tasks.json', "r") as f:
    tasks = json.load(f)

def save():
    with open('tasks.json', "w") as f:
        json.dump(tasks, f, indent=2)

@app.command()
def add(task: Annotated[str, typer.Argument(help="Task name (use \" \" for tasks with multiple words)")]=None):
    """Add a new task"""
    
    if task == None:
      print("You should insert a name after `add` command \nCheck `python3 main.py --help`")
      return
    tasks.append({"name": task, "is_done": False})
    print(f"[green]Task added[/green]: \n{task}")
    save()

@app.command()
def done(task_num: Annotated[int, typer.Argument(help="Task to complete (by number, not name)")]=None, 
         all: Annotated[bool, typer.Option("--all", "-a", help="Mark all as read")]=False):
    """Mark tasks as done (by number)"""
    
    if all:
        for num, task in enumerate(tasks, start=1):
          task["is_done"] = True
        print("[green]All tasks done[/green]")
    elif task_num:
        try:
          done_task = tasks[task_num-1]
          done_task['is_done'] = True
          print(f"[green]Task done \n[strike]{done_task['name']}[/strike][/green]")
        except IndexError:
          print("[red]Invalid task number[/red]")
          print("Run `python3 main.py [b]list[/b]` to see each task with its number")
    else:
        print("No valid option")
    
    save()

@app.command()
def delete(task_num: Annotated[int, typer.Argument(help="Task to delete (by number, not name)")]=None, 
           all: Annotated[bool, typer.Option("--all", "-a", help="Delete all tasks")]=False):
    """Delete tasks (by number)"""

    if all:
        tasks.clear()
        print("[red]All tasks deleted[/red]")
    elif task_num:
        try:
            deleted_task = tasks.pop(task_num-1)
            print(f"[red]Task deleted[/red] \n[strike]{deleted_task['name']}[/strike]")
        except IndexError:
            print("[red]Invalid task number[/red]")
            print("Run `python3 main.py [b]list[/b]` to see each task with its number")
    else:
        print("No valid option")
    save()

@app.command()
def list(table_view: Annotated[bool, typer.Option("--table", "-t", help="Show all tasks in a table")]=False):
  """Show all tasks"""
  
  if tasks == []:
    print("No tasks")
  elif table_view:
    table = Table(title="My Tasks")
    table.add_column("No.", justify="center")
    table.add_column("Task", justify="left", min_width=20)
    table.add_column("Status", justify="center")
    for num, task in enumerate(tasks, start=1):
      if task["is_done"]:
        color = "green"
        decoration = "strike"
        icon = ":white_check_mark:"
      else:
        color = "yellow"
        decoration = "none"
        icon = ":hourglass_flowing_sand:"
      table.add_row(str(num), f"[{color}][{decoration}]{task['name']}[/{decoration}][/{color}]", icon)
    print(table)
  else:
    for num, task in enumerate(tasks, start=1):
      if task["is_done"]:
        color = "green"
        decoration = "strike"
      else:
        color = "yellow"
        decoration = "none"
      print(f"[{color}][{num}] [{decoration}]{task['name']}[/{decoration}][/{color}]")

if __name__ == "__main__":
    app()
