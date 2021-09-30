import { NextApiRequest, NextApiResponse } from 'next';

export default function getProfileById(req, res) {
    res.json({byId: req.query.id, message: 'getProfileById'});
}