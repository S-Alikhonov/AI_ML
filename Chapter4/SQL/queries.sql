SELECT * FROM film;

SELECT
	district,
	postal_code,
	phone
FROM address;

SELECT
	address || ', ' || 
	district || ', ' ||
	postal_code as full_address
FROM address;

SELECT
	customer_id,
	first_name,
	last_name
FROM 
	customer
WHERE
	first_name LIKE 'J%';

SELECT
	payment_id,
	amount,
	payment_date
FROM 
	payment
WHERE
	amount BETWEEN 3 AND 5;


SELECT
	payment_id,
	amount,
	payment_date
FROM 
	payment
WHERE
	payment_date BETWEEN '2007-02-15' AND '2007-02-20';

SELECT
	film_id,
	title,
	rating,
	rental_rate
FROM 
	film
WHERE
	film_id IN (SELECT film_id FROM inventory );

SELECT
	payment_id,
	amount,
	payment_date
FROM 
	payment
WHERE
	amount BETWEEN 4 AND 6
ORDER BY
	payment_date DESC;

SELECT
	first_name,
	last_name
FROM 
	customer
ORDER BY
	first_name DESC
LIMIT 
5

SELECT
	first_name,
	last_name
FROM 
	customer
ORDER BY
	first_name ASC
LIMIT 5 OFFSET 10

INSERT INTO customer(store_id,
					 first_name,
					 last_name,
					email,
					address_id)
VALUES 
	(1,'Name1','Surname1','new1@email.com',1),
	(1,'Name2','Surname2','new2@email.com',1),
	(1,'Name3','Surname3','new3@email.com',1),
	(1,'Name4','Surname4','new4@email.com',1),
	(1,'Name5','Surname5','new5@email.com',1) RETURNING *;;

	
UPDATE customer
SET first_name = 'Name2New'
WHERE customer_id = 602 RETURNING *;

DELETE FROM customer
WHERE customer_id = 605

--  or there is more logical way
 
DELETE FROM customer
WHERE customer_id IN(SELECT customer_id FROM customer ORDER BY customer_id DESC LIMIT 1) RETURNING *;
