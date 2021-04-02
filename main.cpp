#include <iostream>
#include <vector>
#include <filesystem>
#include <stdexcept>
#include "Student.h"

namespace fs = std::filesystem;

void help()
{
	std::cout << std::endl;
	std::cout << "===================================\n";
	std::cout << "> If you want to create database, press '1'\n"
		"> If you want to see list of current students press '2'\n"
		"> If you want to finish work press '0'\n";
	std::cout << "===================================\n";
	std::cout << std::endl;
}

int main()
{
	std::string str_command;
	int int_command;
	bool flag = true;

	std::cout << "Hello, user!\n";

	try
	{
	do
	{
		help();
		std::cout << "Your choise: ";
		std::cin >> str_command;
		std::transform(str_command.begin(), str_command.end(), str_command.begin(), ::tolower);

		switch (std::stoi(str_command))
		{
		case 1:
		{
			std::string DB_name;
			std::cout << "Name your database: ";
			std::cin >> DB_name;

			std::cout << "\nIf you want to create one type DB press 1;\n"
				<< "If you want to create hybrid DB press 2;\n"
				<< "Your choise: ";
			std::cin >> str_command;

			try
			{
				if (fs::exists(DB_name))
					throw std::exception("The folder with the same name is already exists, try again\n");
				fs::create_directory(DB_name);
				std::cout << "The directory was created sucsessfully.\n";
			}
			catch (const std::exception& error)
			{
				std::cerr << error.what();
			}

			break;
		}

		default:
			std::cout << "Incorrect input\n";
			break;
		}

		} while (str_command != "finish");
	}
	catch(const std::exception& error)
	{
		std::cerr << error.what();
	}

	return 0;
}