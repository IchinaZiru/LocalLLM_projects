const Parser = require('tree-sitter');
const Cpp = require('tree-sitter-cpp');
const fs = require('fs');

const parser = new Parser();
parser.setLanguage(Cpp);

const sourceCode = fs.readFileSync('../yuta/src/Bank_System.cpp', 'utf8');
const tree = parser.parse(sourceCode);

function nodeToJSON(node) {
  const result = {
    type: node.type,
    startPosition: node.startPosition,
    endPosition: node.endPosition,
  };

  if (node.namedChildCount > 0) {
    result.children = [];
    for (let i = 0; i < node.namedChildCount; i++) {
      result.children.push(nodeToJSON(node.namedChild(i)));
    }
  } else {
    // 必要に応じてソースコード断片も含める
    result.text = node.text;
  }

  return result;
}

const ast = nodeToJSON(tree.rootNode);

fs.writeFileSync('ast.json', JSON.stringify(ast, null, 2));
console.log('AST written to ast.json');
