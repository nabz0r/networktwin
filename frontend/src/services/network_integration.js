import { io } from 'socket.io-client';

class NetworkIntegrationService {
    constructor(url = 'ws://localhost:8000/ws/network_simulation') {
        this.socket = null;
        this.url = url;
    }

    connect() {
        this.socket = io(this.url);

        this.socket.on('connect', () => {
            console.log('Connecté au service de simulation');
        });

        this.socket.on('connect_error', (error) => {
            console.error('Erreur de connexion', error);
        });

        return this.socket;
    }

    simulateNetwork(networkType, config) {
        return new Promise((resolve, reject) => {
            this.socket.emit('simulate_network', { type: networkType, config });

            this.socket.on('simulation_result', (result) => {
                resolve(result);
            });

            this.socket.on('error', (error) => {
                reject(error);
            });
        });
    }

    disconnect() {
        if (this.socket) {
            this.socket.disconnect();
        }
    }
}

export default new NetworkIntegrationService();