#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/testing")

class BoostConvertConan(base.BoostBaseConan):
    name = "boost_convert"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_convert"
    lib_short_names = ["convert"]
    header_only_libs = ["convert"]
    b2_requires = [
        "boost_config",
        "boost_core",
        "boost_function_types",
        "boost_lexical_cast",
        "boost_math",
        "boost_mpl",
        "boost_optional",
        "boost_parameter",
        "boost_range",
        "boost_spirit",
        "boost_type_traits"
    ]
