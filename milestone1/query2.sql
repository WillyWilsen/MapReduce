SELECT
    SUM(price) AS total_sales
FROM
    purchases
WHERE
    item LIKE '%Toys%';