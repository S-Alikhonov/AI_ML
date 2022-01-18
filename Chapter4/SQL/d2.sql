
-- Select film title description and release year join category table.
-- Name column names with table name by using snake case

SELECT
	title as film_title,
	description as film_description,
	category.name as category_name
	FROM film
	
	INNER JOIN film_category USING(film_id)
	INNER JOIN category USING(category_id);

-- Select customer and their address join country and city tables
-- Name column names with table name by using snake case.

SELECT 
	c.customer_id,
	c.first_name || ' ' || c.last_name customer_full_name,
	a.address || ', ' || a.district || ', ' || a.postal_code  AS customer_address,
	city city_name,
	country country_name,

    -- column aliases used to join columns from different tables to create full address
	a.address || ', ' || a.district || ', ' || a.postal_code
	|| ', ' || city || ', ' || country AS full_adress
	
FROM customer c
INNER JOIN address a USING(address_id)
INNER JOIN  city USING(city_id)
INNER JOIN country USING(country_id);
 

-- Question 3 :
-- Select all payments info including staff info, customer info, and rental info.
-- Name column names with table name by using snake case.

SELECT 
	p.amount payment_amount,
	p.payment_date,
	s.staff_id,
	s.first_name || ' ' || s.last_name staff_full_name,
	c.first_name || ' ' || c.last_name customer_full_name,
	r.rental_date,
	r.return_date
FROM payment p
INNER JOIN staff s 
	ON (p.staff_id = s.staff_id)
INNER JOIN customer c
	ON (p.customer_id = c.customer_id)
INNER JOIN rental r USING(rental_id);
 

 

-- Question 4 :
-- Select all the actors and films and join them
-- Name column names with table name by using snake case.
-- HINT : You need to use groupby

SELECT
 	a.first_name || ' ' ||  a.last_name actor_full_name,
	f.title film_title
FROM actor a
INNER JOIN film_actor USING(actor_id)
INNER JOIN film f USING(film_id)
 

-- Question 5 :
-- Select all the stores with addresses and manager staff name last name.

SELECT
	s.store_id store_store_id,
	a.address || ', ' || a.district address_full_address,
	staff.first_name || ' ' || staff.last_name staff_manager_name
FROM store s
INNER JOIN address a USING(address_id)
INNER JOIN  staff ON (s.manager_staff_id = staff.staff_id);


-- Question 6 :
-- In this store, every worker receives 1500 $ base salary
-- After the 5000th movie, they get a bonus of 0.1 euro for every movie they rent.
-- Calculate total bonus that is received by staff members and join their names and last_names

-- by rentals they proceeded
SELECT
	s.staff_id,
	s.first_name || ' ' || s.last_name staff_full_name,
	CASE 
		WHEN (COUNT(rental_id) -5000)>0  THEN (COUNT(rental_id) -5000)*0.1
		ELSE 0
		END AS staff_bonus
FROM staff s
INNER JOIN rental r USING(staff_id)
GROUP BY s.staff_id,staff_full_name

-- by payment transaction they received from customer
SELECT
	s.staff_id,
	s.first_name || ' ' || s.last_name staff_full_name,
	CASE 
		WHEN (COUNT(payment_id) -5000)>0  THEN (COUNT(payment_id) -5000)*0.1
		ELSE 0
		END AS staff_bonus
FROM staff s
INNER JOIN payment USING(staff_id)
GROUP BY s.staff_id,staff_full_name


SELECT rental_id,
COUNT(payment_id)
FROM rental
INNER JOIN payment USING(rental_id)
GROUP BY rental_id
HAVING COUNT(payment_id)>1