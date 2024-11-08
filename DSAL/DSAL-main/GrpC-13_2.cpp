#include <iostream>
using namespace std;

#define MAX 10

struct node {
    int vertex;
    struct node* next;
};

class Lgraph {
private:
    node* head[MAX];
    int visited[MAX];
    int qu[MAX], front, rear;

public:
    Lgraph()
    {
        int v1;
        for (v1 = 0; v1 < MAX; v1++)
            visited[v1] = 0;
        front = rear = -1;
        for (v1 = 0; v1 < MAX; v1++)
            head[v1] = NULL;
    }

    void create()
    {
        int v1, v2;
        char ans = 'y';
        node* New, * first;
        cout << "\n\nEnter vertices no. beginning from 0";
        do {
            cout << "\nEnter edge of graph: \n";
            cin >> v1 >> v2;
            if (v1 >= MAX || v2 >= MAX)
                cout << "Invalid vertex";
            else {
                New = new node;
                if (New == NULL)
                    cout << "Insufficient memory";
                New->vertex = v2;
                New->next = NULL;
                first = head[v1];
                if (first == NULL)
                    head[v1] = New;
                else {
                    while (first->next != NULL)
                        first = first->next;
                    first->next = New;
                }
                New = new node;
                if (New == NULL)
                    cout << "Insufficient memory";
                New->vertex = v1;
                New->next = NULL;
                first = head[v2];
                if (first == NULL)
                    head[v2] = New;
                else {
                    while (first->next != NULL)
                        first = first->next;
                    first->next = New;
                }
            }
            cout << "\nWant to add more?(y/n): ";
            cin >> ans;
        } while (ans == 'y');
    }

    void bfs(int v1)
    {
        int i;
        node* first;
        qu[++rear] = v1;
        while (front != rear) {
            i = qu[++front];
            if (visited[i] == 0) {
                cout << endl << i;
                visited[i] = 1;
            }
            first = head[i];
            while (first != NULL) {
                if (visited[first->vertex] == 0)
                    qu[++rear] = first->vertex;
                first = first->next;
            }
        }
    }
};

int main()
{
    int v1;
    char ans;
    Lgraph o;
    o.create();
    cout << "\nEnter vertex to travel from: ";
    cin >> v1;
    if (v1 >= MAX)
        cout << "ERROR!";
    else {
        cout << "\nBFS IS: \n";
        o.bfs(v1);
    }
    return 0;
}

