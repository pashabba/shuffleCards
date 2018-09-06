var express = require("express");
var session = require("express-session");
var bodyParser = require('body-parser');
var redis = require('redis');
const uuidv4 = require('uuid/v4');


var REDISCACHEHOSTNAME = "shuffledeck.redis.cache.windows.net";
var REDISCACHEKEY = "kgExy2sOwju0ZSrs3IKnRPKZau4hcPtIOFzVA9dAdJA=";

var client = redis.createClient(6380, REDISCACHEHOSTNAME,
    {auth_pass: REDISCACHEKEY, tls: {servername: REDISCACHEHOSTNAME}});


var app = express();
app.use(bodyParser.json()); // support json encoded bodies

app.use(session({
    id: uuidv4(), // unique ID for each session
    secret: "hi",
    cookie: { maxAge: 60000 },
    proxy: true,
    resave: true,
    saveUninitialized: true
  })
);

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Authorization, Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Getting or Creating the redis hash set based on sessionID (key)
function reqSession(req, callType){
    if(callType=="get"){
        return new Promise(resolve => client.hgetall(req.sessionID, function (err, replies) {
            if(replies){
                if(replies.dealt == "[]"){ replies.dealt = []}
                if(replies.deck == "[]"){ replies.deck = []}
                resolve(replies);
            }
            else{
                resolve({"deck":[], "dealt":[]});
            }
        }));
    }
    if(callType=="post"){
        return new Promise(function(resolve, reject){
            client.hmset(req.sessionID, "deck", JSON.stringify(req.body));
            client.hmset([req.sessionID, "dealt", "[]"]);
            if(req.body == []){
                resolve({"deck":[], "dealt":[]});
            }else{
                resolve({"deck": req.body, "dealt":[]});
            }
        });
    }
}

// checking the typeof result and make it same across the code
async function checkReqSession(req, callType){
    var x = await reqSession(req, callType);
    if (typeof x == "object"){
        return x
    }
    return JSON.parse(x);
}

// to create a deck, make a post call to this.
app.post("/createDeck", async function(req, res){
    var x = await checkReqSession(req, "post");
    if(x.dealt.length > 0){
        res.send(x);
        return;
    }
    res.send(x.deck);
})

// to get a deck, make a get call to this.
app.get("/getDeck", async function(req, res){
    var x = await checkReqSession(req, "get");
    if(x.dealt.length > 0){
        res.send(x);
        return;
    }
    res.send(x.deck);
});

// using fisher yates shuffle
function shuffle (deck) {
    var i = 0
      , j = 0
      , temp = null
  
    for (i = deck.length - 1; i > 0; i -= 1) {
      j = Math.floor(Math.random() * (i + 1))
      temp = deck[i]
      deck[i] = deck[j]
      deck[j] = temp
    }
    return deck
}

// gets the shuffle cards from shuffle function and set the new value to redis hash set
app.get("/shuffleCard", async function(req, res){
    var x = await checkReqSession(req, "get");
    if(x.deck.length == 0 && x.dealt.length == 0){
        res.send(JSON.stringify(x.deck));
        return;
    }
    else{
        try{
            deck = JSON.stringify(shuffle(JSON.parse(x.deck)));
            await client.hmset(req.sessionID, "deck", deck, function(err, r){
                res.send(deck);
            });
        }
        catch(err){
            res.send([]);
        }
    }
    
})

// pop the card from the deck
app.get("/popCard", async function(req, res){
    var x = await checkReqSession(req, "get");
    if(x.deck.length == 0 && x.dealt.length == 0){
        res.send(JSON.stringify(x.dealt));
        return;
    }else{
        try{
            var deck = JSON.parse(x.deck);
            var dealt = (typeof x.dealt != "object") ? JSON.parse(x.dealt) : x.dealt;
            dealt.push(deck[deck.length-1]);
            deck.pop();
            await client.hmset([req.sessionID, "deck", JSON.stringify(deck), "dealt", JSON.stringify(dealt)], function(err, r){
                res.send(JSON.stringify(dealt));
            });
            return;
        }
        catch(err){
            res.send(JSON.stringify(x.dealt));
            return;
        }    
    }
    
})

app.get("/deck", async function(req, res){
    res.send(await reqSession(req, "get"));
});

app.delete("/deleteDeck", async function(req, res){
    await client.set(req.sessionID, JSON.stringify([]), function(err, r){
        res.send(JSON.stringify([]));
    });
});

var port = process.env.PORT || 5000;

app.listen(port, function () {
    console.log("Listening on port " + port);
});
