#include <string>

#pragma once

class Abstract
{
public:
	virtual size_t count_excellent() const = 0;
	virtual  std::string& find_student(std::string& name) const = 0;
};