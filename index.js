const express = require('express');

const app = express();
const port = 3000;


//define index route
app.get('/', (req, res) => {
    res.send('Hello World!')
})



//listen to port
app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})