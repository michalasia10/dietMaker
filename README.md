# DietMaker
---


Application assumptions: An application that allows you to 
enjoy normal food without worrying about exceeding your macronutrients.

## API
https://dietmaker.herokuapp.com/

## ENDPOINTS

### CATEGORY
---
@GET
*/category/* <br />
return: Get all category objects 
```
[
  {
    "name": "Healthy Food",
    "pict_url": "https://media.istockphoto.com/photos/super-food-for-a-healthy-diet-picture-id1081090762?k=20&m=1081090762&s=612x612&w=0&h=8ESzOOTykppA-UC6YpPMvJWLlxNSebbPZyzj3ph2IlM=",
    "id": 1
  },
  // ...
]
```

@GET
*category/{category_id}/recipes* <br />
return: Category objects with recipes belong to category
```
{
  "name": "Healthy Food",
  "pict_url": "https://media.istockphoto.com/photos/super-food-for-a-healthy-diet-picture-id1081090762?k=20&m=1081090762&s=612x612&w=0&h=8ESzOOTykppA-UC6YpPMvJWLlxNSebbPZyzj3ph2IlM=",
  "id": 1,
  "recipes": [
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
    },
    // ...
  ]
}
```

### PRODUCT
---
@GET
*/product/* <br />
return: Get all product objects with pagination default : limit 50 , offset 0 <br />
optional: /product with query /product?limit=50&offset=0 <br />
return: Get all product objects from 0 to 50 id in db


``` 
{
  "items": [
    {
      "code": 32164,
      "name": "Yellow rice",
      "pict_url": "https://images.openfoodfacts.org/images/products/001/740/010/5051/front_en.11.200.jpg",
      "protein": 7.0175438596491,
      "carbo": 77.19298245614,
      "fat": 0,
      "kcal": 350.87719298246,
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
    ],
  "total": 2020,
  "limit": 50,
  "offset": 0
}

```

@GET
**/product/<product_id : int>**<br />  
return: Product with specific id
```
{
  "code": 32164,
  "name": "Yellow rice",
  "pict_url": "https://images.openfoodfacts.org/images/products/001/740/010/5051/front_en.11.200.jpg",
  "protein": 7.0175438596491,
  "carbo": 77.19298245614,
  "fat": 0,
  "kcal": 350.87719298246,
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

### RECIPE
---
@GET
*/recipe/* <br />
return: Get all recipes objects with pagination default : limit 50 , offset 0 
optional: /recipe with query /recipe?limit=50&offset=0 <br />
return: Get all recipe objects from 0 to 50 id in db
```
  "items": [
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
              "code": 540958,
              "name": "Ryż biały długoziarnisty",
              "pict_url": "https://images.openfoodfacts.org/images/products/20053963/front_pl.3.200.jpg",
              "protein": 6.7,
              "carbo": 79,
              "fat": 0.7,
              "kcal": 353
            }
          ],
          "recipe_id": 3
        },
        // ...
      ]
    },
    // ...
  ],
  "total": 3,
  "limit": 50,
  "offset": 0
}
```