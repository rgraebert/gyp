{
  'variables': {
    'chromium_code': 1,
  },
  'includes': [
    '../../build/common.gypi',
  ],
  'targets': [
    {
      'target_name': 'googleurl',
      'type': 'static_library',
      'sources': [
        '../src/gurl.cc',
        '../src/gurl.h',
        '../src/url_canon.h',
        '../src/url_canon_etc.cc',
        '../src/url_canon_fileurl.cc',
        '../src/url_canon_host.cc',
        '../src/url_canon_icu.cc',
        '../src/url_canon_icu.h',
        '../src/url_canon_internal.cc',
        '../src/url_canon_internal.h',
        '../src/url_canon_internal_file.h',
        '../src/url_canon_ip.cc',
        '../src/url_canon_ip.h',
        '../src/url_canon_mailtourl.cc',
        '../src/url_canon_path.cc',
        '../src/url_canon_pathurl.cc',
        '../src/url_canon_query.cc',
        '../src/url_canon_relative.cc',
        '../src/url_canon_stdstring.h',
        '../src/url_canon_stdurl.cc',
        '../src/url_file.h',
        '../src/url_parse.cc',
        '../src/url_parse.h',
        '../src/url_parse_file.cc',
        '../src/url_parse_internal.h',
        '../src/url_util.cc',
        '../src/url_util.h',
      ],
      'dependencies': [
        '../../base/base.gyp:base',
        '../../third_party/icu38/icu38.gyp:icudata',
        '../../third_party/icu38/icu38.gyp:icui18n',
        '../../third_party/icu38/icu38.gyp:icuuc',
      ],
      'direct_dependent_settings': {
        'include_dirs': [
          '../..',
        ],
      },
    },
  ],
}
