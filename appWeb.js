

// Requiring express in our server
const express = require('express');
const app = express();



const { exec } = require('child_process');


app.get('/', function(req, res) {
    res.json(
        {'msg' : 'Server rodando...'}
    );
});

// Defining get request at '/multiple' route
app.get('/executar/Niack_Supremo', function(req, res) {
    
    console.log("Reiniciando server Niack")

    exec(`pm2 restart Niack_Supremo`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
        }
        
        console.log("==Tudo pronto para começar==")
        console.log( "" )

        res.json(
            {'msg' : stdout}
        );
    });    
});



// Defining get request at '/multiple' route
app.get('/executar/EscobarTramps', function(req, res) {
    
    console.log("Reiniciando server EscobarTramps")

    exec(`pm2 restart EscobarTramps_Supremo`, (error, stdout, stderr) => {
        if (error) {
            console.log(`error: ${error.message}`);
            return
        }
        if (stderr) {
            console.log(`stderr: ${stderr}`);
        }
        
        console.log("==Tudo pronto para começar==")
        console.log( stdout )

        res.json(
            {'msg' : stdout}
        );
    });    
});



// Setting the server to listen at port 3000
app.listen(80, function(req, res) {
    console.log("Server start 80");
  });
  

  

// console.log('Testeee')


// exec(`pm2 start bot01`, (error, stdout, stderr) => {
//     if (error) {
//         console.log(`error: ${error.message}`);
//         return
//     }
//     if (stderr) {
//         console.log(`stderr: ${stderr}`);
//     }
//     console.log("==Tudo pronto para começar==")


//     console.log( stdout )
// });


// exec(`pm2 logs bot01 --lines 2`, (error, stdout, stderr) => {
//     if (error) {
//         console.log(`error: ${error.message}`);
//         return
//     }
//     if (stderr) {
//         console.log(`stderr: ${stderr}`);
//     }
//     console.log("==Tudo pronto para começar==")

    
//     console.log( stdout )
// });


