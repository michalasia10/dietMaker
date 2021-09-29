import pandas as pd

IMPORTANT_COLUMNS = ['url', 'products_name', 'brands',
                     'countries', 'image_url', 'image_small_url', 'enegry-kcal_100g', 'fat_100g',
                     'carbohydrates_100g', 'sugars_100g', 'proteins_100g', 'salt_100g', 'categories_tags']

PATH = "en.openfoodfacts.org.products.csv"

file = pd.read_csv(PATH,
                   sep='\t',
                   encoding='UTF-8',
                   low_memory=False)

# delete rows without kcal and useless columns
df = file[file['energy-kcal_100g'].notna()]

# keep only products avaible in Poland
df = df[df['countries'].isin(['Poland', 'Polska', 'Pologne']) == True][IMPORTANT_COLUMNS]

# drop duplicated products
df = df.drop_duplicates(['products_name', 'brands'], keep='last')[df['product_name'].notna()]

# save df
df.to_csv('products_in_poland.csv')
