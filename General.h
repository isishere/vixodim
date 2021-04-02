#include "Student.h"
#include <vector>

#pragma once

class General : public Student
{ 
private:
	std::vector<Student> student;
	size_t mark;
	std::vector<std::vector<std::string>> disciplines;

public:
	General(const std::string& name, const std::string& chair, const size_t& semestr, const size_t& mrk):
		Student(name, chair, semestr), 
		mark(mrk) 
	{ };

};