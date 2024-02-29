#include<bits/stdc++.h>
using namespace std;

int main(){


  // string s="Prat";
  // if(s==Prat){
  //   cout<<"YEs"<<endl;
  // }

//lets build calculator

  int num1;
  cout<<"Enter the first number: ";
  cin>>num1;

  int num2;
  cout<<"Enter the second number";
  cin>>num2;


  int one;
  cout<<"Enter 1 for addition"<<endl;
   cout<<"Enter 2 for substractinon"<<endl;
    cout<<"Enter 3 for multiplication"<<endl;
    cout<<"Enter 4 for division"<<endl;
  cin>>one;

  if(one>4){
    cout<<"Enter the number between 1 , 2 ,3 and 4 only for operations"<<endl;
  }
  else if(one==1){
       cout<<num1+num2;
  }else if(one==2){
    cout<<num1-num2;
  }
  else if(one==3){
    cout<<num1*num2;
  }
  else if(one==4){
    cout<<num1/num2;
  }

    return 0;
}
