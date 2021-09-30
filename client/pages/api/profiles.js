import { NextApiRequest, NextApiResponse } from 'next';

export default function getAllProfiles(req, res) {
    if(req.method !== 'GET') {
        res.status(500).json({message: 'sorry, we only accept GET requests.'})
    }

    res.json({hello: 'world', method: req.method})
}