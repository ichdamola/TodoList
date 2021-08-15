# INTRODUCTION -> TodoList
A Django service that exposes an API using GraphQL to manage a text todo list.
This API allows a user to perform the following functionalities:

- Add an item to the todo list.
- Fetch a list of all items in the todo list.
- Delete an item from the todo list.
- Search the list of items in the todo list that contain a search text.

## Test queries
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
  tasks(search: <"text to be search">){
    id,
    name
  }
}
```

