few_shots = [
    {
        'Question': "How many t-shirts do we have left for Nike in XS size and red color?",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Nike' AND color = 'Red' AND size = 'XS'",
        'SQLResult': "Result of the SQL query",
        'Answer': "56",
    },
    {
        'Question': "How much is the total price of the inventory for all S-size t-shirts?",
        'SQLQuery': "SELECT SUM(price*stock_quantity) FROM t_shirts WHERE size = 'S'",
        'SQLResult': "Result of the SQL query",
        'Answer': "19123",
    },
    {
        'Question': "If we have to sell all the Levi’s T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?",
        'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Levi'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "23209.0",
    },
    {
        'Question': "If we have to sell all the Levi’s T-shirts today. How much revenue our store will generate without discount?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Levi'",
        'SQLResult': "Result of the SQL query",
        'Answer': "23209",
    },

    {
        'Question': "If we have to sell all the Nike T-shirts today with discounts applied. How much revenue  our store will generate (post discounts)?",
        'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike'
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "17183.8",
    },
    {
        'Question': "If we have to sell all the Nike T-shirts today. How much revenue our store will generate without discount?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Nike'",
        'SQLResult': "Result of the SQL query",
        'Answer': "18481",
    },

    {
        'Question': "How many white color Levi's shirt I have?",
        'SQLQuery': "SELECT sum(stock_quantity) FROM t_shirts WHERE brand = 'Levi' AND color = 'White'",
        'SQLResult': "Result of the SQL query",
        'Answer': "185",
    },
    {
        'Question': "how much sales amount will be generated if we sell all large size t shirts today in nike brand after discounts?",
        'SQLQuery': """SELECT sum(a.total_amount * ((100-COALESCE(discounts.pct_discount,0))/100)) as total_revenue from
(select sum(price*stock_quantity) as total_amount, t_shirt_id from t_shirts where brand = 'Nike' and size="L"
group by t_shirt_id) a left join discounts on a.t_shirt_id = discounts.t_shirt_id
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "1650.0",
    },
    {
        'Question': "What is the average price of all Adidas t-shirts in black color?",
        'SQLQuery': "SELECT AVG(price) FROM t_shirts WHERE brand = 'Adidas' AND color = 'Black'",
        'SQLResult': "Result of the SQL query",
        'Answer': "21.3333",
    },
    {
        'Question': "How many different sizes of Van Huesen t-shirts are in stock in red color?",
        'SQLQuery': "SELECT COUNT(DISTINCT size) FROM t_shirts WHERE brand = 'Van Huesen' AND color = 'Red'",
        'SQLResult': "Result of the SQL query",
        'Answer': "4",
    },
    {
        'Question': "What is the total number of t-shirts available in medium size across all brands?",
        'SQLQuery': "SELECT SUM(stock_quantity) FROM t_shirts WHERE size = 'M'",
        'SQLResult': "Result of the SQL query",
        'Answer': "557",
    },
    {
        'Question': "What is the total inventory value (before discount) of all Adidas t-shirts?",
        'SQLQuery': "SELECT SUM(price * stock_quantity) FROM t_shirts WHERE brand = 'Adidas'",
        'SQLResult': "Result of the SQL query",
        'Answer': "18949",
    },
    {
        'Question': "Which brand has the highest total stock of white t-shirts?",
        'SQLQuery': """
SELECT brand FROM t_shirts 
WHERE color = 'White' 
GROUP BY brand 
ORDER BY SUM(stock_quantity) DESC 
LIMIT 1
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "Van Huesen",
    },
    {
        'Question': "How much discount percentage is applied on the t-shirt with ID 7?",
        'SQLQuery': "SELECT pct_discount FROM discounts WHERE t_shirt_id = 7",
        'SQLResult': "Result of the SQL query",
        'Answer': "30.00",
    },
    {
        'Question': "What is the average discount percentage across all discounted t-shirts?",
        'SQLQuery': "SELECT AVG(pct_discount) FROM discounts",
        'SQLResult': "Result of the SQL query",
        'Answer': "23.5",
    },
    {
        'Question': "How many t-shirts have a discount of more than 20 percent?",
        'SQLQuery': "SELECT COUNT(*) FROM discounts WHERE pct_discount > 20",
        'SQLResult': "Result of the SQL query",
        'Answer': "5",
    },
    {
        'Question': "What is the highest priced t-shirt in the store?",
        'SQLQuery': "SELECT MAX(price) FROM t_shirts",
        'SQLResult': "Result of the SQL query",
        'Answer': "50",
    },
    {
        'Question': "What is the total stock of Nike and Adidas t-shirts that are either blue or black?",
        'SQLQuery': """
SELECT SUM(stock_quantity) 
FROM t_shirts 
WHERE brand IN ('Nike', 'Adidas') AND color IN ('Blue', 'Black')
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "734",
    },
    {
        'Question': "How many t-shirts are priced above $40?",
        'SQLQuery': "SELECT COUNT(*) FROM t_shirts WHERE price > 40",
        'SQLResult': "Result of the SQL query",
        'Answer': "13",
    },
    {
        'Question': "What is the total revenue lost due to discounts on all t-shirts?",
        'SQLQuery': """
SELECT SUM(price * stock_quantity * (pct_discount/100)) 
FROM t_shirts 
JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "3567.4",
    },
    {
        'Question': "List total inventory value per brand, sorted from highest to lowest.",
        'SQLQuery': """
SELECT brand, SUM(price * stock_quantity) AS total_value 
FROM t_shirts 
GROUP BY brand 
ORDER BY total_value DESC
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "[('Van Huesen', 30375), ('Levi', 23209), ('Adidas', 18949), ('Nike', 18481)]",
    },
    {
        'Question': "How many t-shirt variants do not have any discount applied?",
        'SQLQuery': """
SELECT COUNT(*) 
FROM t_shirts 
WHERE t_shirt_id NOT IN (SELECT t_shirt_id FROM discounts)
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "49",
    },
    {
        'Question': "For each brand, how many t-shirts have discounts applied?",
        'SQLQuery': """
SELECT brand, COUNT(*) AS discounted_count 
FROM t_shirts 
WHERE t_shirt_id IN (SELECT t_shirt_id FROM discounts) 
GROUP BY brand
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "[('Van Huesen', 4), ('Nike', 2), ('Adidas', 24)]",
    },
    {
        'Question': "Which t-shirt has the highest effective discount in terms of dollar value (price * pct_discount)?",
        'SQLQuery': """
SELECT t_shirts.t_shirt_id, (price * pct_discount / 100) AS discount_value 
FROM t_shirts 
JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id 
ORDER BY discount_value DESC 
LIMIT 1
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "10",
    },
    {
        'Question': "If only discounted t-shirts are sold, how much revenue will be generated post-discount?",
        'SQLQuery': """
SELECT SUM(price * stock_quantity * ((100 - pct_discount)/100)) 
FROM t_shirts 
JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "11348.6",
    },
   
    {
        'Question': "Which color of t-shirts has the lowest total stock in the inventory?",
        'SQLQuery': """
SELECT color 
FROM t_shirts 
GROUP BY color 
ORDER BY SUM(stock_quantity) ASC 
LIMIT 1
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "Blue",
    },
    {
        'Question': "What is the additional revenue we could gain if we sold discounted t-shirts at full price?",
        'SQLQuery': """
SELECT SUM(price * stock_quantity * (pct_discount / 100)) 
FROM t_shirts 
JOIN discounts ON t_shirts.t_shirt_id = discounts.t_shirt_id
""",
        'SQLResult': "Result of the SQL query",
        'Answer': "3567.4",
    }
]
