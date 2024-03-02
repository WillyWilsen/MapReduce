SELECT
    COUNT(*) AS total_sales
FROM
    purchases
WHERE
    transaction_time BETWEEN '10:01' AND '11:00';