import React, { useEffect } from 'react';
import mermaid from 'mermaid';

const MermaidGraph = ({ graphDefinition }) => {
    useEffect(() => {
        mermaid.initialize({
            startOnLoad: true,
            theme: 'dark'
        });
        mermaid.contentLoaded();
    }, []);

    useEffect(() => {
        mermaid.init();
    }, [graphDefinition]);

    return (
        <div className="mermaid">
            {graphDefinition}
        </div>
    );
};

export default MermaidGraph;