cmake_minimum_required(VERSION 3.15)

project(LeetCode)

set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang++)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(fmt REQUIRED)

# NOTE: nix requires extra steps because include folders are in the nix store
# https://mzhang.io/posts/2022-03-03-clangd-in-nix/
#
# though, this is not good practice according to cmake docs
if(DEFINED ENV{IN_NIX_SHELL} AND CMAKE_EXPORT_COMPILE_COMMANDS)
  set(CMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES
      ${CMAKE_CXX_IMPLICIT_INCLUDE_DIRECTORIES})
endif()

add_executable(twoSum 1.cpp)
add_executable(groupAnagrams 49.cpp)
add_executable(hasDuplicate 217.cpp)
add_executable(productExceptSelf 238.cpp)
add_executable(isAnagram 242.cpp)
add_executable(encodeAndDecodeString 271.cpp)
add_executable(topKFrequent 347.cpp)

target_link_libraries(twoSum fmt::fmt)
target_link_libraries(groupAnagrams fmt::fmt)
target_link_libraries(productExceptSelf fmt::fmt)
target_link_libraries(encodeAndDecodeString fmt::fmt)
target_link_libraries(topKFrequent fmt::fmt)
