# DietMaker
---


Application assumptions: An application that allows you to 
enjoy normal food without worrying about exceeding your macronutrients.

## API
https://dietmaker.herokuapp.com/

## ENDPOINTS

### PRODUCT
---
@GET
*/product/* <br />
return: Get all product objects 


``` 
 [
  {
    "name": "Yellow rice",
    "pict_url": "https://images.openfoodfacts.org/images/products/001/740/010/5051/front_en.11.200.jpg",
    "protein": 7.0175438596491,
    "carbo": 77.19298245614,
    "fat": 0,
    "id": 1,
    "description": "",
    "tags": [
      {
        "id": 1,
        "name": "Żywność i napoje na bazie roślin"
      },
      // ...
    ]
  },
  // ...
]

```

@GET
**/product/<product_id : int>**<br />  
return: Product with specific id
```
{
  "name": "Yellow rice",
  "pict_url": "https://images.openfoodfacts.org/images/products/001/740/010/5051/front_en.11.200.jpg",
  "protein": 7.0175438596491,
  "carbo": 77.19298245614,
  "fat": 0,
  "id": 1,
  "description": "",
  "tags": [
    {
      "id": 1,
      "name": "Żywność i napoje na bazie roślin"
    },
    // ...
  ]
}
```

@DELETE
**/product/delete/<product_id : int>**<br />
return: Delete object from Product table with specific id

### PRODUCT
---
@GET
*/recipe/* <br />
return: Get all recipes objects 
```
[
  {
    "name": "Ryż z indykiem",
    "pict_url": "https://image.shutterstock.com/image-photo/indian-cuisinehealthy-tasty-homemade-chicken-260nw-658631542.jpg",
    "category_id": 1,
    "id": 3,
    "ingredients": [
      {
        "amount": 100,
        "unit": [
          {
            "name": "gram"
          }
        ],
        "product": [
          {
            "name": "Ryż biały długoziarnisty",
            "pict_url": "https://images.openfoodfacts.org/images/products/20053963/front_pl.3.200.jpg",
            "protein": 6.7,
            "carbo": 79,
            "fat": 0.7
          }
        ],
        "recipe_id": 3
      },
      // ...
  // ...
]
```