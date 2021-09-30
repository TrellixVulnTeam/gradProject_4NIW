import { NextApiRequest, NextApiResponse } from 'next';

export default function getTopicById(req, res) {
    res.json({byId: req.query.id, message: 'getTopicById'});
}