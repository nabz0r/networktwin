import React, { useState, useEffect } from 'react';
import { ForceGraph3D } from 'react-force-graph';
import * as THREE from 'three';

const LEOConstellationVisualization = ({ satellites }) => {
    const [graphData, setGraphData] = useState({
        nodes: [],
        links: []
    });

    useEffect(() => {
        if (!satellites || satellites.length === 0) return;

        const nodes = satellites.map(sat => ({
            id: sat.id,
            name: sat.id,
            val: sat.bandwidth, // Taille du nœud basée sur la bande passante
            color: getNodeColor(sat.reliability),
            x: sat.position[0],
            y: sat.position[1],
            z: sat.position[2]
        }));

        const links = satellites
            .filter(sat => sat.id !== 'ground_station')
            .map(sat => ({
                source: 'ground_station',
                target: sat.id
            }));

        setGraphData({ nodes, links });
    }, [satellites]);

    const getNodeColor = (reliability) => {
        // Couleur basée sur la fiabilité : vert (haute) à rouge (basse)
        const hue = (reliability * 120).toFixed(0); // 0-120 : vert à rouge
        return `hsl(${hue}, 70%, 50%)`;
    };

    return (
        <div style={{ height: '500px' }}>
            <ForceGraph3D
                graphData={graphData}
                nodeColor={node => node.color}
                nodeVal={node => node.val}
                linkColor={() => 'gray'}
                backgroundColor="black"
                nodeThreeObject={node => {
                    const sprite = new THREE.Sprite();
                    sprite.material.color.set(node.color);
                    sprite.scale.set(10, 10, 10);
                    return sprite;
                }}
            />
        </div>
    );
};

export default LEOConstellationVisualization;