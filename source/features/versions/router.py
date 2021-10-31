from fastapi import APIRouter

from source.features.product.api.v0_3 import version as product_0_3
from source.features.category.api.v0_3 import version as category_0_3
from source.features.ingredient.api.v0_3 import version as ingredient_0_3
from source.features.recipe.api.v0_3 import version as recipe_0_3
from source.features.unit.api.v0_3 import version as unit_0_3
from source.features.user.settings.api.v0_3 import version as settings_0_3
from source.features.user.account.api.v0_3 import version as account_0_3
from source.features.user.meal.api.v0_3 import version as meal_0_3
from source.features.user.week.api.v0_3 import version as week_0_3

ROUTERS_V_0_3 = [product_0_3, category_0_3, ingredient_0_3, recipe_0_3,
                 unit_0_3, settings_0_3, account_0_3, meal_0_3,week_0_3]


basic = APIRouter(
    prefix="/",
    tags=["/"],
)

version_0_3 = APIRouter(
    prefix="/v0.3",
    tags=["v0.3"],
)


for route in ROUTERS_V_0_3:
    basic.include_router(route)
    version_0_3.include_router(route)
