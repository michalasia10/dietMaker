from typing import List

import pandas as pd
from googletrans import Translator
from sqlalchemy.orm import Session

from source.core.db_queries.crud import check_exist_by_name, get_by_code, simple_object_creator
from source.features.product.models import Product, Tag

FILE = 'source/resources/products_in_poland_2021_09_27_14_12.csv'
DATAFRAME = pd.read_csv(FILE)


def tags_translator(tags: List[str]) -> List[str]:
    translator = Translator()
    if tags and not isinstance(tags, float):
        tags = tags.split(',')
        translatedTags = [translator.translate(tag[3:].replace('-', ' ').strip('.').lower(), dest='pl').text for tag in
                          tags if tag]
        return translatedTags


def tag_creator(db: Session, tags: List[str], code: int):
    for tag in tags:
        tagDict = {
            'name': tag,
        }
        tagExist = check_exist_by_name(db, Tag, tagDict).first()
        if tagExist:
            product = get_by_code(db, Product, code).first()
            product.tags.append(tagExist)
            db.commit()
            print(f"{tag} added to {product.name}")
        else:
            tag = simple_object_creator(db, Tag, **tagDict)
            print(f"Tag {tagDict['name']} created")
            product = get_by_code(db, Product, code).first()
            tagNew = check_exist_by_name(db, Tag, tagDict).first()
            product.tags.append(tagNew)
            print(f"{tagNew} added to {product.name}")
            db.commit()


def product_creator(db: Session, dataframe: pd.DataFrame = DATAFRAME):
    for idx, row in enumerate(dataframe[134:].itertuples()):
        code = row._1
        name = row.product_name
        pict_url = row.image_small_url
        protein = row.proteins_100g
        carbo = row.carbohydrates_100g
        fat = row.fat_100g
        kcal = row._8
        simple_object_creator(db, Product,
                              code=code,
                              name=name,
                              pict_url=pict_url,
                              protein=protein,
                              carbo=carbo,
                              fat=fat,
                              kcal=kcal)
        print(f"ID.{idx + 1} CODE: {code}. Created {name}")
        tags = tags_translator(row.categories_tags)
        if tags:
            tag_creator(db, tags, code)
