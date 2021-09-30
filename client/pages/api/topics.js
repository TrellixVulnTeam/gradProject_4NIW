import { NextApiRequest, NextApiResponse } from 'next';

export default function getAllTopics(req, res) {
    res.json([{name: 'bruno'}, {name: 'jake'}])
}