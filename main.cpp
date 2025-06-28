#include <iostream>
using namespace std;

int main()
{
    int num1, num2;
    char op;

    cout << "Enter an number:- ";
    cin >> num1;

    cout << "Enter an number:- ";
    cin >> num2;

    cout << "Choose an Operator:- ";
    cin >> op;

    if(op == '+')
    {
        cout << num1 + num2;
    }
    else if(op == '-')
    {
        cout << num1 - num2;
    }
    else if(op == '*')
    {
        cout << num1 * num2;
    }
    else if(op == '/')
    {
        cout << num1 / num2;
    }
    else
    {
        cout << "Wrong Operator!!!";
    }

    return 0;
}
