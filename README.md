# ainn-request
Request and Answers for Mappings

# To install
1. You need to install pip https://pip.pypa.io/en/stable/installing/
2. Create virtual environment http://docs.python-guide.org/en/latest/dev/virtualenvs/
3. Access the environment variable
4. Install the requirements: run `pip install -r requirements.txt` in the app directory
5. `python app.py`



# Examples

## To add
```
mutation {
  createRequest(description: "test") {
    request {
      description
    }
  }
}
```

## To query all
```
{
  request{
    edges{
      node{
        description
      }
    }
  }
}
```

## To query with filter
{
  request(description: "test"){
    edges{
      node{
        id
        description
        requestedOn
      }
    }
  }
}

