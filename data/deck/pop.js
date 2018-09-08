'use strict';
var Mockgen = require('../mockgen.js');
/**
 * Operations on /deck/pop
 */
module.exports = {
    /**
     * summary: 
     * description: 
     * parameters: tags, limit
     * produces: 
     * responses: 200, default
     * operationId: deck_pop
     */
    get: {
        200: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck/pop',
                operation: 'get',
                response: '200'
            }, callback);
        },
        default: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck/pop',
                operation: 'get',
                response: 'default'
            }, callback);
        }
    }
};
