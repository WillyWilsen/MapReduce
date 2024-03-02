SELECT
    COUNT(*) AS total_sales
FROM
    purchases
WHERE
    transaction_time BETWEEN '09:01' AND '10:00';