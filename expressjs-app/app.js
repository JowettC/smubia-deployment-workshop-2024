// npm init -y
// npm install express python-shell
// npm install cors
const express = require('express');
const { PythonShell } = require('python-shell');
const app = express();
var cors = require('cors')

app.use(cors())
app.use(express.json());

const { exec } = require('child_process');

app.post('/predict', (req, res) => {
    console.log("Received request with data:", req.body.features);

    // Construct the Python command
    const argsString = req.body.features.join(',');

    const pythonCommand = `python predict.py [${argsString}]`;


    exec(pythonCommand, (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return res.status(500).send(`Error: ${error}`);
        }
        if (stderr) {
            console.error(`stderr: ${stderr}`);
            return res.status(500).send(`Error: ${stderr}`);
        }
        console.log(`stdout: ${stdout}`);
        res.json({ prediction: stdout.trim() });
    });
});



app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
