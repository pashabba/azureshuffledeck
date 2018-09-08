'use strict';
var Mockgen = require('./mockgen.js');
/**
 * Operations on /deck
 */
module.exports = {
    /**
     * summary: 
     * description: 
     * parameters: tags, limit
     * produces: 
     * responses: 200, default
     * operationId: get_deck
     */
    get: {
        200: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck',
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
                path: '/deck',
                operation: 'get',
                response: 'default'
            }, callback);
        }
    },
    /**
     * summary: 
     * description: Creates a new Deck
     * parameters: deck
     * produces: 
     * responses: 200, default
     * operationId: addDeck
     */
    post: {
        200: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck',
                operation: 'post',
                response: '200'
            }, callback);
        },
        default: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck',
                operation: 'post',
                response: 'default'
            }, callback);
        }
    },
    /**
     * summary: 
     * description: deletes a Deck based on the sessionId
     * parameters: tags, limit
     * produces: 
     * responses: 204, default
     * operationId: delete_deck
     */
    delete: {
        204: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck',
                operation: 'delete',
                response: '204'
            }, callback);
        },
        default: function (req, res, callback) {
            /**
             * Using mock data generator module.
             * Replace this by actual data for the api.
             */
            Mockgen().responses({
                path: '/deck',
                operation: 'delete',
                response: 'default'
            }, callback);
        }
    }
};
