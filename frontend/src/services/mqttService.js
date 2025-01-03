import mqtt from 'mqtt';

class MQTTService {
  constructor(brokerUrl = 'ws://localhost:9001') {
    this.client = null;
    this.brokerUrl = brokerUrl;
  }

  connect() {
    return new Promise((resolve, reject) => {
      this.client = mqtt.connect(this.brokerUrl);

      this.client.on('connect', () => {
        console.log('MQTT Connected');
        resolve(this.client);
      });

      this.client.on('error', (error) => {
        console.error('MQTT Connection Error', error);
        reject(error);
      });
    });
  }

  subscribe(topic) {
    if (!this.client) {
      throw new Error('MQTT Client not connected');
    }
    this.client.subscribe(topic);
  }

  publish(topic, message) {
    if (!this.client) {
      throw new Error('MQTT Client not connected');
    }
    this.client.publish(topic, JSON.stringify(message));
  }

  onMessage(callback) {
    if (!this.client) {
      throw new Error('MQTT Client not connected');
    }
    this.client.on('message', (topic, message) => {
      callback(topic, JSON.parse(message.toString()));
    });
  }
}

export default new MQTTService();