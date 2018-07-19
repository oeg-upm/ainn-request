# ainn-request
Request and Answers for Mappings

# To install
1. You need to install pip https://pip.pypa.io/en/stable/installing/
2. Create virtual environment http://docs.python-guide.org/en/latest/dev/virtualenvs/
3. Access the environment variable
4. Install the requirements: run `pip install -r requirements.txt` in the app directory
5. `python app.py`
6. Access http://localhost:5000/graphql on your browser




# Examples

## To add
```
mutation {
  createRequest(
    requesterId: "requester1"
    , datasetId: "dataset1"
    , description: "test description 2"
  ) {
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
```
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
```

## To query the first 2 requests
```
{
  request(first: 2){
    edges{
      node{
        id
        description
        requestedOn
      }
    }
  }
}
```

## NEED to BE MODIFIED

{
  response{
    edges{
      node{
        description
        id
        mappingUrl
      }
    }
  }
}

mutation{
  createResponse(request:{description:"test"},
    description:"test", responderId:"test"){
    response{
      description
      mappingUrl
      respondedOn
      responderId
    }
  }
}