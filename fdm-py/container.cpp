#include<iostream>
#include<vector>

using namespace std;

void init1D(vector<double> &f)
{
  /*
  f.resize(10);
  int imax = f.size();
  for(int i=0; i<imax; ++i){
    f[i] = 1.0;
  }
  */
  f.push_back(1.0);
  f.push_back(2.0);
}

int main()
{

  vector<double> f;

  init1D(f);
  
  int imax = f.size();
  cout<<imax<<endl;
  
}
	
