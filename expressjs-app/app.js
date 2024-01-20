// npm init -y
// npm install express python-shell
// npm install cors
const express = require('express');
const { PythonShell } = require('python-shell');
const app = express();
var cors = require('cors')

app.use(cors())
app.use(express.json());

app.post('/predict', (req, res) => {
    console.log("Received request with data:", req.body);

    let options = {
        mode: 'text',
        pythonOptions: ['-u'], // get print results in real-time
        args: [JSON.stringify(req.body.features)]
    };

    PythonShell.run('predict.py', options, function (err, results) {
        if (err) {
            console.error("Error running Python script:", err);
            res.status(500).send(err.message);
        } else {
            console.log("Python script output:", results);
            res.json({ prediction: results[0] });
        }
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
