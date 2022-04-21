# python GraphQL demo project
This project implements Python (Flask) with GraphQL Server implementing SQLAlchemy, graphene, and PostgreSQL

### Local Project Setup
#### Python version: 3.9
1. Run PostgreSQL using docker

```shell
docker run --name postgresql -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres
```

2. Install requirements
```shell
pip install -r services/python_graphql/requirements.txt
```

3. Setup env variables 

```shell
export db_name=demo
export db_username=postgres
export POSTGRES_PASSWORD=password
export db_ip_address=127.0.0.1
```

3. Run main.py
4. Go to http://127.0.0.1:5000/graphql_demo in your browser

### GraphQL queries examples

```text
{
  books {
    name,
    id,
    author,
    genreId
  }
}

{
  booksByName(name: "NAME") {
    name,
    id,
    author,
    genreId
  }
}

{
  genres {
    id,
    name
  }
}
```
### GraphQL mutations examples
```text
mutation {
  createBook(input: {name: "new_book", author: "AUTHOR",genreId: 1}) {
    book {
      id,
      name,
      author,
      genreId
    },
    err
  }
}

mutation {
  deleteBook(input: {name: "new_book"}) {
    ok,
    err
  }
}

mutation {
  createCharacter(input: {name: "CHARACTER", bookId: 1}) {
    character {
      name,
      bookId
    }
    ok,
    err
  }
}

mutation {
  createGenres(input: {name: "action"}) {
    genres {
      id,
      name
    },
    ok,
    err
  }
}
```
