#include <string>

#pragma once

class Student
{

protected:

	std::string SNP;
	std::string chair;
	size_t semester;

public:

	Student(const std::string& name = "", const std::string& lvl = "", const size_t& sem = 0) : SNP(name), chair(lvl), semester(sem) { };

	void set_SNP(const std::string& str);

	void set_chair(const std::string& str);

	void set_semester(const size_t& num);

};