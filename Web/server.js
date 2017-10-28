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
});

app.post('/check', urlencodedParser, function(req,res){
  var spawn = require('child_process').spawn;
  console.log(req.body);
  var process = spawn('python',["C:\Users\Yadnesh\Documents\NodeJS\PredictAddict\PredictAddict\Random_Forest_Model\RF.py",req.body.sex,req.body.address,req.body.famsize,req.body.Pstatus,req.body.Medu,req.body.Fedu,req.body.Mjob,req.body.Fjob,req.body.traveltime,req.body.studytime,req.body.failures,req.body.paid,req.body.activities,req.body.famrel,req.body.goout,req.body.percentage]);


  process.stdout.on('data', function (data){

           if(data){
              res.render('warning-page');
           }
           else {
             res.render('success-page');
           }
 });
});

app.get('/success-page',function(req,res){
     res.sendFile(__dirname + '/success-page');
});

app.post('/success-page',urlencodedParser,function(req,res){
     res.render('success-page',{qs:req.body});


});
