import React from 'react';
import TopologyBuilder from '../components/TopologyBuilder';
import TopologyExporter from '../components/TopologyExporter';

const NetworkTopologyPage = () => {
    return (
        <div>
            <h1>Network Topology Designer</h1>
            <TopologyBuilder />
            <TopologyExporter />
        </div>
    );
};

export default NetworkTopologyPage;