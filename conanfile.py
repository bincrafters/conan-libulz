#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class LibulzConan(ConanFile):
    name = "libulz"
    version = "2d4ec7e"
    description = "A collection of useful functions and data structures to create C apps"
    url = "https://github.com/bincrafters/conan-libulz"
    homepage = "https://github.com/rofl0r/libulz"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            self.options.remove("fPIC")

    def configure(self):
        if self.settings.os == "Windows":
            raise Exception("libulz is not supported on Windows")
        del self.settings.compiler.libcxx

    def source(self):
        full_version = self.version + "adf6cf6f6ea594340fd94de706fb979ca"
        tools.get("{0}/archive/{1}.zip".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + full_version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
