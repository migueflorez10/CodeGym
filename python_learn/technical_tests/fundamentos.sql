-- Comando SELECT : Apunta a una informacion especifica 
SELECT * FROM users;    

SELECT name FROM users;

SELECT user_id, name FROM users;



-- DISTINCT: Quitar duplicados en el resultado
SELECT DISTINCT * FROM users; -- me trae todos los valores distintos de las columnas

SELECT DISTINCT name FROM users; -- me trae los valores distintos del campo nombre



-- WHERE : Solo dame las filas que cumplan esta condición

SELECT * FROM users WHERE age=23;


-- ORDER BY: Ordenar los resultados

SELECT * FROM users ORDER BY age DESC;
SELECT * FROM users WHERE email='vera777@gmail.com' ORDER BY age DESC;



-- LIKE: “Buscar textos que se parezcan a esto”
SELECT * FROM users WHERE email LIKE '%@gmail%';



-- NOT: “dame todo lo que NO cumpla esto”

SELECT * FROM users WHERE NOT email = 'aristi@gmail.com';
SELECT * FROM users WHERE email NOT IN ('aristi@gmail.com', 'miguel124@gmail.com');



-- LIMIT : “muéstrame solo los primeros 5 papeles”
SELECT * FROM users LIMIT;
SELECT * FROM users WHERE email = 'miguel124@gmail.com' OR age = 28



-- MOD(): “el residuo de dividir a entre b”
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID,2)=0;



-- IS NULL: “no hay valor”, “dato desconocido”, “vacío real”.
SELECT * FROM users WHERE email IS NULL;



/*MIN() y MAX(): son funciones de SQL que sirven para encontrar el valor más
pequeño y el más grande de una columna.
*/
SELECT MIN(age) FROM users;

SELECT MAX(age) FROM users;

SELECT MIN(created_at), MAX(created_at) FROM users;



-- COUNT: Sirve para contar filas.
SELECT COUNT(CITY) - COUNT(DISTINCT CITY) FROM STATION;

SELECT COUNT(email) FROM users; -- CONTAMOS LAS FILAS DE LA COLUMNA EMAIL



-- SUM(): Es la función de SQL que sirve para sumar valores de una columna.
SELECT SUM(amount) FROM orders;

SELECT SUM(amount) FROM orders WHERE status = 'paid';



-- IN: “el valor debe estar dentro de esta lista”
SELECT * FROM users WHERE country IN ('Colombia', 'Mexico', 'Peru');



-- BETWEEN : “entre X y Y, incluyendo X y Y”.
SELECT * FROM users WHERE age BETWEEN 28 AND 50;


-- AS(ALIAS): “muéstralo con este nombre”
SELECT name AS nombre, age AS edad FROM users;

SELECT age AS 'Edad de los usuarios' FROM users;



-- CONCAT: Es como hacer + en Python para strings.
SELECT CONCAT(first_name, last_name) FROM users; -- MiguelFlorez