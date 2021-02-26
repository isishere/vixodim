#include <iostream>
#include <chrono>

int plus(double& a, double& b)
{
	return a + b;
}

int main()
{
	double a = 3.14;
	double b = 0.86;

	auto begin = std::chrono::system_clock::now();
	std::cout << plus(a, b) << std::endl;
	auto end = std::chrono::system_clock::now();

	std::cout << "Time: " << std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count();
	return 0;
}
