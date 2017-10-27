var express = require('express');
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({extended:false});

var app = express();

app.set('view engine','ejs');

app.listen(3000,function(res,req){
            console.log('server->on');
});

app.get('/mainpage',function(res,res){
        res.sendFile(__dirname + '/mainpage.html');
});

app.get('/response',function(req,res){
      res.sendFile(__dirname + '/response.html');
});

app.post('/response',urlencodedParser,function(req,res){
    res.render('response',{qs:req.body});
    console.log(JSON.stringify(req.body.email));
    console.log(JSON.stringify(req.body.password));
});
