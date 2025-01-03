import React, { useState } from 'react';
import { Button, Dialog, TextField, Select, MenuItem } from '@mui/material';
import Mermaid from 'mermaid';

const TopologyBuilder = () => {
    const [topology, setTopology] = useState({
        nodes: [],
        links: []
    });
    const [dialogOpen, setDialogOpen] = useState(false);
    const [newNode, setNewNode] = useState({
        id: '',
        type: 'router'
    });

    const nodeTypes = [
        'router', 
        'switch', 
        'firewall', 
        'server', 
        'cloud'
    ];

    const generateMermaidGraph = () => {
        let graph = 'graph TD\n';
        
        topology.nodes.forEach(node => {
            graph += `    ${node.id}[${node.id}]\n`;
        });

        topology.links.forEach((link, index) => {
            graph += `    ${link.source} --- ${link.target}\n`;
        });

        return graph;
    };

    const handleAddNode = () => {
        setTopology(prev => ({
            ...prev,
            nodes: [...prev.nodes, {...newNode}]
        }));
        setDialogOpen(false);
    };

    const handleAddLink = () => {
        // Logique d'ajout de liens
    };

    return (
        <div>
            <h2>Network Topology Builder</h2>
            
            <Button 
                variant="contained" 
                onClick={() => setDialogOpen(true)}
            >
                Add Node
            </Button>

            {/* Mermaid Graph Renderer */}
            <div className="mermaid">
                {generateMermaidGraph()}
            </div>

            <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)}>
                <div style={{padding: 20}}>
                    <TextField
                        label="Node ID"
                        value={newNode.id}
                        onChange={(e) => setNewNode(prev => ({
                            ...prev, 
                            id: e.target.value
                        }))}
                    />
                    <Select
                        value={newNode.type}
                        onChange={(e) => setNewNode(prev => ({
                            ...prev,
                            type: e.target.value
                        }))}
                    >
                        {nodeTypes.map(type => (
                            <MenuItem key={type} value={type}>
                                {type.charAt(0).toUpperCase() + type.slice(1)}
                            </MenuItem>
                        ))}
                    </Select>
                    <Button onClick={handleAddNode}>Confirm</Button>
                </div>
            </Dialog>
        </div>
    );
};

export default TopologyBuilder;