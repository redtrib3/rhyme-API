[![Deploy](https://button.deta.dev/1/svg)](https://deta.sh/)

# Rhymes API
API to GET rhymes for a specific word.

## Documentation [/docs](https://rhymes.herokuapp.com/docs) :

![Screenshot at 2022-09-24 15-09-57](https://user-images.githubusercontent.com/68897241/192091283-b74faa97-8d31-48ee-b2d9-ffb8f59b35a8.png)

## Endpoints:
```
    |_. /rhyme/{word}
      [parameters: count= return count]
```
### Example:
  URL: ` https://zgzert.deta.dev/rhyme/example?count=4 `

### Output:
```
{
    "example": [
        "ampal", 
        "ample", 
        "hampel", 
        "hample"
    ], 
    "COUNT": 4, 
    "maxCount": 8
}
```

# Made with [FastAPI](https://fastapi.tiangolo.com/) :
![FastAPI_logo](https://user-images.githubusercontent.com/68897241/192091105-9411e961-6e57-484a-951d-865224450fbe.png)


Old URL:  ~~https://rhymes.herokuapp.com/docs/~~
