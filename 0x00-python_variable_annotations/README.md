# Python - Variable Annotations
Generally, Python is dynamically typed which implies its variables are dynammically
set at run-time, upon assignment of a value to a variable.
``
    def fn(a, b):
        return a + b
``
The types of `a` and `b` are unknown during build-time.
<p> Type annotation provide a patch fix for this. Python will still be dynammically
typed, but with type annotation, there is better code documentation and linting & validation can be achieved.</p>