ALTER TABLE products
ADD CONSTRAINT fk_products_categories
FOREIGN KEY products(category_id)
REFERENCES categories(id);
