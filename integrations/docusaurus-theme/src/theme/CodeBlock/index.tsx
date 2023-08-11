import React from 'react';

import CodeBlock from '@theme-init/CodeBlock'
import type { DocslabCodeBlockProps } from '../types';


function componentWrapper(Component: typeof CodeBlock)
{
    return (props: DocslabCodeBlockProps) => {
        if (props.docslab) {
        }
        return <CodeBlock {...props} />;
    };
}

export default componentWrapper(CodeBlock);
