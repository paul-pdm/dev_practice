#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *left;
  Node *right;

  Node(int d) {
  data = d;
  left = null ptr;
  right = nullptr;
  }
}

/* BST : Binary Search Tree
*/
class BST {
private:
  Node *root;
  int size;

public:
  BST(){
    root = nullptr;
    size = 0;
  }
  ~BST() {
    clear(root);
  }
  /*
  recursively clears the give subtree at node n
  */
  void clear(Node *n) {
    if (n != nullptr)
      clear(n->left);
      clear(n->right);
  }
}
