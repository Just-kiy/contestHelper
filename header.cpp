#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <iomanip>
#include <ctime>
#include <utility>
#include <fstream>

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sqr(x) (x)*(x)
#define forn(i, n) for(int i = 0; i < (int)n; i++)
#define _with_file
#define TASK ""

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef pair <int, int> PII;
typedef pair <ld, ld> PLL;

const ld EPS = 1e-12;
double __t; 

void quit();

main()
{
#ifdef LOCAL
__t = clock();
#ifndef _with_files
freopen("z.in", "rt", stdin);
freopen("z.out", "wt", stdout);
#endif
#endif
#ifdef _with_files
freopen(TASK".in", "rt", stdin);
freopen(TASK".out", "wt", stdout);
#endif

quit();
}

void quit()
{
#ifdef LOCAL
cerr << "\n\nTOTAL TIME: " <<  (clock() - __t)/1000.0 << "s\n";
#endif
exit(0);
}