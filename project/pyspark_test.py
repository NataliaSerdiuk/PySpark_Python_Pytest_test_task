from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("test").getOrCreate()

products = [(1, 'Смартфон Samsung Galaxy'),
            (2, 'Смартфон Apple iPhone'),
            (3, 'Ноутбук игровой MSI Titan'),
            (4, 'Ноутбук Apple MacBook'),
            (5, 'Телевизор LG'),
            (6, 'Телевизор Samsung'),
            (7, 'Телевизор Xiaomi'),
            (8, 'Холодильник двухкамерный Sharp'),
            (9, 'Винный шкаф'),
            (10, 'Стиральная машина Bosch'),
            (11, 'Пакет'),
            (12, 'Коробка')]
products_column = ["product_id", "product_name"]
products_df = spark.createDataFrame(data=products, schema=products_column)

category = [(1, 'Электроника', 1),
            (1, 'Электроника', 2),
            (1, 'Электроника', 3),
            (1, 'Электроника', 4),
            (1, 'Электроника', 5),
            (1, 'Электроника', 6),
            (1, 'Электроника', 7),
            (2, 'Бытовая техника', 8),
            (2, 'Бытовая техника', 9),
            (2, 'Бытовая техника', 10),
            (3, 'Телефоны и смартфоны', 1),
            (3, 'Телефоны и смартфоны', 2),
            (4, 'Компьютеры и ноутбуки', 3),
            (4, 'Компьютеры и ноутбуки', 4),
            (5, 'Телевизоры,аудио-/видеотехника', 5),
            (5, 'Телевизоры,аудио-/видеотехника', 6),
            (5, 'Телевизоры,аудио-/видеотехника', 7),
            (6, 'Холодильники', 8),
            (6, 'Холодильники', 9),
            (7, 'Стиральные и сушильные машины', 10)]
category_column = ["category_id", "category_name", "product_id"]
categories_df = spark.createDataFrame(data=category, schema=category_column)

result_df = products_df.join(categories_df, products_df.product_id == categories_df.product_id, how="left") \
    .select(products_df['product_name'], categories_df['category_name'])
result_df = result_df.withColumnRenamed("product_name", "Имя продукта")
result_df = result_df.withColumnRenamed("category_name", "Имя категории")
result_df.show(result_df.count(), truncate=False)

spark.stop()