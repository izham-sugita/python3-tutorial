/*C++ version of 1D FDM Heat Equation*/
#include<iostream>
#include<cmath>
#include<vector>
#include<chrono>
#include<algorithm> //for swap(a,b) C++98
#include<fstream>

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
  vector<double> fx, fxnew;

  int itermax = 5000;

  int imax = 100;

  double dx = 1.0/imax;
  double dt = 0.1*dx*dx;
  const double pi = 4.0*atan(1.0);

  double kappa = 1.0;
  double coeff = kappa*dt/(dx*dx);
  
  //peak.resize(1);
  //tminus.resize(1);

  fx.resize(imax);
  fxnew.resize(imax);

  //initiate value for fx
  for(int i=0; i<imax; ++i){
    fx[i] = sin(i*dx*pi);
    fxnew[i] = 0.0;
  }
  
  //initiate peak, tminus
  //peak[0] = 0.0;
  //tminus[0] = 0.0;

  
  high_resolution_clock::time_point t1 = high_resolution_clock::now();
  /*Computation loop*/
  for(int step=0; step<itermax; ++step){
    /*Do something*/
    for(int i=1; i<imax-1; ++i){
      fxnew[i] = fx[i] + coeff*(fx[i-1] -2.0*fx[i]
				+fx[i+1]);
    }
    peak.push_back(fxnew[imax/2]);
    tminus.push_back((step+1)*dt);
    /*Update by swap*/
    swap(fx,fxnew);
  }
  high_resolution_clock::time_point t2 = high_resolution_clock::now();

  duration<double> time_span = duration_cast< duration<double> >(t2-t1);
  double elapsed_time = time_span.count(); //in seconds

  cout<<"Iteration: "<<itermax<<" steps"<<endl;
  cout<<"Time "<<elapsed_time<<" secs"<<endl;

  cout<<fx.size()<<endl;
  
  fstream fp;
  fp.open("decay-cpp.csv", ios::out);
  int row=0;
  fp<<"time, fx_peak\n";
  do{
    fp<<tminus[row]<<", "<<peak[row]<<"\n";
    row +=1;
  }while(row<tminus.size());
  
  fp.close();
  
}
