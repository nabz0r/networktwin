import io from 'socket.io-client';

class WebSocketService {
  constructor(url = 'http://localhost:5000') {
    this.socket = null;
    this.url = url;
  }

  connect() {
    this.socket = io(this.url);

    this.socket.on('connect', () => {
      console.log('WebSocket Connected');
    });

    this.socket.on('connect_error', (error) => {
      console.error('WebSocket Connection Error', error);
    });

    return this.socket;
  }

  subscribeToNetworkUpdates(callback) {
    if (!this.socket) {
      throw new Error('WebSocket not connected');
    }

    this.socket.on('network_update', (data) => {
      callback(data);
    });
  }

  disconnect() {
    if (this.socket) {
      this.socket.disconnect();
    }
  }
}

export default new WebSocketService();