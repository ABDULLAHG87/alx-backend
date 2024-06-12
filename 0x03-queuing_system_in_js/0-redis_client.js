import { createClient } from 'redis';
const client = createClient();

(async () => {
  client.on('error', (err) => console.log('Redis client not connected to server:', err));
  client.on('connect', () => console.log('Redis Client connected to the server'));
})();
