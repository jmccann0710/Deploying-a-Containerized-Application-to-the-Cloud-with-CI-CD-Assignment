const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello from my containerized app!');
});

if (process.env.NODE_ENV !== 'test') {
    app.listen(3000, '0.0.0.0', () => {
        console.log('Server running on port 3000');
    });
}

module.exports = app;