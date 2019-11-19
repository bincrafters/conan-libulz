from conans import ConanFile, CMake, tools
from conans.errors import ConanInvalidConfiguration
import os


class LibulzConan(ConanFile):
    name = "libulz"
    version = "2d4ec7e"
    description = "A collection of useful functions and data structures to create C apps"
    url = "https://github.com/bincrafters/conan-libulz"
    homepage = "https://github.com/rofl0r/libulz"
    license = "LGPL-2.1"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {'shared': False, 'fPIC': True}
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            self.options.remove("fPIC")

    def configure(self):
        if self.settings.os == "Windows":
            raise ConanInvalidConfiguration("libulz is not supported on Windows")
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def source(self):
        full_version = self.version + "adf6cf6f6ea594340fd94de706fb979ca"
        tools.get("{0}/archive/{1}.zip".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + full_version
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(build_folder=self._build_subfolder)
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="COPYING", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
