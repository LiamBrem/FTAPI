const express = require('express');
//add pool
const { Pool } = require('pg');

const app = express();
const port = 3000;

// PostgreSQL configuration
const pool = new Pool({
    user: 'your_postgresql_username',
    host: 'localhost', // Change to your PostgreSQL host if necessary
    database: 'myappdb', // Replace with your database name
    password: 'your_postgresql_password',
    port: 5432, // Default PostgreSQL port
  });
  
  // Test the database connection
  pool.connect()
    .then(() => console.log('Connected to PostgreSQL'))
    .catch(err => console.error('Error connecting to PostgreSQL', err));
  
  // Your Express routes and middleware go here


//define index route
app.get('/', (req, res) => {
    res.send('Hello World!')
})

//listen to port
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})