cmake_minimum_required(VERSION 2.8.11)
project(ulz C)

include(conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCE_FILES
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sha512/sha512.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_getnextlinelength.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_readline.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_getline.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_close.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_internal.h
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_open.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/fileparser/fileparser_readline_userbuf.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_fromfile.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_new.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_eq.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_copy.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_contains.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_concat.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_tofile.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_fromchar.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_here.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_strdup.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_shiftleft.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_hash.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_shiftright.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_format.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_chomp.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/stringptr_rchr.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptr/read_stdin_line.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/iniparser/iniparser_count_sections.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/iniparser/iniparser.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/timelib/timestamp.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/timelib/getutime.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/timelib/gettimestamp.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/timelib/msleep.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/timelib/microsleep.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/timelib/mspassed.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/optparser/op_init.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/optparser/op_hasflag.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/optparser/op_get.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/optparser/op_printall.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/format/ulz_printf.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/format/ulz_vsnprintf.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/format/ulz_fprintf.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/format/ulz_snprintf.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sblist/sblist_sort.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sblist/sblist_addi.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sblist/sblist_insert.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sblist/sblist_delete.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sblist/sblist.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/sblist/sblist_insert_sorted.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_puterror.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_timestamp.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_putln.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_putd.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_put.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_putc.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/logger/log_puts.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelist/filelist.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_contains.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_find.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_dup_entries.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_freestrings.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptr_replace.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_freeall.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_add_strdup.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_tostring_dos.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_fromfile.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptr_splits.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_tofile.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptrlist_tostring.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/stringptrlist/stringptr_splitc.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/md5/md5str.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/md5/md5.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/hashlist/hashlist.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/hashlist/hashlist_iterator.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/crc32/crc32c.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/kvlist/kvlist.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/int64ToString.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/hexval.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/containsChar.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/base64enc.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/strdup_n.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/strstr_uc.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/uintToString.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/strstar.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/isnumericipv4.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/isAlpha.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/isNumber.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/ipv4fromstring.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/isLower.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/isLetter.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/numberToString.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/conv_cypher.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/raw2hex.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/uint64ToString.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/base64_tbl.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/base64dec.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/strtoint.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/base64enc_str.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/isUpper.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/intToString.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/makeupper.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/rc4.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/stringfromipv4.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/findword.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/makelower.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/hex2raw.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/strlib/strtoint64.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/proclib/process.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/proclib/daemonize.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/getfilemodtime.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/ulz_mkdtemp.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/mktempdir.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/getfileext.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/getfilename.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/getfilesize.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/normalizepath.c
    ${CMAKE_SOURCE_DIR}/source_subfolder/src/filelib/getpathdiff.c
    )

set(INCLUDE_DIR ${CMAKE_SOURCE_DIR}/source_subfolder/include)

add_library(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_include_directories(${CMAKE_PROJECT_NAME} PUBLIC ${INCLUDE_DIR})
set_property(TARGET ${CMAKE_PROJECT_NAME} PROPERTY C_STANDARD 99)

install(TARGETS ${CMAKE_PROJECT_NAME}
        RUNTIME DESTINATION ${CMAKE_INSTALL_PREFIX}/bin
        LIBRARY DESTINATION ${CMAKE_INSTALL_PREFIX}/lib
        ARCHIVE DESTINATION ${CMAKE_INSTALL_PREFIX}/lib)

install(DIRECTORY ${INCLUDE_DIR} DESTINATION ${CMAKE_INSTALL_PREFIX})
