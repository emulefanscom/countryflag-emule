﻿# -*- coding: utf-8 -*-
# eMule countryflag
# Copyright (C) 2009-2024 eMuleFans Team
# 
# This program is free software: you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or 
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License 
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# eMule countryflag checksum script
# Contributions: eMuleFans Team
# 


# Import external module.
import hashlib
import os

# Mark file location.
root_path = os.getcwd()
file_list = []
for current_path, sub_folder, file in os.walk(root_path):
	for filename in file:
		file_list.append(os.path.join(current_path, filename))

# Hash files and store the result.
result_list_text_sha3 = []
result_list_text_sha2 = []
result_list_markdown_sha3 = []
result_list_markdown_sha2 = []
for filename_index in file_list:
	with open(filename_index, r"rb") as current_file:
		digest = hashlib.file_digest(current_file, r"sha3_256")
		digest_result = digest.hexdigest()
		result_list_text_sha3.append(r"  * sha3_256(" + filename_index + r") = " + digest_result + "\n")
		result_list_markdown_sha3.append(r"sha3_256(" + filename_index + r") | " + digest_result + r" |" + "\n")
for filename_index in file_list:
	with open(filename_index, r"rb") as current_file:
		digest = hashlib.file_digest(current_file, r"sha256")
		digest_result = digest.hexdigest()
		result_list_text_sha2.append(r"  * sha2_256(" + filename_index + r") = " + digest_result + "\n")
		result_list_markdown_sha2.append(r"sha2_256(" + filename_index + r") | " + digest_result + r" |" + "\n")

# Write the result to text file.
writefile_name = r"checksum.txt"
writefile_handle = open(writefile_name, mode = r"w", encoding = r"utf_8_sig")
writefile_handle.write(r"* Release checksum" + "\n")
for result_index in result_list_text_sha3:
	writefile_handle.write(result_index)
for result_index in result_list_text_sha2:
	writefile_handle.write(result_index)
writefile_handle.close()

# Write the result to markdown file.
writefile_name = r"checksum.md"
writefile_handle = open(writefile_name, mode = r"w", encoding = r"utf_8_sig")
writefile_handle.write(r"Algorithm(File) | Hash |" + "\n")
writefile_handle.write(r":--- | :--- |" + "\n")
for result_index in result_list_markdown_sha3:
	writefile_handle.write(result_index)
for result_index in result_list_markdown_sha2:
	writefile_handle.write(result_index)
writefile_handle.close()

# Pause to show the result.
print()
input("Press \"Return\" to end.")
