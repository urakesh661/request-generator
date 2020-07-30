# request-generator

This script is used for generating multiple paths from a single url.It ignores the values after question mark in the request if it exists.
This can be usefull if you want to try new multiple paths.

Usage:

A. python3 request_generator.py -r "v1/user/info/66?param=98"


v1/user/info/66

v1/user/66/info

v1/info/user/66

v1/info/66/user

v1/66/user/info

v1/66/info/user

v1/user/info

v1/user/66

v1/info/user

v1/info/66

v1/66/user

v1/66/info

v1/user

v1/info

v1/66


B. python3 request_generator.py -r "v1/user/info/66"         

v1/user/info/66

v1/user/66/info

v1/info/user/66

v1/info/66/user

v1/66/user/info

v1/66/info/user

v1/user/info

v1/user/66

v1/info/user

v1/info/66

v1/66/user

v1/66/info

v1/user

v1/info

v1/66

C. python3 request_generator.py -r "user/info/66" 

user/info/66

user/66/info

info/user/66

info/66/user

66/user/info

66/info/user

user/info

user/66

info/user

info/66

66/user

66/info

user

info

66


Credits:Script is inspired from "@healthyoutlet",<a href="https://github.com/tehryanx/sprawl" style="font-size: 11px;" target="_self">sprawl</a> script.
