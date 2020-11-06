#include<iostream>
#include<string>
using namespace std;

int main(){
    string as,bs;
    int an[101]={0},bn[101]={0},c[202]={0},aLen,bLen,cLen;
    
    cin>>as>>bs;
    
    aLen=as.length();
    bLen=bs.length();
    
    //倒序存储两个数于整型数组中 
    for(int i=0;i<aLen;i++){
        an[aLen-i-1]=as[i]-'0';
    }
    
    for(int i=0;i<bLen;i++){
        bn[bLen-i-1]=bs[i]-'0';
    }

    //进行乘法运算，结果存于c[]
    for(int i=0;i<bLen;i++){
        for(int j=0;j<aLen;j++){
            c[i+j]+=an[j]*bn[i];
            c[i+j+1]+=c[i+j]/10;
            c[i+j]%=10;
        }
    }
     
    cLen=aLen+bLen;
    
    //删除结果高位的前缀0 
    while(c[cLen-1]==0  && cLen>1){
        cLen--;
    }
    
    //将结果倒序输出
    for(int i=cLen-1;i>=0;i--){
        cout<<c[i];
    }
    cout<<endl;
    
    return 0;
}