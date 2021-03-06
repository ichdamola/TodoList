# INTRODUCTION -> TodoList
A Django service that exposes an API using GraphQL to manage a text todo list.
This API allows a user to perform the following functionalities:

- Add an item to the todo list.
- Fetch a list of all items in the todo list.
- Delete an item from the todo list.
- Search the list of items in the todo list that contain a search text.

# Project Setup Locally
1. Clone repo
```git clone git clone https://github.com/ichdamola/TodoList.git```
2. Create virtual environment
```cd TodoList```
```virtualenv env```
3. Activate env
```source env/bin/activate```
4. Setup django secret_key
- ```touch .env``` at the root folder
- copy the SECRET_KEY from [```secret_key.txt```](https://github.com/ichdamola/TodoList/blob/main/secret_key.txt) file in the root folder,
- paste it into the ```.env``` file in the format: 
- ```SECRET_KEY=<'the key'>```.
5. Install dependencies
```python install -r requirements.py```
6. Commit model to ORM
```python manage.py makemigrations```
7. Migrate model to db
```python manage.py migrate```
8. Start app server
```python manage.py runserver```
9. GraphQL link
```localhost:8000/graphql```
### Accessing Admin panel
1. Browse url
```localhost:8000/admin```
2. Login
```username: damola```
```password: p@55w@rd```
### Create login to admin(if login didnt work!)
```python manage.py createsupersuer```


## Test queries
### Create Project -> pattern

```json
mutation myProjectMutation {
    createProject(name: "hit the gym"){
    ok
  }  
}
```
### Create Task -> pattern

```json
mutation myTaskMutation {
    createTask(name: <"test task">, text: <"test task body">, projectid: <id>) {
        task {
          id,
        	name
        }
    ok
    }
}
```

### Delete a Task -> query pattern
```json
mutation myTaskMutation {
    deleteTask(id: <id>) {
    ok
    }
}
```

### Search text -> query pattern

```json
query {
  tasks(search: <"text to be search">){
    id,
    name
  }
}
```


### Fetch all items -> query pattern

```
query {
  projects{
    id,
    name
  }
}
```

