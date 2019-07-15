#include<iostream>
#include<vector>  //for vector container
#include<cmath>
#include<chrono>  //for high_resolution_clock class
#include<fstream> //file I/O
#include<utility> //for swap(a,b) C++11
#include<iomanip> // setprecision()

#define pi 4.0*atan(1.0)

using namespace std;
using namespace std::chrono;

double theloop2D(vector< vector<double> > &fx,
		 vector< vector<double> > &fxnew,
		 vector<double> &peak,
		 vector<double> &tminus,
		 int itermax, int imax, int jmax, int rec,
		 double coeff, double dt)
{
  int i, j, iter;
  double ops = 0.0;
  double var1, var2;
  iter = 0;
  do{

    for(i=1; i<imax-1; ++i){
      for(j=1; j<jmax-1; ++j){
	fxnew[i][j] = fx[i][j] + coeff*(fx[i-1][j]
					-2.0*fx[i][j]
					+fx[i+1][j]
					+fx[i][j-1]
					-2.0*fx[i][j]
					+fx[i][j+1]
					); 
      }
    }
    swap(fx,fxnew);
    iter +=1;
    ops += 7.0*(double)(imax-2)*(double)(jmax-2);
    
    if(iter%rec==0){
      /*For recording*/
    var1 = fx[imax/2][jmax/2];
    var2 = dt*(iter+1);
    peak.push_back(var1);
    tminus.push_back(var2);
      cout<<"Time: "<<var2<<" Peak : "<<var1<<endl;
     }
    
    
  }while(iter<itermax);

  return ops;
}

void init(vector< vector<double> > &fx,
	  vector< vector<double> > &fxnew,
	  vector<double> &peak,
	  vector<double> &tminus,
	  int &imax, int &jmax, int &itermax, int &rec,
	  double &dt, double &dx, double &dy, double &coeff)
{
  cout<<"Enter imax (imax=jmax) "<<endl;
  cin>>imax;
  cout<<"Enter maximum iteration "<<endl;
  cin>>itermax;
  cout<<"Enter interval iteration"<<endl;
  cin>>rec;

  jmax = imax;
  dx = 1.0/(double)(imax-1);
  dy = 1.0/(double)(jmax-1);
  dt = 0.1*(dx*dx);
  double kappa = 0.25;
  coeff = kappa*dt/(dx*dx);

  fx.resize(imax);
  fxnew.resize(imax);
  for(int i=0; i<imax; ++i){
    fx[i].resize(jmax);
    fxnew[i].resize(jmax);
  }
  
  //initiate value for vector
  for(int i=0; i<imax; ++i){
    for(int j=0; j<jmax; ++j){
      fx[i][j] = sin(i*dx*pi)*sin(j*dy*pi);
      fxnew[i][j] = 0.0;
    }
  }
  peak.push_back(fx[imax/2][jmax/2]);
  tminus.push_back(0.0);
      
}


int main(int argc, char* argv[])
{

  int imax, jmax, itermax, rec;
  double dt, dx, dy, coeff;

  vector< vector<double> > fx, fxnew;
  vector<double> peak, tminus;

  init(fx, fxnew, peak, tminus,
       imax, jmax, itermax, rec,
       dt, dx, dy, coeff);

  
  high_resolution_clock::time_point t1 = high_resolution_clock::now();


  double ops = theloop2D(fx,fxnew,peak,tminus,
		 itermax, imax, jmax, rec,
		 coeff, dt);

  
  high_resolution_clock::time_point t2 = high_resolution_clock::now();
  duration<double> time_span = duration_cast< duration<double> >(t2-t1);
  double elapsed_time = time_span.count(); //in seconds
  cout<<"Elapsed time: "<< elapsed_time<<" secs"<<endl;

  double flops = (ops/elapsed_time)*1.0e-9;
  cout<<setprecision(8)<<"Performance: "<<flops<<" GFLOPS"<<endl;
  
}
