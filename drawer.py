import polars as pl
import plotly.express as px

class DataDrawer:
    def __init__(self, path:str):
        self.df = pl.read_csv(path)


    def plot_stores(self):
        try:
            df = self.df
            df_store_sales = df.group_by('store_id').agg(pl.col('quantity').sum())

            fig = px.bar(df_store_sales.to_pandas(), x='store_id', y='quantity', title='مقایسه فروشگاه‌ها',
                        labels={'store_id':'آیدی فروشگاه', 'quantity':'تعداد فروش'}, template='plotly_dark')
            return fig
        
        except Exception as e:
            print(f'Error in plot_Stores function: {e}')


    def store_sales(self, ID):
        try:
            df = self.df
            df_store_ID = df.filter(pl.col("store_id") == ID)
            df_daily_sales = df_store_ID.group_by("date").agg(pl.col("quantity").sum())

            fig = px.bar(df_daily_sales.to_pandas(), x="date", y="quantity",
                        title=f"آمار فروش فروشگاه {ID}", template='plotly_dark'
                        , labels={'date':'تاریخ', 'quantity':'تعداد فروش'})
            return fig
        
        except Exception as e:
            print(f'Error in store_sales function: {e}')


    def product_sales(self, ID, Prod):
        try:
            df = self.df
            df_product = df.filter((pl.col("product") == Prod) & (pl.col("store_id") == ID))
            df_product_sales = df_product.group_by("date").agg(pl.col("quantity").sum())

            fig = px.bar(df_product_sales.to_pandas(), x="date", y="quantity",
                        title=f"فروش محصول {Prod}", template='plotly_dark',
                        labels={'date':'تاریخ', 'quantity':'تعداد فروش'})
            return fig
        
        except Exception as e:
            print(f'Error in product_sales function: {e}')
    

    def sales_pie(self, ID):
        try:
            df = self.df
            df_store_product_sales = df.group_by(['store_id', 'product']).agg(pl.col('quantity').sum())

            df_store_sales = df_store_product_sales.filter(pl.col('store_id') == ID)

            fig = px.pie(df_store_sales.to_pandas(), values='quantity', names='product',
                        title=f'توزیع فروش فروشگاه {ID}', template='plotly_dark')
            return fig
        
        except Exception as e:
            print(f'Error in product_sales function: {e}')
    

    def rush_hour(self, ID):
        try:
            df = self.df
            df_hour = df.filter((pl.col('store_id')==ID))
            df_hour = df_hour.group_by('hour').agg(pl.col('quantity').sum())
            df_hour = df_hour.sort('hour')

            fig = px.bar(df_hour.to_pandas(), x="hour", y="quantity",
                        title=f"فروش محصولات در روز", template='plotly_dark',
                        labels={'hour':'ساعت', 'quantity':'تعداد فروش'})
        
        except Exception as e:
            print(f'Error in product_sales function: {e}')