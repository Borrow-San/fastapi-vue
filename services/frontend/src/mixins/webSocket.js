export default function connectWebSocket() {
  const socket = new WebSocket(`ws://${process.env.VUE_APP_BACKEND_DOMAIN}/ws`);

  socket.addEventListener('open', (event) => {
    console.log('WebSocket connected', event);
  });

  socket.addEventListener('message', (event) => {
    console.log('Received WebSocket message:', event.data);
  });

  socket.addEventListener('error', (event) => {
    console.error('WebSocket error:', event);
  });

  socket.addEventListener('close', (event) => {
    console.log('WebSocket closed:', event.code, event.reason);
  });

  return socket;
}