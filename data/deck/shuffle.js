'use strict';
var Mockgen = require('../mockgen.js');
/**
 * Operations on /deck/shuffle
 */
module.exports = {
    /**
     * summary: 
     * description: 
     * parameters: tags, limit
     * produces: 
     * responses: 200, default
     * operationId: deck_shuffle
     */
    get: {
        200: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck/shuffle',
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
                path: '/deck/shuffle',
                operation: 'get',
                response: 'default'
            }, callback);
        }
    }
};
