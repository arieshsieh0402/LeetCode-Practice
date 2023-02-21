SELECT
  Product.product_id,
  Product.product_name
FROM
  Product
LEFT JOIN Sales
ON Sales.product_id = Product.product_id
GROUP BY
  Product.product_id,
  Product.product_name
HAVING MAX(Sales.sale_date) <= CAST('2019-03-31' as DATE)
   AND MIN(Sales.sale_date) >= CAST('2019-01-01' as DATE)
   