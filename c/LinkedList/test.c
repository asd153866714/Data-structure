#include <stdio.h>

struct node {
    struct node *next;
};

typedef struct node Node;

void ListNodePrint(Node *node){
    Node *p;
    for (p=node; p!=NULL; p=p->next){
        printf("%p --> ",p);
    }
}

int main(){
    Node a, b, c;
    a.next = &b;
    b.next = &c;
    c.next = NULL;
    ListNodePrint(&a);
}
