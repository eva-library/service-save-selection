[![N|Solid](https://i.ibb.co/LtT31vK/eva-150px.png)](https://eva.bot/)

# Microservice 

## **_Save Selection_**

This micro-service shows with the _EVA_ format the answer with the articles previously saved.

## Technologies 

- GitLab
- Visual Studio Code
- Google Cloud Platform
- Python 3.8
- Postman


## ¿How to start?

We have two modes to prove this micro-service : Local-mode and Cloud-function-mode

### Local-mode

1. Go to the main.py file, delete the word "self" from the line 79 in _test_functions_
2. Execute the main.py file 
3. Go to Postman with the "POST" method
4. Put the url with the function name "guardar_seleccion" example: https://127.0.0.1:8002/guardar_seleccion
5. Put the request format in Body-> Raw -> JSON

### Cloud-function-mode (Google Cloud -> Cloud Functions)

1. Copy the url generated by the Cloud funtion and paste in to the Postman input in the "POST" method
2. Put the request format in Body-> Raw -> JSON

Request format from Json body:

```json
{
    "hiddenContext": {},
    "openContext": {
        "add_code": "LETRERO"
    },
    "visibleContext": {}
}
```

## License

Private software.

