import { useState, useEffect } from 'react';
import WebSocketService from '../services/websocketService';

const useNetworkUpdates = () => {
  const [networkData, setNetworkData] = useState({
    nodes: [],
    links: [],
    stats: {}
  });

  useEffect(() => {
    const socket = WebSocketService.connect();

    WebSocketService.subscribeToNetworkUpdates((data) => {
      setNetworkData(prevData => ({
        ...prevData,
        ...data
      }));
    });

    return () => {
      WebSocketService.disconnect();
    };
  }, []);

  return networkData;
};

export default useNetworkUpdates;