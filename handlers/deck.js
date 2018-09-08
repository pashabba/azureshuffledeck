'use strict';
var REDISCACHEHOSTNAME = "shuffledeck.redis.cache.windows.net";
var REDISCACHEKEY = "kgExy2sOwju0ZSrs3IKnRPKZau4hcPtIOFzVA9dAdJA=";
var redis = require('redis');

var client = redis.createClient(6380, REDISCACHEHOSTNAME,
    {auth_pass: REDISCACHEKEY, tls: {servername: REDISCACHEHOSTNAME}});


module.exports = {
     get: function deck_get(req, res) {
    	 console.log(req.sessionID);
    	 return new Promise(resolve => client.hgetall(req.sessionID, function (err, replies) {
             if(replies){
                 replies.dealt = ((typeof replies.dealt == "string") ? JSON.parse(replies.dealt) : replies.dealt);
                 replies.deck = ((typeof replies.deck == "string") ? JSON.parse(replies.deck) : replies.deck);
                 var reply = ((replies.dealt!=[]) ? replies : replies.deck);
                 res.json(reply);
             }
             else{
                 res.json({"deck":[]});
             }
         }));
    	 res.json([])
     },
     post: function deck_post(req, res){
    	 return new Promise(function(resolve, reject){
             client.hmset(req.sessionID, "deck", JSON.stringify(req.body));
             client.hmset([req.sessionID, "dealt", "[]"]);
             if(req.body == []){
                 res.json({"deck":[], "dealt":[]});
             }else{
            	 res.json({"deck": req.body, "dealt":[]});
             }
         });

     },
     delete: function deck_delete(req, res){
    	 return new Promise(function(resolve, reject){
             client.hmset(req.sessionID, "deck", "[]");
             client.hmset([req.sessionID, "dealt", "[]"]);
             if(req.body == []){
                 res.json({"deck":[], "dealt":[]});
             }else{
            	 res.json({"deck": req.body, "dealt":[]});
             }
         });
     }
 };