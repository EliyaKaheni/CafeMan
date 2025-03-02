import polars as pl

def read_file(dir='../data/Products.csv'):
    df = pl.read_csv(dir)
    return df

def write_file(df, dir='../data/Products.csv') -> None:
    df.write_csv(dir)

def add(product: str, ingredients: dict, prices: int):
    df = read_file()
    new_rows = []
    for ingredient, quantity in ingredients.items():
        new_rows.append({
            'Product': product,
            'Ingredient': ingredient,
            'Price': prices,
            'Quantity': quantity
        })
    new_df = pl.DataFrame(new_rows)
    df = pl.concat([df, new_df])
    write_file(df)

def remove_item(product: str):
    df = read_file()
    df = df.filter(pl.col("Product") != product)
    write_file(df)

def check_recipe():
    df = read_file()
    have = {}




def compare(have: dict) -> dict:
    status = {}
    want = check_recipe()

    for prod in want:
        status[prod] = want[prod] <= have[prod]

    return status