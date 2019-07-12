/*C++ version of 1D FDM Heat Equation*/
#include<iostream>
#include<cmath>
#include<vector>
#include<chrono>

using namespace std;
using namespace std::chrono;

void theloop(vector<double> fx, vector<double> fxnew,
	     vector<double> peak, vector<double> tminus,
	     int itermax, int imax, double coeff, double dt)
{

}

int main()
{

  vector<double> peak,tminus;

  peak.resize(1);
  tminus.resize(1);
  
  high_resolution_clock::time_point t1 = high_resolution_clock::now();
  /*Computation loop*/
  for(int i=0; i<1000; ++i){
    /*Do something*/
  }
  high_resolution_clock::time_point t2 = high_resolution_clock::now();

  duration<double> time_span = duration_cast< duration<double> >(t2-t1);
  double elapsed_time = time_span.count(); //in seconds
  cout<<"Time "<<elapsed_time<<" secs"<<endl;
    
  
}
