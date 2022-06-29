ALTER TABLE products
ADD CONSTRAINT fk_cproducts_categories
FOREIGN KEY products(category_id)
REFERENCES categories(id);