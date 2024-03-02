SELECT
    p.store,
    p.price AS max_price,
    p.item
FROM
    purchases p
JOIN (
    SELECT
        store,
        MAX(price) AS max_price
    FROM
        purchases
    WHERE
        store IN ('Miami', 'San Francisco', 'Atlanta')
    GROUP BY
        store
) AS max_prices
ON
    p.store = max_prices.store
    AND p.price = max_prices.max_price;