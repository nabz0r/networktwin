import React from 'react';
import { Button } from '@mui/material';

const TopologyExporter = ({ topology }) => {
    const exportToGNS3 = () => {
        // Future implementation for GNS3 export
        console.log('Exporting to GNS3:', topology);
    };

    const exportToJSON = () => {
        const jsonTopology = JSON.stringify(topology, null, 2);
        const blob = new Blob([jsonTopology], {type: 'application/json'});
        const href = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = href;
        link.download = 'network_topology.json';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    };

    return (
        <div>
            <Button onClick={exportToGNS3}>Export to GNS3</Button>
            <Button onClick={exportToJSON}>Export JSON</Button>
        </div>
    );
};