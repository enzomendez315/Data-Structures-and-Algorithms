# include <iostream>

using namespace std;

class Node {
    public:
        Node* leftChild;
        int data;
        Node* rightChild;
};

class BST {
    private:
        Node* root;
    public:
        BST(){ root = nullptr; }
        Node* getRoot() { return root; }
        void Insert(int key);
        void InOrder(Node* p);
        Node* Search(int key);
};

void BST::Insert(int key) {
    Node* t = root;
    Node* p;
    Node* r;

    // Root is empty.
    if (root == nullptr) {
        p = new Node;
        p->data = key;
        p->leftChild = nullptr;
        p->rightChild = nullptr;
        root = p;
        return;
    }

    while (t != nullptr) {
        r = t;
        if (key < t->data) {
            t = t->leftChild;
        } else if (key > t->data) {
            t = t->rightChild;
        } else {
            return;
        }
    }

    // Now 't' points at NULL and 'r' points at insert location.
    p = new Node;
    p->data = key;
    p->leftChild = nullptr;
    p->rightChild = nullptr;

    if (key < r->data) {
        r->leftChild = p;
    } else {
        r->rightChild = p;
    }
}

void BST::InOrder(Node* p) {
    if (p) {
        InOrder(p->leftChild);
        cout << p->data << ", " << flush;
        InOrder(p->rightChild);
    }
}

Node* BST::Search(int key) {
    Node* t = root;
    while (t != nullptr) {
        if (key == t->data) {
            return t;
        } else if (key < t->data) {
            t = t->leftChild;
        } else {
            t = t->rightChild;
        }
    }

    return nullptr; 
}

int main() {
    BST bst;

    // Insert.
    bst.Insert(10);
    bst.Insert(5);
    bst.Insert(20);
    bst.Insert(8);
    bst.Insert(30);

    // In order traversal.
    bst.InOrder(bst.getRoot());
    cout << endl;

    // Search.
    Node* temp = bst.Search(2);
    if (temp != nullptr) {
        cout << temp->data << endl;
    } else {
        cout << "Element not found" << endl;
    }

    return 0;
}