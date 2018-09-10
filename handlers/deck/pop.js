'use strict';
var REDISCACHEHOSTNAME = "shuffledeck.redis.cache.windows.net";
var REDISCACHEKEY = "kgExy2sOwju0ZSrs3IKnRPKZau4hcPtIOFzVA9dAdJA=";
var redis = require('redis');

var client = redis.createClient(6380, REDISCACHEHOSTNAME,
    {auth_pass: REDISCACHEKEY, tls: {servername: REDISCACHEHOSTNAME}});


module.exports = {
     get: function deck_pop(req, res) {
    	 return new Promise(resolve => client.hgetall(req.sessionID, function (err, replies) {
             if(replies){
                 replies.dealt = ((typeof replies.dealt == "string") ? JSON.parse(replies.dealt) : replies.dealt);
                 replies.deck = ((typeof replies.deck == "string") ? JSON.parse(replies.deck) : replies.deck);
                 if(replies.deck == [] && replies.dealt == [] ){
                	 res.json({"last card popped":[]});
                     return;
                 }
                 replies.dealt.push(replies.deck[replies.deck.length-1]);

                 var pop = replies.deck[replies.deck.length-1]
                 res.json({"last card popped":replies.deck[replies.deck.length-1]});
                 replies.deck.pop();
                 return new Promise(function(resolve, reject){
		             client.hmset(req.sessionID, "deck", JSON.stringify(replies.deck));
		             client.hmset([req.sessionID, "dealt", JSON.stringify(replies.dealt)]);
                 });
             }
             else{
                res.json({"last card popped":[]});
             }
    	 }));
     }
 };